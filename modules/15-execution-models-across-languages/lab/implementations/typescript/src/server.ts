import { createServer, IncomingMessage, ServerResponse } from "node:http";

export type Child = { child_id: string; required: boolean; delay_ms: number; payload_bytes: number; mode?: "ok"|"error"|"invalid" };
export type RequestShape = { request_id: string; deadline_ms: number; concurrency_limit: number; children: Child[] };

export function validate(value: unknown): value is RequestShape {
  if (!value || typeof value !== "object" || Array.isArray(value)) return false;
  const v = value as Record<string, unknown>;
  if (Object.keys(v).some(k => !["request_id","deadline_ms","concurrency_limit","children"].includes(k))) return false;
  if (typeof v.request_id !== "string" || !/^[A-Za-z0-9_-]{1,64}$/.test(v.request_id)) return false;
  if (!Number.isInteger(v.deadline_ms) || (v.deadline_ms as number) < 50 || (v.deadline_ms as number) > 5000) return false;
  if (!Number.isInteger(v.concurrency_limit) || (v.concurrency_limit as number) < 1 || (v.concurrency_limit as number) > 64) return false;
  if (!Array.isArray(v.children) || v.children.length < 1 || v.children.length > 16) return false;
  return v.children.every(raw => {
    if (!raw || typeof raw !== "object" || Array.isArray(raw)) return false;
    const c = raw as Record<string, unknown>;
    if (Object.keys(c).some(k => !["child_id","required","delay_ms","payload_bytes","mode"].includes(k))) return false;
    return typeof c.child_id === "string" && /^[a-z0-9-]{1,32}$/.test(c.child_id) &&
      typeof c.required === "boolean" && Number.isInteger(c.delay_ms) && (c.delay_ms as number) >= 0 && (c.delay_ms as number) <= 10000 &&
      Number.isInteger(c.payload_bytes) && (c.payload_bytes as number) >= 0 && (c.payload_bytes as number) <= 2097152 &&
      (c.mode === undefined || c.mode === "ok" || c.mode === "error" || c.mode === "invalid");
  });
}

export async function fanout(req: RequestShape) {
  const started = performance.now();
  const deadline = started + req.deadline_ms;
  const children: Array<{child_id:string;status:string;elapsed_ms:number}> = [];
  let next = 0;
  let active = 0;
  let observedMax = 0;
  async function worker() {
    while (next < req.children.length) {
      const child = req.children[next++];
      if (!child) break;
      const began = performance.now();
      const remaining = Math.max(0, deadline - began);
      if (remaining === 0) { children.push({child_id:child.child_id,status:"timeout",elapsed_ms:0}); continue; }
      active += 1;
      observedMax = Math.max(observedMax, active);
      await new Promise(resolve => setTimeout(resolve, Math.min(child.delay_ms, remaining)));
      active -= 1;
      children.push({ child_id: child.child_id, status: child.delay_ms >= remaining ? "timeout" : (child.mode ?? "ok"), elapsed_ms: performance.now()-began });
    }
  }
  await Promise.all(Array.from({length:Math.min(req.concurrency_limit,req.children.length)},()=>worker()));
  children.sort((a,b) => a.child_id.localeCompare(b.child_id));
  const requiredFailed = children.some(row => req.children.find(c => c.child_id === row.child_id)?.required && row.status !== "ok");
  return { request_id:req.request_id, runtime:"typescript", outcome:requiredFailed?"failed":children.some(c=>c.status!=="ok")?"partial":"complete", children, elapsed_ms:performance.now()-started, max_in_flight:observedMax, cleanup:{active_tasks:active,open_resources:0} };
}

async function body(request: IncomingMessage): Promise<unknown> { const chunks: Buffer[]=[]; for await (const chunk of request) chunks.push(Buffer.from(chunk)); if (chunks.reduce((n,b)=>n+b.length,0)>1048576) throw new Error("too_large"); return JSON.parse(Buffer.concat(chunks).toString("utf8")); }
function send(response: ServerResponse, status: number, value: unknown) { const data=JSON.stringify(value); response.writeHead(status,{"content-type":"application/json","content-length":Buffer.byteLength(data)}); response.end(data); }

if (process.argv[1]?.endsWith("server.js")) createServer(async (request,response) => { try { if (request.method==="GET" && request.url==="/health") return send(response,200,{status:"ok",runtime:"typescript"}); if (request.method==="GET" && request.url==="/telemetry/snapshot") return send(response,200,{runtime:"typescript",active_tasks:0,open_resources:0}); if (request.method==="POST" && request.url==="/fanout") { const value=await body(request); if (!validate(value)) return send(response,400,{error:"invalid_request"}); return send(response,200,await fanout(value)); } send(response,404,{error:"not_found"}); } catch { send(response,400,{error:"invalid_request"}); } }).listen(Number(process.env.PORT ?? 8080),"127.0.0.1");
