/* ============================================================
   service-worker.js  —  Offline support
   Animal Genetics and Breeding Studio
   ------------------------------------------------------------
   Strategy:
     - App shell (HTML, CSS, JS, data files): cache first, then
       update in the background. The site opens instantly and
       works with no signal.
     - Images: cache as they are used, up to a sensible limit.

   IMPORTANT: bump CACHE_VERSION whenever you change any file in
   PRECACHE, otherwise students keep seeing the old version.
   ============================================================ */

var CACHE_VERSION = "vgen-v17";
var SHELL_CACHE = CACHE_VERSION + "-shell";
var IMG_CACHE = CACHE_VERSION + "-img";

var PRECACHE = [
  "./",
  "index.html",
  "manifest.json",

  "assets/css/tokens.css",
  "assets/css/main.css",
  "assets/css/sections.css",
  "assets/css/deep-guide.css",
  "assets/css/events.css",
  "assets/css/animations.css",

  "data/data-syllabus.JS",
  "data/data-theory-unit1.JS",
  "data/data-theory-unit2.JS",
  "data/data-theory-unit3.JS",
  "data/data-practical.JS",
  "data/data-why.JS",
  "data/data-qa.JS",
  "data/data-quiz.JS",
  "data/events-data.js",

  "js/store.js",
  "js/quiz.js",
  "js/dashboard.js",
  "js/glossary.js",
  "js/search.js",
  "js/deep-guide.js",
  "js/events.js",
  "js/app.js",

  "images/icon-192.png",
  "images/icon-512.png",
  "images/icon-maskable-512.png"
];

self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open(SHELL_CACHE)
      .then(function (c) {
        // addAll fails entirely if one file 404s, so add them one by one.
        return Promise.all(PRECACHE.map(function (url) {
          return c.add(url).catch(function () { /* skip missing file */ });
        }));
      })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        if (k.indexOf(CACHE_VERSION) !== 0) return caches.delete(k);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener("message", function (e) {
  if (e.data && e.data.type === "SKIP_WAITING") {
    self.skipWaiting();
  }
});

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;

  var url = new URL(req.url);
  if (url.origin !== location.origin) return;   // never touch third-party requests

  // ---- HTML Navigation Requests (Opening app / refreshing while offline) ----
  if (req.mode === "navigate" || (req.headers.get("accept") && req.headers.get("accept").indexOf("text/html") !== -1)) {
    e.respondWith(
      fetch(req).then(function (res) {
        if (res && res.status === 200) {
          var copy = res.clone();
          caches.open(SHELL_CACHE).then(function (c) { c.put(req, copy); });
        }
        return res;
      }).catch(function () {
        return caches.match("index.html").then(function (hit) {
          return hit || caches.match("./");
        });
      })
    );
    return;
  }

  // ---- Images: cache on first use ----
  if (/\.(png|jpg|jpeg|webp|gif|svg)$/i.test(url.pathname)) {
    e.respondWith(
      caches.open(IMG_CACHE).then(function (c) {
        return c.match(req).then(function (hit) {
          if (hit) return hit;
          return fetch(req).then(function (res) {
            if (res && res.status === 200) c.put(req, res.clone());
            return res;
          }).catch(function () { return hit; });
        });
      })
    );
    return;
  }

  // ---- App code & data (JS, CSS, JSON, HTML): Network-first with Cache fallback ----
  // Ensures the live GitHub web link always delivers the newest updates immediately
  // while retaining full offline access when disconnected.
  e.respondWith(
    fetch(req).then(function (res) {
      if (res && res.status === 200) {
        var copy = res.clone();
        caches.open(SHELL_CACHE).then(function (c) { c.put(req, copy); });
      }
      return res;
    }).catch(function () {
      // Offline fallback
      return caches.match(req).then(function (hit) {
        if (hit) return hit;
        if (req.mode === "navigate" || (req.headers.get("accept") && req.headers.get("accept").indexOf("text/html") !== -1)) {
          return caches.match("index.html").then(function (fallback) {
            return fallback || caches.match("./");
          });
        }
      });
    })
  );
});
