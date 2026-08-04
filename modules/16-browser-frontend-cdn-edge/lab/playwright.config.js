import {defineConfig, devices} from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  testMatch: '**/*.spec.js',
  fullyParallel: false,
  workers: 1,
  retries: 0,
  reporter: [['list'], ['json', {outputFile: 'test-results/results.json'}]],
  use: {
    baseURL: 'http://127.0.0.1:4180',
    trace: 'retain-on-failure',
    ...devices['Desktop Chrome']
  },
  webServer: {
    command: 'node src/server.js',
    url: 'http://127.0.0.1:4180/telemetry/snapshot',
    reuseExistingServer: false,
    timeout: 30000
  }
});
