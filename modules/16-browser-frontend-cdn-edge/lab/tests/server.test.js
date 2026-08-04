import test from 'node:test';
import assert from 'node:assert/strict';
import React from 'react';
import {renderToStaticMarkup, renderToString} from 'react-dom/server';
import {Layout, SkyEvents, StaffIsland} from '../src/app.js';

test('regional static route contains semantic controls and global content', () => {
  const markup = renderToStaticMarkup(React.createElement(Layout, {title: 'test'}, React.createElement(SkyEvents, {region: 'north'})));
  assert.match(markup, /<main id="main">/);
  assert.match(markup, /<select id="region"/);
  assert.match(markup, /Aurora Watch/);
  assert.match(markup, /Lunar Occultation/);
  assert.doesNotMatch(markup, /Meteor Window/);
});

test('staff island is deterministic for identical server and client state', () => {
  const first = renderToString(React.createElement(StaffIsland, {alias: 'vega'}));
  const second = renderToString(React.createElement(StaffIsland, {alias: 'vega'}));
  assert.equal(first, second);
  assert.match(first, /vega&#x27;s observing shift/);
  assert.match(first, /<button id="confirm-shift"/);
});
