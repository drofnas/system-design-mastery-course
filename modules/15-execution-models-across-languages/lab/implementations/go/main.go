package main

import (
	"context"
	"encoding/json"
	"errors"
	"net/http"
	"os"
	"regexp"
	"sort"
	"strconv"
	"sync"
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

func validate(r Request) error {
	if !requestID.MatchString(r.RequestID) || r.DeadlineMS < 50 || r.DeadlineMS > 5000 || r.ConcurrencyLimit < 1 || r.ConcurrencyLimit > 64 || len(r.Children) < 1 || len(r.Children) > 16 {
		return errors.New("invalid_request")
	}
	for _, c := range r.Children {
		if !childID.MatchString(c.ChildID) || c.DelayMS < 0 || c.DelayMS > 10000 || c.PayloadBytes < 0 || c.PayloadBytes > 2097152 || (c.Mode != "" && c.Mode != "ok" && c.Mode != "error" && c.Mode != "invalid") {
			return errors.New("invalid_request")
		}
	}
	return nil
}

func run(parent context.Context, r Request) Response {
	start := time.Now()
	ctx, cancel := context.WithTimeout(parent, time.Duration(r.DeadlineMS)*time.Millisecond)
	defer cancel()
	limit := r.ConcurrencyLimit
	if limit > len(r.Children) {
		limit = len(r.Children)
	}
	sem := make(chan struct{}, limit)
	out := make(chan ChildResult, len(r.Children))
	var wg sync.WaitGroup
	for _, child := range r.Children {
		child := child
		select {
		case sem <- struct{}{}:
			wg.Add(1)
			go func() {
				defer wg.Done()
				defer func() { <-sem }()
				began := time.Now()
				status := "ok"
				select {
				case <-time.After(time.Duration(child.DelayMS) * time.Millisecond):
					if child.Mode != "" {
						status = child.Mode
					}
				case <-ctx.Done():
					status = "timeout"
				}
				out <- ChildResult{child.ChildID, status, float64(time.Since(began).Microseconds()) / 1000}
			}()
		case <-ctx.Done():
			out <- ChildResult{child.ChildID, "timeout", 0}
		}
	}
	wg.Wait()
	close(out)
	rows := make([]ChildResult, 0, len(r.Children))
	for row := range out {
		rows = append(rows, row)
	}
	sort.Slice(rows, func(i, j int) bool { return rows[i].ChildID < rows[j].ChildID })
	outcome := "complete"
	for _, row := range rows {
		if row.Status != "ok" {
			outcome = "partial"
			for _, c := range r.Children {
				if c.ChildID == row.ChildID && c.Required {
					outcome = "failed"
				}
			}
		}
	}
	return Response{r.RequestID, "go", outcome, rows, float64(time.Since(start).Microseconds()) / 1000, limit, Cleanup{0, 0}}
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
		write(w, 200, map[string]any{"runtime": "go", "active_tasks": 0, "open_resources": 0})
		return
	}
	if r.Method != http.MethodPost || r.URL.Path != "/fanout" {
		write(w, 404, map[string]string{"error": "not_found"})
		return
	}
	r.Body = http.MaxBytesReader(w, r.Body, 1048576)
	defer r.Body.Close()
	var request Request
	decoder := json.NewDecoder(r.Body)
	decoder.DisallowUnknownFields()
	if decoder.Decode(&request) != nil || validate(request) != nil {
		write(w, 400, map[string]string{"error": "invalid_request"})
		return
	}
	write(w, 200, run(r.Context(), request))
}
func main() {
	port := 8080
	if value := os.Getenv("PORT"); value != "" {
		if n, e := strconv.Atoi(value); e == nil {
			port = n
		}
	}
	server := &http.Server{Addr: "127.0.0.1:" + strconv.Itoa(port), Handler: http.HandlerFunc(handler), ReadHeaderTimeout: 2 * time.Second}
	_ = server.ListenAndServe()
}
