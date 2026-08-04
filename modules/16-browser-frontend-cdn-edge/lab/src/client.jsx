import React from 'react';
import {createRoot, hydrateRoot} from 'react-dom/client';
import {StaffIsland, events} from './app.js';

const fault = document.documentElement.dataset.fault || '';

function busy(ms) {
  const end = performance.now() + ms;
  while (performance.now() < end) {}
}

if (fault === 'long-task') busy(180);

if (location.pathname === '/sky-events') {
  const select = document.querySelector('#region');
  select?.addEventListener('change', () => {
    const region = select.value;
    const list = document.querySelector('#event-list');
    const filtered = events.filter((item) => item.region === region || item.region === 'global');
    list.replaceChildren(...filtered.map((item) => {
      const article = document.createElement('article');
      article.className = 'card';
      article.innerHTML = `<h2><a href="/events/${item.id}">${item.title}</a></h2><p>${item.time} · ${item.region}</p>`;
      return article;
    }));
  });
}

if (location.pathname === '/live') {
  const status = document.querySelector('#live-status');
  const load = async () => {
    const response = await fetch('/api/live', {cache: 'no-store'});
    const data = await response.json();
    status.textContent = `${data.condition}; updated ${data.version}`;
  };
  document.querySelector('#refresh-live')?.addEventListener('click', load);
  load();
}

if (location.pathname === '/staff/schedule') {
  const root = document.querySelector('#staff-island');
  const serverAlias = root.dataset.alias;
  const alias = fault === 'hydrate' ? 'different-client-state' : serverAlias;
  hydrateRoot(root, <StaffIsland alias={alias} />, {
    onRecoverableError(error) {
      window.__northstarHydrationErrors = [...(window.__northstarHydrationErrors || []), error.message];
    }
  });
  document.querySelector('#confirm-shift')?.addEventListener('click', (event) => {
    document.querySelector('#confirm-status').textContent = 'Shift confirmed';
    event.currentTarget.focus();
  });
}

if (fault === 'resource-leak') {
  window.__northstarLeakTimer = setInterval(() => {}, 1000);
  window.addEventListener('northstar-leak', () => document.body.dataset.leaked = 'true');
  window.__northstarActiveResources = {timers: 1, listeners: 1};
} else {
  window.__northstarActiveResources = {timers: 0, listeners: 0};
}

if (fault === 'third-party') {
  const control = document.querySelector('#region');
  if (control) control.disabled = true;
  const script = document.createElement('script');
  script.src = '/third-party.js?delay=600';
  script.async = false;
  script.addEventListener('error', () => { window.__northstarThirdPartyFailure = true; });
  document.head.append(script);
}

window.__northstarReady = true;
