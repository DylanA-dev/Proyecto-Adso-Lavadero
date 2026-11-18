import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./estilos.css";

if ("serviceWorker" in navigator && import.meta.env.PROD) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").catch(() => {
      // La aplicación sigue funcionando sin el service worker.
    });
  });
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
