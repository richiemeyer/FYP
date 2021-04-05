// Telling the service worker which urls to cache
let CACHE_NAME = 'my-cache';
let urlsToCache = [
    '/',
    '/profile/',
    '/login/',
    '/register/',
    '/about/'
];

self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

// Fetch event that will decide whether to return content from cache or through the network
self.addEventListener('fetch', function (event) {
    event.respondWith(
        caches.match(event.request)
            .then(function (response) {
                    // Cache hit - return response
                    if (response) {
                        return response;
                    }
                    return fetch(event.request);
                }
            )
    );
});

self.addEventListener('activate', function (event) {
    var cacheWhitelist = ['pigment'];
    event.waitUntil(
        caches.keys().then(function (cacheNames) {
            return Promise.all(
                cacheNames.map(function (cacheName) {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});


// self.addEventListener('sync', function (event) {
//     if (event.tag == 'myFirstSync') {
//         event.waitUntil(update_db());
//     }
// });
//
// self.addEventListener('install', (e) => {
//   console.log('[Service Worker] Install');
// });
