import http from 'node:http';
import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import React from 'react';
import {renderToPipeableStream, renderToStaticMarkup, renderToString} from 'react-dom/server';
import {EventDetail, Layout, LiveShell, SkyEvents, StaffIsland, events} from './app.js';

const edgePort = Number(process.env.NORTHSTAR_PORT || 4180);
const originPort = edgePort + 1;
const cache = new Map();
const counters = {edgeRequests: 0, originRequests: 0, cacheHits: 0, cacheMisses: 0, privateBypasses: 0, rejectedTraceparents: 0};
const clientBundle = await readFile(fileURLToPath(new URL('../dist/client.js', import.meta.url)));
const validTraceparent = /^00-[0-9a-f]{32}-[0-9a-f]{16}-0[01]$/;

function cleanRegion(value) {
  return value === 'south' ? 'south' : 'north';
}

function aliasFromCookie(cookie = '') {
  const match = /(?:^|;\s*)northstar_alias=([a-z0-9-]{1,24})/.exec(cookie.toLowerCase());
  return match?.[1] || 'observer';
}

function html(document, fault = '') {
  const markup = '<!doctype html>' + renderToStaticMarkup(document);
  return fault ? markup.replace('<html lang="en">', `<html lang="en" data-fault="${fault}">`) : markup;
}

function send(res, status, headers, body) {
  res.writeHead(status, {'content-type': 'text/html; charset=utf-8', ...headers});
  res.end(body);
}

const origin = http.createServer((req, res) => {
  counters.originRequests += 1;
  const url = new URL(req.url, `http://${req.headers.host}`);
  const fault = req.headers['x-northstar-fault'] || '';
  const traceparent = req.headers.traceparent || '';
  const safeTrace = validTraceparent.test(traceparent) ? traceparent : '00-00000000000000000000000000000016-0000000000000016-01';
  if (traceparent && traceparent !== safeTrace) counters.rejectedTraceparents += 1;
  const common = {'x-origin-traceparent': safeTrace, 'x-content-version': 'northstar-2026-08-03'};

  if (url.pathname === '/assets/client.js') {
    res.writeHead(200, {'content-type': 'text/javascript; charset=utf-8', 'cache-control': 'public, max-age=31536000, immutable'});
    return res.end(clientBundle);
  }
  if (url.pathname === '/api/live') {
    res.writeHead(200, {'content-type': 'application/json', 'cache-control': 'no-store', ...common});
    return res.end(JSON.stringify({condition: 'Clear', version: 'live-42'}));
  }
  if (url.pathname === '/third-party.js') {
    const delay = Math.min(Number(url.searchParams.get('delay') || 0), 1000);
    return setTimeout(() => {
      res.writeHead(503, {'content-type': 'text/javascript', 'cache-control': 'no-store'});
      res.end('throw new Error("contained third-party failure")');
    }, delay);
  }
  if (url.pathname === '/sky-events') {
    const region = cleanRegion(req.headers['x-region']);
    return send(res, 200, {'cache-control': 'public, max-age=60, stale-while-revalidate=30', vary: 'x-region', ...common}, html(React.createElement(Layout, {title: 'Sky events'}, React.createElement(SkyEvents, {region})), fault));
  }
  if (url.pathname.startsWith('/events/')) {
    const id = url.pathname.split('/')[2];
    const event = events.find((row) => row.id === id) || events[0];
    res.writeHead(200, {'content-type': 'text/html; charset=utf-8', 'cache-control': 'public, max-age=20', ...common});
    res.write('<!doctype html>');
    const stream = renderToPipeableStream(React.createElement(Layout, {title: event.title}, React.createElement(EventDetail, {event})), {
      onShellReady() {
        stream.pipe(res);
        setTimeout(() => {}, 25);
      },
      onError(error) {
        console.error('stream error', error.message);
      }
    });
    return setTimeout(() => stream.abort(), 2000);
  }
  if (url.pathname === '/live') {
    return send(res, 200, {'cache-control': 'public, max-age=30', ...common}, html(React.createElement(Layout, {title: 'Live'}, React.createElement(LiveShell)), fault));
  }
  if (url.pathname === '/staff/schedule') {
    const alias = aliasFromCookie(req.headers.cookie);
    const state = JSON.stringify({alias}).replaceAll('<', '\\u003c');
    const island = renderToString(React.createElement(StaffIsland, {alias}));
    const body = `<!doctype html><html lang="en"${fault ? ` data-fault="${fault}"` : ''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Staff schedule · Northstar</title><style>body{font:16px system-ui;max-width:52rem;margin:2rem auto;padding:0 1rem}:focus-visible{outline:3px solid #7b2cff;outline-offset:3px}</style></head><body><a href="#main">Skip to content</a><main id="main"><h1>Private staff schedule</h1><div id="staff-island" data-alias="${alias}">${island}</div></main><script type="application/json" id="staff-state">${state}</script><script type="module" src="/assets/client.js"></script></body></html>`;
    return send(res, 200, {'cache-control': 'private, no-store', vary: 'cookie', ...common}, body);
  }
  send(res, 404, {'cache-control': 'no-store', ...common}, '<!doctype html><h1>Not found</h1>');
});

function cacheKey(url, headers, incomplete = false) {
  if (incomplete) return url.pathname;
  return `${url.pathname}|region=${cleanRegion(headers['x-region'])}`;
}

const edge = http.createServer(async (req, res) => {
  counters.edgeRequests += 1;
  const url = new URL(req.url, `http://${req.headers.host}`);
  if (url.pathname === '/telemetry/snapshot') {
    res.writeHead(200, {'content-type': 'application/json', 'cache-control': 'no-store'});
    return res.end(JSON.stringify({...counters, cacheEntries: cache.size, traceFields: ['traceparent'], sensitiveFields: []}));
  }
  const isPrivate = url.pathname === '/staff/schedule' || url.pathname === '/api/live' || url.pathname === '/telemetry/snapshot';
  const fault = req.headers['x-northstar-fault'] || '';
  const key = cacheKey(url, req.headers, fault === 'cache-key');
  if (!isPrivate && cache.has(key)) {
    counters.cacheHits += 1;
    const hit = cache.get(key);
    res.writeHead(hit.status, {...hit.headers, 'x-cache': 'HIT'});
    return res.end(hit.body);
  }
  if (isPrivate) counters.privateBypasses += 1;
  else counters.cacheMisses += 1;
  const upstream = await fetch(`http://127.0.0.1:${originPort}${req.url}`, {headers: req.headers});
  const body = Buffer.from(await upstream.arrayBuffer());
  const headers = Object.fromEntries(upstream.headers.entries());
  if (!isPrivate && /public/.test(headers['cache-control'] || '') && upstream.ok) cache.set(key, {status: upstream.status, headers, body});
  res.writeHead(upstream.status, {...headers, 'x-cache': isPrivate ? 'BYPASS' : 'MISS'});
  res.end(body);
});

origin.listen(originPort, '127.0.0.1', () => edge.listen(edgePort, '127.0.0.1'));

function shutdown() {
  edge.close(() => origin.close(() => process.exit(0)));
}
process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);
