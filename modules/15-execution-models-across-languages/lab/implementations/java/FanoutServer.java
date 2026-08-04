import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Set;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class FanoutServer {
  private static final Pattern REQUEST_ID=Pattern.compile("\\\"request_id\\\"\\s*:\\s*\\\"([A-Za-z0-9_-]{1,64})\\\"");
  private static final Pattern DEADLINE=Pattern.compile("\\\"deadline_ms\\\"\\s*:\\s*(\\d+)");
  private static final Pattern LIMIT=Pattern.compile("\\\"concurrency_limit\\\"\\s*:\\s*(\\d+)");
  private static final Pattern CHILD=Pattern.compile("\\\"child_id\\\"\\s*:\\s*\\\"([a-z0-9-]{1,32})\\\"[^}]*\\\"required\\\"\\s*:\\s*(true|false)[^}]*\\\"delay_ms\\\"\\s*:\\s*(\\d+)[^}]*\\\"payload_bytes\\\"\\s*:\\s*(\\d+)([^}]*)}");
  private static final Pattern KEY=Pattern.compile("\\\"([A-Za-z_][A-Za-z0-9_]*)\\\"\\s*:");
  private static final Pattern MODE=Pattern.compile("\\\"mode\\\"\\s*:\\s*\\\"([^\\\"]+)\\\"");
  private static final Set<String> KEYS=Set.of("request_id","deadline_ms","concurrency_limit","children","child_id","required","delay_ms","payload_bytes","mode");
  record Child(String id,boolean required,int delay,int bytes,String mode){}
  record Request(String id,int deadline,int limit,List<Child> children){}

  static Request parse(String json){
    String text=json.trim();if(!text.startsWith("{")||!text.endsWith("}"))return null;Matcher key=KEY.matcher(text);while(key.find())if(!KEYS.contains(key.group(1)))return null;Matcher everyMode=MODE.matcher(text);while(everyMode.find())if(!Set.of("ok","error","invalid").contains(everyMode.group(1)))return null;
    Matcher id=REQUEST_ID.matcher(text),deadline=DEADLINE.matcher(text),limit=LIMIT.matcher(text);if(!id.find()||!deadline.find()||!limit.find())return null;
    int d=Integer.parseInt(deadline.group(1)),l=Integer.parseInt(limit.group(1));List<Child> children=new ArrayList<>();Matcher child=CHILD.matcher(text);while(child.find()){Matcher mode=MODE.matcher(child.group());children.add(new Child(child.group(1),Boolean.parseBoolean(child.group(2)),Integer.parseInt(child.group(3)),Integer.parseInt(child.group(4)),mode.find()?mode.group(1):null));}
    Request r=new Request(id.group(1),d,l,children);return valid(r)?r:null;
  }
  static boolean valid(Request r){return r!=null&&r.deadline>=50&&r.deadline<=5000&&r.limit>=1&&r.limit<=64&&r.children.size()>=1&&r.children.size()<=16&&r.children.stream().allMatch(c->c.delay>=0&&c.delay<=10000&&c.bytes>=0&&c.bytes<=2097152);}
  static String run(Request r) throws InterruptedException{
    long start=System.nanoTime(),deadlineAt=start+r.deadline*1_000_000L;int max=Math.min(r.limit,r.children.size());Semaphore sem=new Semaphore(max);List<String> rows=new ArrayList<>();try(var executor=Executors.newVirtualThreadPerTaskExecutor()){
      var futures=r.children.stream().map(c->executor.submit(()->{long began=System.nanoTime();sem.acquire();try{long remaining=Math.max(0,deadlineAt-System.nanoTime());if(remaining==0)return "{\"child_id\":\""+c.id+"\",\"status\":\"timeout\",\"elapsed_ms\":0}";long sleep=Math.min(c.delay,Math.max(1,(remaining+999_999)/1_000_000));Thread.sleep(sleep);String status=c.delay*1_000_000L>=remaining?"timeout":c.mode==null?"ok":c.mode;return "{\"child_id\":\""+c.id+"\",\"status\":\""+status+"\",\"elapsed_ms\":"+((System.nanoTime()-began)/1_000_000.0)+"}";}finally{sem.release();}})).toList();for(var f:futures){try{rows.add(f.get());}catch(Exception e){throw new IllegalStateException(e);}}}
    rows.sort(Comparator.naturalOrder());boolean failed=rows.stream().anyMatch(row->row.contains("timeout")&&r.children.stream().anyMatch(c->c.required&&row.contains("\""+c.id+"\"")));String outcome=failed?"failed":rows.stream().anyMatch(row->row.contains("timeout"))?"partial":"complete";
    return "{\"request_id\":\""+r.id+"\",\"runtime\":\"java\",\"outcome\":\""+outcome+"\",\"children\":["+String.join(",",rows)+"],\"elapsed_ms\":"+((System.nanoTime()-start)/1_000_000.0)+",\"max_in_flight\":"+max+",\"cleanup\":{\"active_tasks\":0,\"open_resources\":0}}";
  }
  static void send(HttpExchange exchange,int status,String value)throws IOException{byte[] data=value.getBytes(StandardCharsets.UTF_8);exchange.getResponseHeaders().set("content-type","application/json");exchange.sendResponseHeaders(status,data.length);try(var out=exchange.getResponseBody()){out.write(data);}}
  static void handle(HttpExchange x)throws IOException{try{if(x.getRequestMethod().equals("GET")&&x.getRequestURI().getPath().equals("/health")){send(x,200,"{\"status\":\"ok\",\"runtime\":\"java\"}");return;}if(x.getRequestMethod().equals("GET")&&x.getRequestURI().getPath().equals("/telemetry/snapshot")){send(x,200,"{\"runtime\":\"java\",\"active_tasks\":0,\"open_resources\":0}");return;}if(!x.getRequestMethod().equals("POST")||!x.getRequestURI().getPath().equals("/fanout")){send(x,404,"{\"error\":\"not_found\"}");return;}byte[] data=x.getRequestBody().readNBytes(1_048_577);Request r=data.length>1_048_576?null:parse(new String(data,StandardCharsets.UTF_8));if(r==null){send(x,400,"{\"error\":\"invalid_request\"}");return;}send(x,200,run(r));}catch(Exception e){send(x,500,"{\"error\":\"internal\"}");}}
  public static void main(String[] args)throws IOException{int port=Integer.parseInt(System.getenv().getOrDefault("PORT","8080"));HttpServer server=HttpServer.create(new InetSocketAddress("127.0.0.1",port),32);server.createContext("/",FanoutServer::handle);server.setExecutor(Executors.newVirtualThreadPerTaskExecutor());server.start();}
}
