package main

import (
	"context"
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"os"
	"regexp"
	"sort"
	"strconv"
	"sync"
	"sync/atomic"
	"time"
)

type Child struct {
	ChildID      string `json:"child_id"`
	Required     bool   `json:"required"`
	DelayMS      int    `json:"delay_ms"`
	PayloadBytes int    `json:"payload_bytes"`
	Mode         string `json:"mode,omitempty"`
}
type Request struct {
	RequestID        string  `json:"request_id"`
	DeadlineMS       int     `json:"deadline_ms"`
	ConcurrencyLimit int     `json:"concurrency_limit"`
	Children         []Child `json:"children"`
}
type ChildResult struct {
	ChildID   string  `json:"child_id"`
	Status    string  `json:"status"`
	ElapsedMS float64 `json:"elapsed_ms"`
}
type Cleanup struct {
	ActiveTasks   int `json:"active_tasks"`
	OpenResources int `json:"open_resources"`
}
type Response struct {
	RequestID   string        `json:"request_id"`
	Runtime     string        `json:"runtime"`
	Outcome     string        `json:"outcome"`
	Children    []ChildResult `json:"children"`
	ElapsedMS   float64       `json:"elapsed_ms"`
	MaxInFlight int           `json:"max_in_flight"`
	Cleanup     Cleanup       `json:"cleanup"`
}

var requestID = regexp.MustCompile(`^[A-Za-z0-9_-]{1,64}$`)
var childID = regexp.MustCompile(`^[a-z0-9-]{1,32}$`)
var fault = os.Getenv("COURSE_FAULT")
var globalActive atomic.Int64
var globalMax atomic.Int64
var sharedCounter int64
var sharedCounterMutex sync.Mutex

func validate(r Request) error {
	if !requestID.MatchString(r.RequestID) || r.DeadlineMS < 50 || r.DeadlineMS > 5000 || r.ConcurrencyLimit < 1 || r.ConcurrencyLimit > 64 || len(r.Children) < 1 || len(r.Children) > 16 {
		return errors.New("invalid_request")
	}
	ids := make(map[string]bool, len(r.Children))
	for _, c := range r.Children {
		if !childID.MatchString(c.ChildID) || ids[c.ChildID] || c.DelayMS < 0 || c.DelayMS > 10000 || c.PayloadBytes < 0 || c.PayloadBytes > 2097152 || (c.Mode != "" && c.Mode != "ok" && c.Mode != "error" && c.Mode != "invalid") {
			return errors.New("invalid_request")
		}
		ids[c.ChildID] = true
	}
	return nil
}

func enterTask() {
	value := globalActive.Add(1)
	for {
		prior := globalMax.Load()
		if value <= prior || globalMax.CompareAndSwap(prior, value) {
			break
		}
	}
}
func leaveTask() { globalActive.Add(-1) }

func incrementShared() {
	if fault == "data_race" {
		// The race-enabled harness observes this intentionally unsynchronized access.
		value := sharedCounter
		time.Sleep(time.Microsecond)
		sharedCounter = value + 1
		return
	}
	sharedCounterMutex.Lock()
	sharedCounter++
	sharedCounterMutex.Unlock()
}

func childWork(ctx context.Context, child Child) ChildResult {
	enterTask()
	defer leaveTask()
	begin := time.Now()
	incrementShared()
	status := "ok"
	delay := child.DelayMS
	if fault == "task_leak" {
		delay += 250
	}
	select {
	case <-time.After(time.Duration(delay) * time.Millisecond):
		if child.Mode != "" {
			status = child.Mode
		}
	case <-ctx.Done():
		status = "timeout"
	}
	return ChildResult{child.ChildID, status, float64(time.Since(begin).Microseconds()) / 1000}
}

func outcomeFor(r Request, rows []ChildResult) string {
	if len(rows) != len(r.Children) {
		return "failed"
	}
	required := make(map[string]bool, len(r.Children))
	for _, child := range r.Children {
		required[child.ChildID] = child.Required
	}
	outcome := "complete"
	for _, row := range rows {
		if row.Status != "ok" {
			if required[row.ChildID] {
				return "failed"
			}
			outcome = "partial"
		}
	}
	return outcome
}

