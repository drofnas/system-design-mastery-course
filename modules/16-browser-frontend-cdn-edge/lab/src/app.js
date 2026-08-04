import React from 'react';

export const events = [
  {id: 'aurora-7', title: 'Aurora Watch', region: 'north', time: '22:30 UTC'},
  {id: 'meteor-4', title: 'Meteor Window', region: 'south', time: '03:10 UTC'},
  {id: 'lunar-2', title: 'Lunar Occultation', region: 'global', time: '05:45 UTC'}
];

export function Layout({title, children, script = true}) {
  return React.createElement('html', {lang: 'en'},
    React.createElement('head', null,
      React.createElement('meta', {charSet: 'utf-8'}),
      React.createElement('meta', {name: 'viewport', content: 'width=device-width,initial-scale=1'}),
      React.createElement('title', null, `${title} · Northstar`),
      React.createElement('style', null, 'body{font:16px system-ui;max-width:52rem;margin:2rem auto;padding:0 1rem;line-height:1.5}nav a{margin-right:1rem}:focus-visible{outline:3px solid #7b2cff;outline-offset:3px}.card{border:1px solid #777;border-radius:.5rem;padding:1rem;margin:.75rem 0}.status{min-height:1.5rem}')),
    React.createElement('body', null,
      React.createElement('a', {href: '#main'}, 'Skip to content'),
      React.createElement('nav', {'aria-label': 'Primary'},
        React.createElement('a', {href: '/sky-events'}, 'Sky events'),
        React.createElement('a', {href: '/live'}, 'Live'),
        React.createElement('a', {href: '/staff/schedule'}, 'Staff schedule')),
      React.createElement('main', {id: 'main'}, children),
      script ? React.createElement('script', {type: 'module', src: '/assets/client.js'}) : null));
}

export function SkyEvents({region}) {
  const visible = events.filter((event) => event.region === region || event.region === 'global');
  return React.createElement(React.Fragment, null,
    React.createElement('h1', null, 'Public sky events'),
    React.createElement('label', {htmlFor: 'region'}, 'Observing region'),
    React.createElement('select', {id: 'region', defaultValue: region},
      React.createElement('option', {value: 'north'}, 'North'),
      React.createElement('option', {value: 'south'}, 'South')),
    React.createElement('section', {id: 'event-list', 'aria-live': 'polite', 'aria-label': 'Matching events'},
      visible.map((event) => React.createElement('article', {className: 'card', key: event.id},
        React.createElement('h2', null, React.createElement('a', {href: `/events/${event.id}`}, event.title)),
        React.createElement('p', null, `${event.time} · ${event.region}`)))));
}

function Forecast({forecastPromise}) {
  const forecast = React.use(forecastPromise);
  return React.createElement('p', {id: 'stream-status', className: 'status', role: 'status'}, forecast);
}

export function EventDetail({event, forecastPromise}) {
  return React.createElement(React.Fragment, null,
    React.createElement('h1', null, event.title),
    React.createElement('p', null, `Visibility: ${event.region}. Starts ${event.time}.`),
    React.createElement(React.Suspense, {fallback: React.createElement('p', {id: 'stream-status', className: 'status', role: 'status'}, 'Forecast arriving…')},
      React.createElement(Forecast, {forecastPromise})),
    React.createElement('noscript', null,
      React.createElement('style', null, '#stream-status{display:none}'),
      React.createElement('p', {id: 'forecast-degraded', className: 'status', role: 'status'},
        'Forecast unavailable without JavaScript. Event time and visibility remain available.')));
}

export function LiveShell() {
  return React.createElement(React.Fragment, null,
    React.createElement('h1', null, 'Live observatory status'),
    React.createElement('p', {id: 'live-status', className: 'status', role: 'status'}, 'Loading current conditions…'),
    React.createElement('button', {id: 'refresh-live', type: 'button'}, 'Refresh conditions'));
}

export function StaffIsland({alias}) {
  return React.createElement('section', {'aria-labelledby': 'schedule-heading'},
    React.createElement('h2', {id: 'schedule-heading'}, `${alias}'s observing shift`),
    React.createElement('p', null, 'Primary telescope: Kepler Ridge'),
    React.createElement('button', {id: 'confirm-shift', type: 'button'}, 'Confirm shift'),
    React.createElement('p', {id: 'confirm-status', className: 'status', role: 'status'}));
}
