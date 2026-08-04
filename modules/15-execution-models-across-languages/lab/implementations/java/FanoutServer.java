import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.lang.management.ManagementFactory;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.Semaphore;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.regex.Pattern;

public final class FanoutServer {
  private static final Pattern REQUEST_ID = Pattern.compile("^[A-Za-z0-9_-]{1,64}$");
  private static final Pattern CHILD_ID = Pattern.compile("^[a-z0-9-]{1,32}$");
  private static final Set<String> REQUEST_KEYS = Set.of("request_id", "deadline_ms", "concurrency_limit", "children");
  private static final Set<String> CHILD_KEYS = Set.of("child_id", "required", "delay_ms", "payload_bytes", "mode");
  private static final String FAULT = System.getenv().getOrDefault("COURSE_FAULT", "none");
  private static final String SCENARIO = System.getenv().getOrDefault("COURSE_SCENARIO", "contract");
  private static final Semaphore GLOBAL_ADMISSION = new Semaphore(64);
  private static final AtomicInteger ACTIVE_TASKS = new AtomicInteger();
  private static final AtomicInteger MAX_ACTIVE = new AtomicInteger();
  private static final AtomicInteger OPEN_RESOURCES = new AtomicInteger();
  private static final long INITIAL_GC_COLLECTIONS = gcCollections();
  private static final long INITIAL_GC_TIME_MS = gcTimeMs();

  record Child(String id, boolean required, int delay, int bytes, String mode) {}
  record Request(String id, int deadline, int limit, List<Child> children) {}
  record ChildResult(String id, String status, double elapsedMs) {}

  private static final class JsonParser {
    private final String text;
    private int position;
    JsonParser(String text) { this.text = text; }
    Object parse() {
      Object value = value();
      whitespace();
      if (position != text.length()) throw new IllegalArgumentException("trailing JSON");
      return value;
    }
    private Object value() {
      whitespace();
      if (position >= text.length()) throw new IllegalArgumentException("missing JSON value");
      return switch (text.charAt(position)) {
        case '{' -> object();
        case '[' -> array();
        case '"' -> string();
        case 't' -> literal("true", Boolean.TRUE);
        case 'f' -> literal("false", Boolean.FALSE);
        case 'n' -> literal("null", null);
        default -> number();
      };
    }
    private Map<String, Object> object() {
      position++;
      Map<String, Object> result = new LinkedHashMap<>();
      whitespace();
      if (consume('}')) return result;
      while (true) {
        whitespace();
        String key = string();
        if (result.containsKey(key)) throw new IllegalArgumentException("duplicate key");
        whitespace();
        expect(':');
        result.put(key, value());
        whitespace();
        if (consume('}')) return result;
        expect(',');
      }
    }
    private List<Object> array() {
      position++;
      List<Object> result = new ArrayList<>();
      whitespace();
      if (consume(']')) return result;
      while (true) {
        result.add(value());
        whitespace();
        if (consume(']')) return result;
        expect(',');
      }
    }
    private String string() {
      expect('"');
      StringBuilder result = new StringBuilder();
      while (position < text.length()) {
        char current = text.charAt(position++);
        if (current == '"') return result.toString();
        if (current < 0x20) throw new IllegalArgumentException("control character");
        if (current != '\\') { result.append(current); continue; }
        if (position >= text.length()) throw new IllegalArgumentException("bad escape");
        char escaped = text.charAt(position++);
        switch (escaped) {
          case '"', '\\', '/' -> result.append(escaped);
          case 'b' -> result.append('\b');
          case 'f' -> result.append('\f');
          case 'n' -> result.append('\n');
          case 'r' -> result.append('\r');
          case 't' -> result.append('\t');
          case 'u' -> {
            if (position + 4 > text.length()) throw new IllegalArgumentException("bad unicode escape");
            result.append((char) Integer.parseInt(text.substring(position, position + 4), 16));
            position += 4;
          }
          default -> throw new IllegalArgumentException("bad escape");
        }
      }
      throw new IllegalArgumentException("unterminated string");
    }
    private Long number() {
      int start = position;
      if (consume('-')) { /* sign */ }
      if (position >= text.length() || !Character.isDigit(text.charAt(position))) throw new IllegalArgumentException("bad number");
      if (text.charAt(position) == '0') position++;
      else while (position < text.length() && Character.isDigit(text.charAt(position))) position++;
      if (position < text.length() && ".eE".indexOf(text.charAt(position)) >= 0) throw new IllegalArgumentException("integer required");
      return Long.parseLong(text.substring(start, position));
    }
    private Object literal(String expected, Object value) {
      if (!text.startsWith(expected, position)) throw new IllegalArgumentException("bad literal");
      position += expected.length();
      return value;
    }
    private void whitespace() { while (position < text.length() && Character.isWhitespace(text.charAt(position))) position++; }
    private boolean consume(char expected) { if (position < text.length() && text.charAt(position) == expected) { position++; return true; } return false; }
    private void expect(char expected) { if (!consume(expected)) throw new IllegalArgumentException("expected " + expected); }
  }

