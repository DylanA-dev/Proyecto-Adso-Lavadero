const CACHE = "aqualavado-v1";
const RECURSOS = ["/", "/index.html", "/manifest.webmanifest", "/icono.svg"];

self.addEventListener("install", (evento) => {
  evento.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(RECURSOS))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (evento) => {
  evento.waitUntil(
    caches.keys().then((claves) =>
      Promise.all(
        claves.filter((clave) => clave !== CACHE).map((clave) => caches.delete(clave))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (evento) => {
  if (evento.request.method !== "GET") {
    return;
  }
  evento.respondWith(
    fetch(evento.request)
      .then((respuesta) => {
        const copia = respuesta.clone();
        caches.open(CACHE).then((cache) => cache.put(evento.request, copia));
        return respuesta;
      })
      .catch(() => caches.match(evento.request).then((copia) => copia || caches.match("/")))
  );
});
