// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py


var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
  '/offline',
  '/',
  '/static/css/django-pwa-app.css',
  '/static/index.css',
  '/static/home/img/iert_icon.png',
  //images
  "home/img/director.jpg",
  "home/img/dip.jpeg",
  "home/img/kk.jpg",
  "home/img/slide1.jpeg",
  "home/img/slide2.jpeg",
  "home/img/no6.jpg",
  "home/img/n1.jpg",
  "home/img/gr.png",
  "home/img/p.jpg",
  "home/img/swa.jpg",
  "home/img/aktu.png",
  "home/img/aicte.jpg",
  "home/img/si.png",
  "home/img/s.png",
  "home/img/download.png",
  "home/img/v.jpg",
  "home/img/dst-logo.png",

];

// Cache on install
self.addEventListener("install", event => {
  this.skipWaiting();
  event.waitUntil(
    caches.open(staticCacheName)
    .then(cache => {
      return cache.addAll(filesToCache);
    })
  )
});

// Clear cache on activate
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
        .filter(cacheName => (cacheName.startsWith("django-pwa-")))
        .filter(cacheName => (cacheName !== staticCacheName))
        .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});

// Serve from Cache
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
    .then(response => {
      return response || fetch(event.request);
    })
    .catch(() => {
      return caches.match('offline');
    })
  )
});