  @SuppressWarnings("unchecked")
  static Request parse(String json) {
    try {
      Object root = new JsonParser(json).parse();
      if (!(root instanceof Map<?, ?> raw) || !raw.keySet().equals(REQUEST_KEYS)) return null;
      Map<String, Object> object = (Map<String, Object>) raw;
      if (!(object.get("request_id") instanceof String id) || !(object.get("deadline_ms") instanceof Long deadline) ||
          !(object.get("concurrency_limit") instanceof Long limit) || !(object.get("children") instanceof List<?> rawChildren)) return null;
      if (deadline < Integer.MIN_VALUE || deadline > Integer.MAX_VALUE || limit < Integer.MIN_VALUE || limit > Integer.MAX_VALUE) return null;
      List<Child> children = new ArrayList<>();
      Set<String> ids = new HashSet<>();
      for (Object value : rawChildren) {
        if (!(value instanceof Map<?, ?> rawChild)) return null;
        Map<String, Object> child = (Map<String, Object>) rawChild;
        Set<String> keys = child.keySet();
        if (!CHILD_KEYS.containsAll(keys) || !keys.containsAll(Set.of("child_id", "required", "delay_ms", "payload_bytes"))) return null;
        if (!(child.get("child_id") instanceof String childId) || !(child.get("required") instanceof Boolean required) ||
            !(child.get("delay_ms") instanceof Long delay) || !(child.get("payload_bytes") instanceof Long bytes)) return null;
        Object rawMode = child.get("mode");
        if (rawMode != null && !(rawMode instanceof String)) return null;
        String mode = (String) rawMode;
        if (!ids.add(childId) || delay < Integer.MIN_VALUE || delay > Integer.MAX_VALUE || bytes < Integer.MIN_VALUE || bytes > Integer.MAX_VALUE) return null;
        children.add(new Child(childId, required, delay.intValue(), bytes.intValue(), mode));
      }
      Request request = new Request(id, deadline.intValue(), limit.intValue(), children);
      return valid(request) ? request : null;
    } catch (RuntimeException error) {
      return null;
    }
  }

  static boolean valid(Request request) {
    return request != null && REQUEST_ID.matcher(request.id).matches() && request.deadline >= 50 && request.deadline <= 5000 &&
        request.limit >= 1 && request.limit <= 64 && request.children.size() >= 1 && request.children.size() <= 16 &&
        request.children.stream().allMatch(child -> CHILD_ID.matcher(child.id).matches() && child.delay >= 0 && child.delay <= 10000 &&
            child.bytes >= 0 && child.bytes <= 2_097_152 && (child.mode == null || Set.of("ok", "error", "invalid").contains(child.mode)));
  }

  private static ChildResult work(Child child, long deadlineAt) throws InterruptedException {
    long began = System.nanoTime();
    int active = ACTIVE_TASKS.incrementAndGet();
    MAX_ACTIVE.accumulateAndGet(active, Math::max);
    OPEN_RESOURCES.incrementAndGet();
    try {
      byte[] allocation = new byte[child.bytes];
      long remaining = Math.max(0, deadlineAt - System.nanoTime());
      if (remaining == 0) return new ChildResult(child.id, "timeout", 0);
      long sleep = Math.min(child.delay, Math.max(1, (remaining + 999_999) / 1_000_000));
      Thread.sleep(sleep);
      if (allocation.length > 0) allocation[0] = 0;
      String status = child.delay * 1_000_000L >= remaining ? "timeout" : child.mode == null ? "ok" : child.mode;
      return new ChildResult(child.id, status, (System.nanoTime() - began) / 1_000_000.0);
    } finally {
      ACTIVE_TASKS.decrementAndGet();
      if (!FAULT.equals("resource_leak")) OPEN_RESOURCES.decrementAndGet();
    }
  }