func run(parent context.Context, r Request) Response {
	start := time.Now()
	contextOwner := parent
	if fault == "task_leak" {
		contextOwner = context.Background()
	}
	ctx, cancel := context.WithDeadline(contextOwner, start.Add(time.Duration(r.DeadlineMS)*time.Millisecond))
	if fault != "task_leak" {
		defer cancel()
	}
	limit := r.ConcurrencyLimit
	if limit > len(r.Children) {
		limit = len(r.Children)
	}
	sem := make(chan struct{}, limit)
	out := make(chan ChildResult, len(r.Children))
	var wg sync.WaitGroup
	localActive := atomic.Int64{}
	localMax := atomic.Int64{}

	for _, child := range r.Children {
		child := child
		select {
		case sem <- struct{}{}: // admission precedes goroutine creation
			wg.Add(1)
			go func() {
				defer wg.Done()
				defer func() { <-sem }()
				active := localActive.Add(1)
				for {
					prior := localMax.Load()
					if active <= prior || localMax.CompareAndSwap(prior, active) {
						break
					}
				}
				defer localActive.Add(-1)
				out <- childWork(ctx, child)
			}()
		case <-ctx.Done():
			out <- ChildResult{child.ChildID, "timeout", 0}
		}
	}

	if fault == "task_leak" {
		// The test-only variant returns while owned child tasks are still live.
		rows := make([]ChildResult, 0, len(r.Children))
		for len(out) > 0 {
			rows = append(rows, <-out)
		}
		return Response{r.RequestID, "go", "failed", rows, float64(time.Since(start).Microseconds()) / 1000, int(localMax.Load()), Cleanup{int(localActive.Load()), 0}}
	}

	wg.Wait()
	close(out)
	rows := make([]ChildResult, 0, len(r.Children))
	for row := range out {
		rows = append(rows, row)
	}
	sort.Slice(rows, func(i, j int) bool { return rows[i].ChildID < rows[j].ChildID })
	return Response{r.RequestID, "go", outcomeFor(r, rows), rows, float64(time.Since(start).Microseconds()) / 1000, int(localMax.Load()), Cleanup{int(localActive.Load()), 0}}
}

func write(w http.ResponseWriter, status int, value any) {
	w.Header().Set("content-type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(value)
}

func handler(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodGet && r.URL.Path == "/health" {
		write(w, 200, map[string]any{"status": "ok", "runtime": "go"})
		return
	}
	if r.Method == http.MethodGet && r.URL.Path == "/telemetry/snapshot" {
		write(w, 200, map[string]any{"runtime": "go", "active_tasks": globalActive.Load(), "open_resources": 0, "observed_max_in_flight": globalMax.Load(), "shared_counter": sharedCounter, "fault": fault})
		return
	}
	if r.Method != http.MethodPost || r.URL.Path != "/fanout" {
		write(w, 404, map[string]string{"error": "not_found"})
		return
	}
	r.Body = http.MaxBytesReader(w, r.Body, 1_048_576)
	defer r.Body.Close()
	var request Request
	decoder := json.NewDecoder(r.Body)
	decoder.DisallowUnknownFields()
	if decoder.Decode(&request) != nil || decoder.Decode(&struct{}{}) != io.EOF || validate(request) != nil {
		write(w, 400, map[string]string{"error": "invalid_request"})
		return
	}
	write(w, 200, run(r.Context(), request))
}

func main() {
	port := 8080
	if value := os.Getenv("PORT"); value != "" {
		if n, err := strconv.Atoi(value); err == nil {
			port = n
		}
	}
	host := os.Getenv("HOST")
	if host == "" {
		host = "127.0.0.1"
	}
	server := &http.Server{Addr: host + ":" + strconv.Itoa(port), Handler: http.HandlerFunc(handler), ReadHeaderTimeout: 2 * time.Second}
	_ = server.ListenAndServe()
}
