import { createServer, IncomingMessage, ServerResponse } from "node:http";

export type Child = {
  child_id: string;
  required: boolean;
  delay_ms: number;
  payload_bytes: number;
  mode?: "ok" | "error" | "invalid";
};
export type RequestShape = {
  request_id: string;
  deadline_ms: number;
  concurrency_limit: number;
  children: Child[];
};
type ChildResult = { child_id: string; status: string; elapsed_ms: number };

const fault = process.env.COURSE_FAULT ?? "none";
let activeTasks = 0;
let observedMax = 0;

export function validate(value: unknown): value is RequestShape {
  if (!value || typeof value !== "object" || Array.isArray(value)) return false;
  const v = value as Record<string, unknown>;
  const requestKeys = ["request_id", "deadline_ms", "concurrency_limit", "children"];
  if (Object.keys(v).some((key) => !requestKeys.includes(key))) return false;
  if (typeof v.request_id !== "string" || !/^[A-Za-z0-9_-]{1,64}$/.test(v.request_id)) return false;
  if (!Number.isInteger(v.deadline_ms) || (v.deadline_ms as number) < 50 || (v.deadline_ms as number) > 5000) return false;
  if (!Number.isInteger(v.concurrency_limit) || (v.concurrency_limit as number) < 1 || (v.concurrency_limit as number) > 64) return false;
  if (!Array.isArray(v.children) || v.children.length < 1 || v.children.length > 16) return false;
  const ids = new Set<string>();
  return v.children.every((raw) => {
    if (!raw || typeof raw !== "object" || Array.isArray(raw)) return false;
    const c = raw as Record<string, unknown>;
    const childKeys = ["child_id", "required", "delay_ms", "payload_bytes", "mode"];
    if (Object.keys(c).some((key) => !childKeys.includes(key))) return false;
    if (typeof c.child_id !== "string" || !/^[a-z0-9-]{1,32}$/.test(c.child_id) || ids.has(c.child_id)) return false;
    ids.add(c.child_id);
    return typeof c.required === "boolean" &&
      Number.isInteger(c.delay_ms) && (c.delay_ms as number) >= 0 && (c.delay_ms as number) <= 10000 &&
      Number.isInteger(c.payload_bytes) && (c.payload_bytes as number) >= 0 && (c.payload_bytes as number) <= 2097152 &&
      (c.mode === undefined || c.mode === "ok" || c.mode === "error" || c.mode === "invalid");
  });
}

function sleep(milliseconds: number, signal?: AbortSignal): Promise<boolean> {
  return new Promise((resolve) => {
    if (signal?.aborted) return resolve(false);
    const timer = setTimeout(() => { cleanup(); resolve(true); }, milliseconds);
    const cancel = () => { clearTimeout(timer); cleanup(); resolve(false); };
    const cleanup = () => signal?.removeEventListener("abort", cancel);
    signal?.addEventListener("abort", cancel, { once: true });
  });
}

export async function fanout(req: RequestShape, signal?: AbortSignal) {
  const started = performance.now();
  const deadline = started + req.deadline_ms;
  const children: ChildResult[] = [];
  let next = 0;
  let localActive = 0;
  let localMax = 0;

  if (fault === "event_loop_block") {
    const until = performance.now() + req.deadline_ms + 25;
    while (performance.now() < until) { /* test-only event-loop starvation */ }
  }

  async function worker() {
    while (next < req.children.length && !signal?.aborted) {
      const child = req.children[next++];
      if (!child) break;
      const began = performance.now();
      const remaining = Math.max(0, deadline - began);
      if (remaining === 0) {
        children.push({ child_id: child.child_id, status: "timeout", elapsed_ms: 0 });
        continue;
      }
      localActive += 1;
      activeTasks += 1;
      localMax = Math.max(localMax, localActive);
      observedMax = Math.max(observedMax, activeTasks);
      const completed = await sleep(Math.min(child.delay_ms, remaining), signal);
      localActive -= 1;
      activeTasks -= 1;
      const status = !completed ? "cancelled" : child.delay_ms >= remaining ? "timeout" : (child.mode ?? "ok");
      children.push({ child_id: child.child_id, status, elapsed_ms: performance.now() - began });
    }
  }

  // At most concurrency_limit workers exist; a child is selected only by an admitted worker.
  const workerCount = Math.min(req.concurrency_limit, req.children.length);
  await Promise.all(Array.from({ length: workerCount }, () => worker()));
  for (; next < req.children.length; next += 1) {
    const child = req.children[next];
    if (child) children.push({ child_id: child.child_id, status: "cancelled", elapsed_ms: 0 });
  }
  children.sort((a, b) => a.child_id.localeCompare(b.child_id));
  const byId = new Map(req.children.map((child) => [child.child_id, child]));
  const requiredFailed = children.some((row) => byId.get(row.child_id)?.required && row.status !== "ok") || children.length !== req.children.length;
  const optionalFailed = children.some((row) => row.status !== "ok");
  return {
    request_id: req.request_id,
    runtime: "typescript",
    outcome: requiredFailed ? "failed" : optionalFailed ? "partial" : "complete",
    children,
    elapsed_ms: performance.now() - started,
    max_in_flight: localMax,
    cleanup: { active_tasks: localActive, open_resources: 0 },
  };
}

async function body(request: IncomingMessage): Promise<unknown> {
  const chunks: Buffer[] = [];
  let size = 0;
  for await (const chunk of request) {
    const value = Buffer.from(chunk);
    size += value.length;
    if (size > 1_048_576) throw new Error("too_large");
    chunks.push(value);
  }
  return JSON.parse(Buffer.concat(chunks).toString("utf8"));
}

function send(response: ServerResponse, status: number, value: unknown) {
  if (response.destroyed || response.headersSent) return;
  const data = JSON.stringify(value);
  response.writeHead(status, { "content-type": "application/json", "content-length": Buffer.byteLength(data) });
  response.end(data);
}

if (process.argv[1]?.endsWith("server.js")) {
  createServer(async (request, response) => {
    const controller = new AbortController();
    request.once("aborted", () => controller.abort());
    response.once("close", () => { if (!response.writableEnded) controller.abort(); });
    try {
      if (request.method === "GET" && request.url === "/health") return send(response, 200, { status: "ok", runtime: "typescript" });
      if (request.method === "GET" && request.url === "/telemetry/snapshot") {
        return send(response, 200, { runtime: "typescript", active_tasks: activeTasks, open_resources: 0, observed_max_in_flight: observedMax, fault });
      }
      if (request.method === "POST" && request.url === "/fanout") {
        const value = await body(request);
        if (fault !== "invalid_json" && !validate(value)) return send(response, 400, { error: "invalid_request" });
        if (!value || typeof value !== "object") return send(response, 400, { error: "invalid_request" });
        return send(response, 200, await fanout(value as RequestShape, controller.signal));
      }
      send(response, 404, { error: "not_found" });
    } catch {
      send(response, 400, { error: "invalid_request" });
    }
  }).listen(Number(process.env.PORT ?? 8080), process.env.HOST ?? "127.0.0.1");
}
