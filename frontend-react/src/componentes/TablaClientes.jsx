import Boton from "./Boton.jsx";

/**
 * Tabla de clientes con opción de eliminación.
 */
export default function TablaClientes({ clientes, alEliminar }) {
  return (
    <div className="tabla-contenedor">
      <table className="tabla tabla-ajustada">
        <colgroup>
          <col style={{ width: "7%" }} />
          <col style={{ width: "17%" }} />
          <col style={{ width: "18%" }} />
          <col style={{ width: "16%" }} />
          <col style={{ width: "24%" }} />
          <col style={{ width: "18%" }} />
        </colgroup>
        <thead>
          <tr>
            <th>Id</th>
            <th>Documento</th>
            <th>Nombre</th>
            <th>Teléfono</th>
            <th>Correo</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          {clientes.map((cliente) => (
            <tr key={cliente.idCliente}>
              <td>{cliente.idCliente}</td>
              <td>{cliente.documento}</td>
              <td>{cliente.nombre}</td>
              <td>{cliente.telefono}</td>
              <td>{cliente.correo}</td>
              <td>
                <Boton
                  variante="secundario"
                  alHacerClic={() => alEliminar(cliente)}
                >
                  Eliminar
                </Boton>
              </td>
            </tr>
          ))}
          {clientes.length === 0 && (
            <tr>
              <td colSpan={6} className="texto-suave">
                No hay clientes registrados.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
