const BASE = import.meta.env.VITE_API_URL ?? "/api";

/**
 * Ejecuta una petición a la API y devuelve el cuerpo en formato JSON.
 * @param {string} ruta ruta relativa del servicio
 * @param {object} opciones configuración de fetch
 */
async function solicitar(ruta, opciones = {}) {
  const configuracion = {
    headers: { "Content-Type": "application/json" },
    ...opciones
  };

  const respuesta = await fetch(`${BASE}${ruta}`, configuracion);
  if (!respuesta.ok) {
    let mensaje = "No fue posible completar la operación.";
    try {
      const cuerpo = await respuesta.json();
      mensaje = cuerpo.mensaje || cuerpo.detalle || cuerpo.error || mensaje;
    } catch {
      // Se conserva el mensaje general.
    }
    throw new Error(mensaje);
  }

  if (respuesta.status === 204) {
    return null;
  }
  return respuesta.json();
}

export const api = {
  login: (correo, clave) =>
    solicitar("/auth/login", {
      method: "POST",
      body: JSON.stringify({ correo, clave })
    }),

  ordenes: () => solicitar("/ordenes"),
  crearOrden: (orden) =>
    solicitar("/ordenes", { method: "POST", body: JSON.stringify(orden) }),
  avanzarOrden: (id) => solicitar(`/ordenes/${id}/estado`, { method: "PUT" }),

  clientes: () => solicitar("/clientes"),
  crearCliente: (cliente) =>
    solicitar("/clientes", { method: "POST", body: JSON.stringify(cliente) }),
  eliminarCliente: (id) => solicitar(`/clientes/${id}`, { method: "DELETE" }),

  vehiculos: () => solicitar("/vehiculos"),
  servicios: () => solicitar("/servicios"),
  resumen: () => solicitar("/reportes/resumen")
};

export function formatearPeso(valor) {
  return "$" + Number(valor ?? 0).toLocaleString("es-CO");
}

export function formatearFecha(fecha) {
  if (!fecha) {
    return "Pendiente";
  }
  return new Date(fecha).toLocaleString("es-CO", {
    dateStyle: "short",
    timeStyle: "short"
  });
}
