//! Compile-fail teaching fixture: `Rc<RefCell<_>>` cannot cross a thread.
//! Run with `rustc` after uncommenting the body; preserve compiler output.
// use std::{cell::RefCell, rc::Rc};
// fn main() { let value=Rc::new(RefCell::new(0)); std::thread::spawn(move || *value.borrow_mut()+=1); }
#[test] fn fixture_is_documented(){assert!(include_str!("send_sync_compile_fail.rs").contains("Rc<RefCell"));}
