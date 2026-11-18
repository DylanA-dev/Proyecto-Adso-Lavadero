const OPCIONES = [
  { clave: "panel", texto: "Panel principal" },
  { clave: "clientes", texto: "Clientes" },
  { clave: "ordenes", texto: "Órdenes de lavado" },
  { clave: "reportes", texto: "Reportes" }
];

/**
 * Menú de navegación del sistema. En pantallas pequeñas se convierte en una
 * barra inferior para facilitar el uso desde el teléfono.
 */
export default function BarraLateral({ seccion, alCambiar, usuario, alCerrarSesion }) {
  return (
    <aside className="barra-lateral">
      <div className="marca-lateral">
        <span className="logo">AQUA</span>
        <span className="logo-acento">LAVADO</span>
        <small>Gestión de lavadero</small>
      </div>

      <nav aria-label="Menú principal">
        {OPCIONES.map((opcion) => (
          <button
            key={opcion.clave}
            type="button"
            className={seccion === opcion.clave ? "activo" : ""}
            onClick={() => alCambiar(opcion.clave)}
          >
            {opcion.texto}
          </button>
        ))}
      </nav>

      <div className="sesion">
        <strong>{usuario.nombre}</strong>
        <span>{usuario.rol}</span>
        <button type="button" className="cerrar" onClick={alCerrarSesion}>
          Cerrar sesión
        </button>
      </div>
    </aside>
  );
}
