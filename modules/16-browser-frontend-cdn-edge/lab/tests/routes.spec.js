import {test, expect} from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('public regional cache keys do not collide', async ({request}) => {
  const north = await request.get('/sky-events', {headers: {'x-region': 'north'}});
  const south = await request.get('/sky-events', {headers: {'x-region': 'south'}});
  const southAgain = await request.get('/sky-events', {headers: {'x-region': 'south'}});
  expect(await north.text()).toContain('Aurora Watch');
  expect(await south.text()).toContain('Meteor Window');
  expect(southAgain.headers()['x-cache']).toBe('HIT');
});

test('private staff responses bypass shared cache across sessions', async ({request}) => {
  const vega = await request.get('/staff/schedule', {headers: {cookie: 'northstar_alias=vega'}});
  const lyra = await request.get('/staff/schedule', {headers: {cookie: 'northstar_alias=lyra'}});
  expect(vega.headers()['cache-control']).toContain('private');
  expect(vega.headers()['x-cache']).toBe('BYPASS');
  expect(lyra.headers()['x-cache']).toBe('BYPASS');
  expect(await vega.text()).toContain('vega');
  expect(await lyra.text()).toContain('lyra');
});

test('static, streaming, live, and island routes execute their contracts', async ({page, context}) => {
  await context.addCookies([{name: 'northstar_alias', value: 'vega', domain: '127.0.0.1', path: '/'}]);
  await page.goto('/sky-events');
  await expect(page.getByRole('heading', {name: 'Public sky events'})).toBeVisible();
  await page.getByLabel('Observing region').selectOption('south');
  await expect(page.getByText('Meteor Window')).toBeVisible();

  await page.goto('/events/aurora-7');
  await expect(page.getByRole('heading', {name: 'Aurora Watch'})).toBeVisible();

  await page.goto('/live');
  await expect(page.getByRole('status')).toContainText('Clear');

  await page.goto('/staff/schedule');
  await expect(page.getByRole('heading', {name: "vega's observing shift"})).toBeVisible();
  expect(await page.evaluate(() => window.__northstarHydrationErrors || [])).toEqual([]);
});

test('critical journeys pass axe plus explicit keyboard and focus checks', async ({page}) => {
  for (const route of ['/sky-events', '/live', '/staff/schedule']) {
    await page.goto(route);
    const results = await new AxeBuilder({page}).analyze();
    expect(results.violations).toEqual([]);
  }
  await page.goto('/staff/schedule');
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link', {name: 'Skip to content'})).toBeFocused();
  await page.getByRole('button', {name: 'Confirm shift'}).focus();
  await page.keyboard.press('Enter');
  await expect(page.getByRole('status')).toHaveText('Shift confirmed');
  await expect(page.getByRole('button', {name: 'Confirm shift'})).toBeFocused();
});

test('hydration mismatch is observed and repaired state is clean', async ({browser}) => {
  const broken = await browser.newContext({extraHTTPHeaders: {'x-northstar-fault': 'hydrate'}});
  const brokenPage = await broken.newPage();
  await brokenPage.goto('/staff/schedule');
  await expect.poll(() => brokenPage.evaluate(() => (window.__northstarHydrationErrors || []).length)).toBeGreaterThan(0);
  await broken.close();

  const repaired = await browser.newPage();
  await repaired.goto('/staff/schedule');
  expect(await repaired.evaluate(() => window.__northstarHydrationErrors || [])).toEqual([]);
});

test('trace input is sanitized before origin correlation', async ({request}) => {
  const response = await request.get('/events/lunar-2?trace-test=1', {headers: {traceparent: 'not-a-trace'}});
  expect(response.headers()['x-origin-traceparent']).toMatch(/^00-[0-9a-f]{32}-[0-9a-f]{16}-0[01]$/);
  expect(response.headers()['x-origin-traceparent']).not.toBe('not-a-trace');
  const snapshot = await request.get('/telemetry/snapshot');
  const counters = await snapshot.json();
  expect(counters.rejectedTraceparents).toBeGreaterThan(0);
  expect(counters.sensitiveFields).toEqual([]);
});

test('constrained profile preserves a usable critical route and records timing', async ({browser}) => {
  const context = await browser.newContext({viewport: {width: 390, height: 844}, deviceScaleFactor: 2});
  const page = await context.newPage();
  const client = await context.newCDPSession(page);
  await client.send('Network.emulateNetworkConditions', {offline: false, latency: 150, downloadThroughput: 187500, uploadThroughput: 93750, connectionType: 'cellular3g'});
  const started = Date.now();
  await page.goto('/sky-events');
  await expect(page.getByLabel('Observing region')).toBeEnabled();
  const elapsedMs = Date.now() - started;
  expect(elapsedMs).toBeLessThan(10000);
  test.info().annotations.push({type: 'lab-observation', description: `critical-route elapsed=${elapsedMs}ms; not field evidence`});
  await context.close();
});

test('200% zoom reflows at an effective 320 CSS pixels', async ({browser}) => {
  const context = await browser.newContext({viewport: {width: 640, height: 800}});
  const page = await context.newPage();
  await page.goto('/sky-events');
  const layout = await page.evaluate(() => {
    document.documentElement.style.zoom = '200%';
    return {
      viewportWidth: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth
    };
  });
  expect(layout.scrollWidth).toBeLessThanOrEqual(layout.viewportWidth);
  await expect(page.getByLabel('Observing region')).toBeVisible();
  await context.close();
});

test('public content and navigation remain available with JavaScript disabled', async ({browser}) => {
  const context = await browser.newContext({javaScriptEnabled: false});
  const page = await context.newPage();
  await page.goto('/sky-events');
  await expect(page.getByRole('heading', {name: 'Public sky events'})).toBeVisible();
  await expect(page.getByLabel('Observing region')).toBeVisible();
  await expect(page.getByRole('link', {name: 'Aurora Watch'})).toBeVisible();
  await page.getByRole('link', {name: 'Aurora Watch'}).click();
  await expect(page.getByRole('heading', {name: 'Aurora Watch'})).toBeVisible();
  await expect(page.getByRole('status')).toContainText('Forecast unavailable without JavaScript');
  await expect(page.getByText('Visibility: north. Starts 22:30 UTC.')).toBeVisible();
  await context.close();
});

test('streamed detail exposes a bounded status while delayed content resolves', async ({page}) => {
  await page.goto('/events/aurora-7');
  await expect(page.getByRole('heading', {name: 'Aurora Watch'})).toBeVisible();
  await expect(page.getByRole('status')).toContainText('Forecast: clear');
});