  static String run(Request request) throws InterruptedException {
    long start = System.nanoTime();
    long deadlineAt = start + request.deadline * 1_000_000L;
    Semaphore localAdmission = new Semaphore(Math.min(request.limit, request.children.size()));
    AtomicInteger localActive = new AtomicInteger();
    AtomicInteger localMax = new AtomicInteger();
    List<Future<ChildResult>> futures = new ArrayList<>();
    try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
      for (Child child : request.children) {
        localAdmission.acquire();
        boolean globalHeld = !FAULT.equals("worker_exhaustion");
        if (globalHeld) GLOBAL_ADMISSION.acquire();
        futures.add(executor.submit(() -> {
          int active = localActive.incrementAndGet();
          localMax.accumulateAndGet(active, Math::max);
          try { return work(child, deadlineAt); }
          finally {
            localActive.decrementAndGet();
            localAdmission.release();
            if (globalHeld) GLOBAL_ADMISSION.release();
          }
        }));
      }
      List<ChildResult> rows = new ArrayList<>();
      for (Future<ChildResult> future : futures) {
        try { rows.add(future.get()); }
        catch (Exception error) { rows.add(new ChildResult("internal", "error", 0)); }
      }
      rows.sort(Comparator.comparing(ChildResult::id));
      Map<String, Boolean> required = new HashMap<>();
      for (Child child : request.children) required.put(child.id, child.required);
      boolean requiredFailed = rows.size() != request.children.size() || rows.stream().anyMatch(row -> required.getOrDefault(row.id, true) && !row.status.equals("ok"));
      boolean optionalFailed = rows.stream().anyMatch(row -> !row.status.equals("ok"));
      String outcome = requiredFailed ? "failed" : optionalFailed ? "partial" : "complete";
      return responseJson(request.id, outcome, rows, (System.nanoTime() - start) / 1_000_000.0, localMax.get(), localActive.get(), 0);
    }
  }

  private static String quote(String value) { return "\"" + value.replace("\\", "\\\\").replace("\"", "\\\"") + "\""; }
  private static String responseJson(String requestId, String outcome, List<ChildResult> rows, double elapsed, int max, int active, int resources) {
    List<String> children = rows.stream().map(row -> "{\"child_id\":" + quote(row.id) + ",\"status\":" + quote(row.status) + ",\"elapsed_ms\":" + row.elapsedMs + "}").toList();
    return "{\"request_id\":" + quote(requestId) + ",\"runtime\":\"java\",\"outcome\":" + quote(outcome) + ",\"children\":[" + String.join(",", children) + "],\"elapsed_ms\":" + elapsed + ",\"max_in_flight\":" + max + ",\"cleanup\":{\"active_tasks\":" + active + ",\"open_resources\":" + resources + "}}";
  }

  private static long gcCollections() { return ManagementFactory.getGarbageCollectorMXBeans().stream().mapToLong(bean -> Math.max(0, bean.getCollectionCount())).sum(); }
  private static long gcTimeMs() { return ManagementFactory.getGarbageCollectorMXBeans().stream().mapToLong(bean -> Math.max(0, bean.getCollectionTime())).sum(); }
  private static String telemetryJson() {
    if (SCENARIO.equals("F05")) {
      System.gc();
      try { Thread.sleep(25); } catch (InterruptedException interrupted) { Thread.currentThread().interrupt(); }
    }
    return "{\"runtime\":\"java\",\"active_tasks\":" + ACTIVE_TASKS.get() + ",\"open_resources\":" + OPEN_RESOURCES.get() +
        ",\"observed_max_in_flight\":" + MAX_ACTIVE.get() + ",\"gc_observed\":" + !FAULT.equals("gc_pause") +
        ",\"gc_collections\":" + (gcCollections() - INITIAL_GC_COLLECTIONS) + ",\"gc_time_ms\":" + (gcTimeMs() - INITIAL_GC_TIME_MS) + ",\"fault\":" + quote(FAULT) + "}";
  }

  static void send(HttpExchange exchange, int status, String value) throws IOException {
    byte[] data = value.getBytes(StandardCharsets.UTF_8);
    exchange.getResponseHeaders().set("content-type", "application/json");
    exchange.sendResponseHeaders(status, data.length);
    try (var out = exchange.getResponseBody()) { out.write(data); }
  }

  static void handle(HttpExchange exchange) throws IOException {
    try {
      String method = exchange.getRequestMethod();
      String path = exchange.getRequestURI().getPath();
      if (method.equals("GET") && path.equals("/health")) { send(exchange, 200, "{\"status\":\"ok\",\"runtime\":\"java\"}"); return; }
      if (method.equals("GET") && path.equals("/telemetry/snapshot")) { send(exchange, 200, telemetryJson()); return; }
      if (!method.equals("POST") || !path.equals("/fanout")) { send(exchange, 404, "{\"error\":\"not_found\"}"); return; }
      byte[] data = exchange.getRequestBody().readNBytes(1_048_577);
      Request request = data.length > 1_048_576 ? null : parse(new String(data, StandardCharsets.UTF_8));
      if (request == null) { send(exchange, 400, "{\"error\":\"invalid_request\"}"); return; }
      send(exchange, 200, run(request));
    } catch (Exception error) {
      send(exchange, 500, "{\"error\":\"internal\"}");
    }
  }

  public static void main(String[] args) throws IOException {
    int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8080"));
    String host = System.getenv().getOrDefault("HOST", "127.0.0.1");
    HttpServer server = HttpServer.create(new InetSocketAddress(host, port), 32);
    server.createContext("/", FanoutServer::handle);
    server.setExecutor(Executors.newVirtualThreadPerTaskExecutor());
    server.start();
  }
}
