import {test, expect} from '@playwright/test';

async function contextWithFault(browser, fault) {
  return browser.newContext({extraHTTPHeaders: {'x-northstar-fault': fault}});
}

test('F01 long task is observable and repaired default has none', async ({browser}) => {
  const run = async (fault) => {
    const context = fault ? await contextWithFault(browser, fault) : await browser.newContext();
    await context.addInitScript(() => {
      window.__northstarLongTasks = [];
      new PerformanceObserver((list) => window.__northstarLongTasks.push(...list.getEntries().map((row) => row.duration))).observe({type: 'longtask', buffered: true});
    });
    const page = await context.newPage();
    await page.goto('/sky-events');
    await expect.poll(() => page.evaluate(() => window.__northstarReady)).toBe(true);
    const observations = await page.evaluate(() => window.__northstarLongTasks);
    await context.close();
    return observations;
  };
  expect((await run('long-task')).some((duration) => duration >= 150)).toBe(true);
  expect((await run('')).some((duration) => duration >= 150)).toBe(false);
});

test('F02 hydration state mismatch is exposed and repaired', async ({browser}) => {
  const broken = await contextWithFault(browser, 'hydrate');
  const page = await broken.newPage();
  await page.goto('/staff/schedule');
  await expect.poll(() => page.evaluate(() => (window.__northstarHydrationErrors || []).length)).toBeGreaterThan(0);
  await broken.close();
  const repaired = await browser.newPage();
  await repaired.goto('/staff/schedule');
  expect(await repaired.evaluate(() => window.__northstarHydrationErrors || [])).toEqual([]);
});

test('F03 route-owned timer/listener deltas return to zero after repair', async ({browser}) => {
  const broken = await contextWithFault(browser, 'resource-leak');
  const page = await broken.newPage();
  await page.goto('/sky-events');
  expect(await page.evaluate(() => window.__northstarActiveResources)).toEqual({timers: 1, listeners: 1});
  await broken.close();
  const repaired = await browser.newPage();
  await repaired.goto('/sky-events');
  expect(await repaired.evaluate(() => window.__northstarActiveResources)).toEqual({timers: 0, listeners: 0});
});

test('F04 third-party failure cannot disable repaired core interaction', async ({browser}) => {
  const broken = await contextWithFault(browser, 'third-party');
  const page = await broken.newPage();
  await page.goto('/sky-events');
  await expect(page.getByLabel('Observing region')).toBeDisabled();
  await expect.poll(() => page.evaluate(() => window.__northstarThirdPartyFailure || false)).toBe(true);
  await broken.close();
  const repaired = await browser.newPage();
  await repaired.goto('/sky-events');
  await expect(repaired.getByLabel('Observing region')).toBeEnabled();
});

test('F05 incomplete public key collides while repaired key preserves region', async ({request}) => {
  const brokenNorth = await request.get('/sky-events?pair=f05-broken-n', {headers: {'x-region': 'north', 'x-northstar-fault': 'cache-key'}});
  const brokenSouth = await request.get('/sky-events?pair=f05-broken-s', {headers: {'x-region': 'south', 'x-northstar-fault': 'cache-key'}});
  expect(await brokenNorth.text()).toContain('Aurora Watch');
  expect(await brokenSouth.text()).toContain('Aurora Watch');
  const repairedSouth = await request.get('/sky-events?pair=f05-repaired', {headers: {'x-region': 'south'}});
  expect(await repairedSouth.text()).toContain('Meteor Window');
});

test('F06 unsafe private caching crosses aliases while repaired responses bypass', async ({request}) => {
  const brokenVega = await request.get('/staff/schedule?pair=f06', {headers: {cookie: 'northstar_alias=vega', 'x-northstar-fault': 'private-cache'}});
  const brokenLyra = await request.get('/staff/schedule?pair=f06', {headers: {cookie: 'northstar_alias=lyra', 'x-northstar-fault': 'private-cache'}});
  expect(await brokenVega.text()).toContain('vega');
  expect(await brokenLyra.text()).toContain('vega');
  const repairedLyra = await request.get('/staff/schedule?pair=f06-repaired', {headers: {cookie: 'northstar_alias=lyra'}});
  expect(repairedLyra.headers()['x-cache']).toBe('BYPASS');
  expect(await repairedLyra.text()).toContain('lyra');
});

test('F07 origin failure requires bounded marked public stale and private fail-closed', async ({request}) => {
  await request.get('/sky-events?pair=f07', {headers: {'x-region': 'south'}});
  const unsafe = await request.get('/sky-events?pair=f07', {headers: {'x-region': 'south', 'x-northstar-fault': 'origin-failure-unsafe'}});
  expect(unsafe.headers()['x-stale-age']).toBe('3600');
  expect(unsafe.headers()['x-degraded']).toBe('false');
  const repaired = await request.get('/sky-events?pair=f07', {headers: {'x-region': 'south', 'x-northstar-fault': 'origin-failure-bounded'}});
  expect(repaired.headers()['x-stale-age']).toBe('60');
  expect(repaired.headers()['x-degraded']).toBe('true');
  const privateResponse = await request.get('/staff/schedule', {headers: {'x-northstar-fault': 'origin-failure-bounded'}});
  expect(privateResponse.status()).toBe(503);
  expect(privateResponse.headers()['x-cache']).toBe('FAIL-CLOSED');
});

test('F08 delayed critical bundle violates guardrail while repaired load fits it', async ({browser}) => {
  const duration = async (fault) => {
    const context = fault ? await contextWithFault(browser, fault) : await browser.newContext();
    const page = await context.newPage();
    const start = Date.now();
    await page.goto('/sky-events');
    await expect.poll(() => page.evaluate(() => window.__northstarReady)).toBe(true);
    const elapsed = Date.now() - start;
    await context.close();
    return elapsed;
  };
  expect(await duration('critical-bloat')).toBeGreaterThan(1200);
  expect(await duration('')).toBeLessThan(1200);
});
