package main

import (
	"context"
	"testing"
)

func TestValidation(t *testing.T) {
	if validate(Request{RequestID: "x", DeadlineMS: 500, ConcurrencyLimit: 4, Children: nil}) == nil {
		t.Fatal("empty children accepted")
	}
}
func TestValidationRejectsInvalidMode(t *testing.T) {
	if validate(Request{RequestID: "x", DeadlineMS: 500, ConcurrencyLimit: 1, Children: []Child{{ChildID: "a", Mode: "invented"}}}) == nil {
		t.Fatal("invalid mode accepted")
	}
}
func TestFanout(t *testing.T) {
	r := run(context.Background(), Request{RequestID: "r1", DeadlineMS: 100, ConcurrencyLimit: 2, Children: []Child{{ChildID: "b", DelayMS: 1}, {ChildID: "a", Required: true, DelayMS: 1}}})
	if r.Outcome != "complete" || r.Children[0].ChildID != "a" || r.Cleanup.ActiveTasks != 0 {
		t.Fatalf("bad result: %#v", r)
	}
}
func TestDeadlineDoesNotRestartForQueuedWork(t *testing.T) {
	r := run(context.Background(), Request{RequestID: "r2", DeadlineMS: 50, ConcurrencyLimit: 1, Children: []Child{{ChildID: "a", Required: true, DelayMS: 40}, {ChildID: "b", Required: true, DelayMS: 40}}})
	if r.Children[1].Status != "timeout" || r.Cleanup.ActiveTasks != 0 {
		t.Fatalf("deadline or cleanup failed: %#v", r)
	}
}
