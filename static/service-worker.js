const CACHE_NAME = 'cpi-calculator-cache-v1'; // Unique cache name
const urlsToCache = [ // List of static assets to cache
  '/',
  '/static/css/style.css',
  '/static/js/script.js', // If you have any JS files
  '/static/images/icon-192x192.png', // Add your icons
  '/static/images/icon-512x512.png',
  '/templates/index.html' // You can cache the base HTML if it's largely static
];

self.addEventListener('install', event => { // Install event
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache); // Cache all specified URLs
      })
  );
});

self.addEventListener('fetch', event => { // Fetch event
  event.respondWith(
    caches.match(event.request) // Try to find request in cache
      .then(response => {
        // Cache hit - return response from cache
        if (response) {
          return response;
        }
        return fetch(event.request); // Not in cache - fetch from network
      }
    )
  );
});

// Optional: Activate event for cache cleanup (for future updates to service worker)
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName); // Delete old caches
          }
        })
      );
    })
  );
});