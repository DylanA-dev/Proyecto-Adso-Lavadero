import EstadoOrden from "./EstadoOrden.jsx";
import { formatearFecha, formatearPeso } from "../servicios/api.js";

/**
 * Tabla de órdenes de lavado con la acción para avanzar de estado.
 */
export default function TablaOrdenes({ ordenes, alAvanzar, compacta = false }) {
  return (
    <div className="tabla-contenedor">
      <table className={`tabla tabla-ajustada${compacta ? " tabla-compacta" : ""}`}>
        <colgroup>
          {(compacta
            ? ["8%", "12%", "19%", "19%", "20%", "22%"]
            : ["8%", "11%", "14%", "14%", "13%", "17%", "11%", "12%"]
          ).map((ancho, indice) => (
            <col key={indice} style={{ width: ancho }} />
          ))}
        </colgroup>
        <thead>
          <tr>
            <th>Orden</th>
            <th>Placa</th>
            <th className="col-opcional">Servicio</th>
            <th className="col-opcional">Operario</th>
            {!compacta && <th>Ingreso</th>}
            <th>Estado</th>
            <th>Valor</th>
            {!compacta && <th>Acción</th>}
          </tr>
        </thead>
        <tbody>
          {ordenes.map((orden) => (
            <tr key={orden.idOrden}>
              <td>{orden.idOrden}</td>
              <td>{orden.placa}</td>
              <td className="col-opcional">{orden.nombreServicio}</td>
              <td className="col-opcional">{orden.nombreOperario}</td>
              {!compacta && <td>{formatearFecha(orden.fechaIngreso)}</td>}
              <td>
                <EstadoOrden estado={orden.estado} />
              </td>
              <td>{formatearPeso(orden.valor)}</td>
              {!compacta && (
                <td>
                  {orden.estado === "ENTREGADO" ? (
                    <span className="texto-suave">Entregado</span>
                  ) : (
                    <button
                      type="button"
                      className="boton boton-pequeno"
                      onClick={() => alAvanzar(orden.idOrden)}
                    >
                      Avanzar
                    </button>
                  )}
                </td>
              )}
            </tr>
          ))}
          {ordenes.length === 0 && (
            <tr>
              <td colSpan={compacta ? 6 : 8} className="texto-suave">
                No hay órdenes registradas.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
