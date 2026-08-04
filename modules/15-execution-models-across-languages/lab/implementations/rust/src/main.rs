use axum::{body::Bytes, extract::{DefaultBodyLimit, State}, http::StatusCode, routing::{get, post}, Json, Router};
use serde::{Deserialize, Serialize};
use serde_json::{json, Value};
use std::{collections::{HashSet, VecDeque}, sync::{atomic::{AtomicUsize, Ordering}, Arc}, time::{Duration, Instant}};
use tokio::{sync::Mutex, task::JoinSet, time::timeout};

#[derive(Clone)]
struct AppState {
    fault: Arc<String>,
    active_tasks: Arc<AtomicUsize>,
    max_active: Arc<AtomicUsize>,
    open_resources: Arc<AtomicUsize>,
    buffered_bytes: Arc<AtomicUsize>,
    peak_buffered_bytes: Arc<AtomicUsize>,
    cancel_after_ms: Option<u64>,
}

#[derive(Clone, Deserialize)]
#[serde(deny_unknown_fields)]
struct Child { child_id: String, required: bool, delay_ms: u64, payload_bytes: u64, mode: Option<String> }
#[derive(Clone, Deserialize)]
#[serde(deny_unknown_fields)]
struct FanoutRequest { request_id: String, deadline_ms: u64, concurrency_limit: usize, children: Vec<Child> }
#[derive(Serialize)]
struct ChildResult { child_id: String, status: String, elapsed_ms: f64 }
#[derive(Serialize)]
struct Cleanup { active_tasks: usize, open_resources: usize }
#[derive(Serialize)]
struct FanoutResponse { request_id: String, runtime: &'static str, outcome: String, children: Vec<ChildResult>, elapsed_ms: f64, max_in_flight: usize, cleanup: Cleanup }

struct TaskGuard { state: AppState, bytes: usize }
impl TaskGuard {
    fn enter(state: &AppState, bytes: usize) -> Self {
        let active = state.active_tasks.fetch_add(1, Ordering::SeqCst) + 1;
        state.max_active.fetch_max(active, Ordering::SeqCst);
        state.open_resources.fetch_add(1, Ordering::SeqCst);
        let buffered = state.buffered_bytes.fetch_add(bytes, Ordering::SeqCst) + bytes;
        state.peak_buffered_bytes.fetch_max(buffered, Ordering::SeqCst);
        Self { state: state.clone(), bytes }
    }
}
impl Drop for TaskGuard {
    fn drop(&mut self) {
        self.state.active_tasks.fetch_sub(1, Ordering::SeqCst);
        self.state.open_resources.fetch_sub(1, Ordering::SeqCst);
        self.state.buffered_bytes.fetch_sub(self.bytes, Ordering::SeqCst);
    }
}

fn chars(value: &str, min: usize, max: usize, allowed: fn(char) -> bool) -> bool {
    (min..=max).contains(&value.len()) && value.chars().all(allowed)
}
fn valid(request: &FanoutRequest) -> bool {
    let mut ids = HashSet::new();
    chars(&request.request_id, 1, 64, |c| c.is_ascii_alphanumeric() || c == '_' || c == '-') &&
        (50..=5000).contains(&request.deadline_ms) &&
        (1..=64).contains(&request.concurrency_limit) &&
        !request.children.is_empty() && request.children.len() <= 16 &&
        request.children.iter().all(|child| {
            chars(&child.child_id, 1, 32, |v| v.is_ascii_lowercase() || v.is_ascii_digit() || v == '-') &&
                ids.insert(child.child_id.clone()) && child.delay_ms <= 10000 && child.payload_bytes <= 2_097_152 &&
                matches!(child.mode.as_deref(), None | Some("ok") | Some("error") | Some("invalid"))
        })
}

async fn health() -> Json<Value> { Json(json!({"status":"ok","runtime":"rust"})) }
async fn telemetry(State(state): State<AppState>) -> Json<Value> {
    Json(json!({
        "runtime":"rust",
        "active_tasks":state.active_tasks.load(Ordering::SeqCst),
        "open_resources":state.open_resources.load(Ordering::SeqCst),
        "observed_max_in_flight":state.max_active.load(Ordering::SeqCst),
        "buffered_bytes":state.buffered_bytes.load(Ordering::SeqCst),
        "peak_buffered_bytes":state.peak_buffered_bytes.load(Ordering::SeqCst),
        "fault":state.fault.as_str()
    }))
}

async fn child_work(state: AppState, child: Child, deadline_at: Instant) -> ChildResult {
    let began = Instant::now();
    let multiplier = if state.fault.as_str() == "allocation_pressure" { 4 } else { 1 };
    let allocation = vec![0_u8; child.payload_bytes as usize * multiplier];
    let _guard = TaskGuard::enter(&state, allocation.len());
    let remaining = deadline_at.saturating_duration_since(began);
    let status = if remaining.is_zero() {
        "timeout".into()
    } else {
        let delay_ms = if state.fault.as_str() == "missing_cancellation" { child.delay_ms + 500 } else { child.delay_ms };
        match timeout(remaining, tokio::time::sleep(Duration::from_millis(delay_ms))).await {
            Ok(_) => child.mode.unwrap_or_else(|| "ok".into()),
            Err(_) => "timeout".into(),
        }
    };
    drop(allocation);
    ChildResult { child_id: child.child_id, status, elapsed_ms: began.elapsed().as_secs_f64() * 1000.0 }
}

async fn fanout(State(state): State<AppState>, body: Bytes) -> Result<Json<FanoutResponse>, (StatusCode, Json<Value>)> {
    let request: FanoutRequest = serde_json::from_slice(&body)
        .map_err(|_| (StatusCode::BAD_REQUEST, Json(json!({"error":"invalid_request"}))))?;
    if !valid(&request) {
        return Err((StatusCode::BAD_REQUEST, Json(json!({"error":"invalid_request"}))));
    }
    let started = Instant::now();
    let deadline_at = started + Duration::from_millis(request.deadline_ms);
    let worker_count = request.concurrency_limit.min(request.children.len());
    let queue = Arc::new(Mutex::new(VecDeque::from(request.children.clone())));
    let local_active = Arc::new(AtomicUsize::new(0));
    let local_max = Arc::new(AtomicUsize::new(0));
    let mut joins = JoinSet::new();

    for _ in 0..worker_count {
        let queue = queue.clone();
        let state = state.clone();
        let local_active = local_active.clone();
        let local_max = local_max.clone();
        joins.spawn(async move {
            let mut rows = Vec::new();
            loop {
                let child = queue.lock().await.pop_front();
                let Some(child) = child else { break };
                let active = local_active.fetch_add(1, Ordering::SeqCst) + 1;
                local_max.fetch_max(active, Ordering::SeqCst);
                rows.push(child_work(state.clone(), child, deadline_at).await);
                local_active.fetch_sub(1, Ordering::SeqCst);
            }
            rows
        });
    }

    if state.fault.as_str() == "missing_cancellation" {
        joins.detach_all();
        return Ok(Json(FanoutResponse {
            request_id: request.request_id,
            runtime: "rust",
            outcome: "failed".into(),
            children: Vec::new(),
            elapsed_ms: started.elapsed().as_secs_f64() * 1000.0,
            max_in_flight: local_max.load(Ordering::SeqCst),
            cleanup: Cleanup { active_tasks: state.active_tasks.load(Ordering::SeqCst), open_resources: state.open_resources.load(Ordering::SeqCst) },
        }));
    }

    let collect = async {
        let mut rows = Vec::new();
        while let Some(result) = joins.join_next().await {
            rows.extend(result.map_err(|_| (StatusCode::INTERNAL_SERVER_ERROR, Json(json!({"error":"task_failure"}))))?);
        }
        Ok::<Vec<ChildResult>, (StatusCode, Json<Value>)>(rows)
    };
    let mut rows = if let Some(milliseconds) = state.cancel_after_ms {
        match timeout(Duration::from_millis(milliseconds), collect).await {
            Ok(result) => result?,
            Err(_) => {
                joins.abort_all();
                while joins.join_next().await.is_some() {}
                Vec::new()
            }
        }
    } else {
        collect.await?
    };
    rows.sort_by(|a, b| a.child_id.cmp(&b.child_id));
    let required: std::collections::HashMap<String, bool> = request.children.iter().map(|child| (child.child_id.clone(), child.required)).collect();
    let required_failed = rows.len() != request.children.len() || rows.iter().any(|row| required.get(&row.child_id).copied().unwrap_or(true) && row.status != "ok");
    let optional_failed = rows.iter().any(|row| row.status != "ok");
    Ok(Json(FanoutResponse {
        request_id: request.request_id,
        runtime: "rust",
        outcome: if required_failed { "failed" } else if optional_failed { "partial" } else { "complete" }.into(),
        children: rows,
        elapsed_ms: started.elapsed().as_secs_f64() * 1000.0,
        max_in_flight: local_max.load(Ordering::SeqCst),
        cleanup: Cleanup { active_tasks: local_active.load(Ordering::SeqCst), open_resources: 0 },
    }))
}

#[tokio::main]
async fn main() {
    let state = AppState {
        fault: Arc::new(std::env::var("COURSE_FAULT").unwrap_or_else(|_| "none".into())),
        active_tasks: Arc::new(AtomicUsize::new(0)),
        max_active: Arc::new(AtomicUsize::new(0)),
        open_resources: Arc::new(AtomicUsize::new(0)),
        buffered_bytes: Arc::new(AtomicUsize::new(0)),
        peak_buffered_bytes: Arc::new(AtomicUsize::new(0)),
        cancel_after_ms: std::env::var("COURSE_CANCEL_AFTER_MS").ok().and_then(|value| value.parse().ok()),
    };
    let app = Router::new().route("/health", get(health)).route("/telemetry/snapshot", get(telemetry)).route("/fanout", post(fanout)).layer(DefaultBodyLimit::max(1_048_576)).with_state(state);
    let port = std::env::var("PORT").ok().and_then(|value| value.parse().ok()).unwrap_or(8080);
    let host = std::env::var("HOST").unwrap_or_else(|_| "127.0.0.1".into());
    let listener = tokio::net::TcpListener::bind(format!("{host}:{port}")).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    fn request(children: Vec<Child>) -> FanoutRequest { FanoutRequest { request_id: "x".into(), deadline_ms: 500, concurrency_limit: 4, children } }
    #[test] fn rejects_empty() { assert!(!valid(&request(Vec::new()))); }
    #[test] fn rejects_duplicate_ids() { let child = Child { child_id:"a".into(), required:true, delay_ms:1, payload_bytes:0, mode:None }; assert!(!valid(&request(vec![child.clone(), child]))); }
    #[test] fn rejects_invalid_mode() { assert!(!valid(&request(vec![Child { child_id:"a".into(), required:true, delay_ms:1, payload_bytes:0, mode:Some("invented".into()) }]))); }
}
