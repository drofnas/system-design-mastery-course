use axum::{extract::State,http::StatusCode,routing::{get,post},Json,Router};
use serde::{Deserialize,Serialize};
use serde_json::{json,Value};
use std::{sync::Arc,time::{Duration,Instant}};
use tokio::{sync::Semaphore,time::timeout};

#[derive(Clone)] struct AppState { runtime: &'static str }
#[derive(Clone,Deserialize)] #[serde(deny_unknown_fields)] struct Child { child_id:String, required:bool, delay_ms:u64, payload_bytes:u64, mode:Option<String> }
#[derive(Clone,Deserialize)] #[serde(deny_unknown_fields)] struct FanoutRequest { request_id:String, deadline_ms:u64, concurrency_limit:usize, children:Vec<Child> }
#[derive(Serialize)] struct ChildResult { child_id:String,status:String,elapsed_ms:f64 }
#[derive(Serialize)] struct Cleanup { active_tasks:u64,open_resources:u64 }
#[derive(Serialize)] struct FanoutResponse { request_id:String,runtime:&'static str,outcome:String,children:Vec<ChildResult>,elapsed_ms:f64,max_in_flight:usize,cleanup:Cleanup }

fn chars(value:&str,min:usize,max:usize,allowed:fn(char)->bool)->bool{(min..=max).contains(&value.len())&&value.chars().all(allowed)}
fn valid(r:&FanoutRequest)->bool{chars(&r.request_id,1,64,|c|c.is_ascii_alphanumeric()||c=='_'||c=='-')&&(50..=5000).contains(&r.deadline_ms)&&(1..=64).contains(&r.concurrency_limit)&&!r.children.is_empty()&&r.children.len()<=16&&r.children.iter().all(|c|chars(&c.child_id,1,32,|v|v.is_ascii_lowercase()||v.is_ascii_digit()||v=='-')&&c.delay_ms<=10000&&c.payload_bytes<=2097152&&matches!(c.mode.as_deref(),None|Some("ok")|Some("error")|Some("invalid")))}
async fn health(State(s):State<AppState>)->Json<Value>{Json(json!({"status":"ok","runtime":s.runtime}))}
async fn telemetry()->Json<Value>{Json(json!({"runtime":"rust","active_tasks":0,"open_resources":0}))}
async fn fanout(State(_):State<AppState>,Json(req):Json<FanoutRequest>)->Result<Json<FanoutResponse>,(StatusCode,Json<Value>)>{
 if !valid(&req){return Err((StatusCode::BAD_REQUEST,Json(json!({"error":"invalid_request"}))))}
 let started=Instant::now();let deadline_at=started+Duration::from_millis(req.deadline_ms);let max=req.concurrency_limit.min(req.children.len());let sem=Arc::new(Semaphore::new(max));let mut joins=Vec::new();
 for child in req.children.clone(){let sem=sem.clone();joins.push(tokio::spawn(async move{let _permit=sem.acquire_owned().await.expect("semaphore open");let began=Instant::now();let remaining=deadline_at.saturating_duration_since(began);let status=if remaining.is_zero(){"timeout".into()}else{match timeout(remaining,tokio::time::sleep(Duration::from_millis(child.delay_ms))).await{Ok(_)=>child.mode.unwrap_or_else(||"ok".into()),Err(_)=>"timeout".into()}};ChildResult{child_id:child.child_id,status,elapsed_ms:began.elapsed().as_secs_f64()*1000.0}}));}
 let mut rows=Vec::new();for join in joins{rows.push(join.await.map_err(|_|(StatusCode::INTERNAL_SERVER_ERROR,Json(json!({"error":"task_failure"}))))?)}rows.sort_by(|a,b|a.child_id.cmp(&b.child_id));let mut outcome="complete";for row in &rows{if row.status!="ok"{outcome="partial";if req.children.iter().any(|c|c.child_id==row.child_id&&c.required){outcome="failed"}}}
 Ok(Json(FanoutResponse{request_id:req.request_id,runtime:"rust",outcome:outcome.into(),children:rows,elapsed_ms:started.elapsed().as_secs_f64()*1000.0,max_in_flight:max,cleanup:Cleanup{active_tasks:0,open_resources:0}}))
}
#[tokio::main] async fn main(){let state=AppState{runtime:"rust"};let app=Router::new().route("/health",get(health)).route("/telemetry/snapshot",get(telemetry)).route("/fanout",post(fanout)).with_state(state);let port=std::env::var("PORT").ok().and_then(|v|v.parse().ok()).unwrap_or(8080);let listener=tokio::net::TcpListener::bind(("127.0.0.1",port)).await.unwrap();axum::serve(listener,app).await.unwrap();}

#[cfg(test)] mod tests{use super::*;#[test]fn rejects_empty(){assert!(!valid(&FanoutRequest{request_id:"x".into(),deadline_ms:500,concurrency_limit:4,children:vec![]}));}#[test]fn rejects_invalid_mode(){assert!(!valid(&FanoutRequest{request_id:"x".into(),deadline_ms:500,concurrency_limit:1,children:vec![Child{child_id:"a".into(),required:true,delay_ms:1,payload_bytes:0,mode:Some("invented".into())}]}));}#[tokio::test]async fn deadline_does_not_restart_for_queued_work(){let req=FanoutRequest{request_id:"r2".into(),deadline_ms:50,concurrency_limit:1,children:vec![Child{child_id:"a".into(),required:true,delay_ms:40,payload_bytes:0,mode:None},Child{child_id:"b".into(),required:true,delay_ms:40,payload_bytes:0,mode:None}]};let Json(response)=fanout(State(AppState{runtime:"rust"}),Json(req)).await.unwrap();assert_eq!(response.children.iter().find(|c|c.child_id=="b").unwrap().status,"timeout");assert_eq!(response.cleanup.active_tasks,0);}}
