import { useEffect, useState } from "react";
import { api, formatearPeso } from "../servicios/api.js";
import TarjetaIndicador from "../componentes/TarjetaIndicador.jsx";

/**
 * Reporte de ingresos y lavados por tipo de servicio.
 */
export default function Reportes() {
  const [resumen, setResumen] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    api
      .resumen()
      .then(setResumen)
      .catch((fallo) => setError(fallo.message));
  }, []);

  if (error) {
    return <p className="mensaje-error">{error}</p>;
  }

  if (!resumen) {
    return <p className="texto-suave">Generando reporte...</p>;
  }

  const servicios = Object.keys(resumen.cantidades);

  return (
    <>
      <section className="tarjetas">
        <TarjetaIndicador
          etiqueta="Lavados entregados"
          valor={resumen.entregadas}
          detalle="órdenes cerradas"
        />
        <TarjetaIndicador
          etiqueta="Ingresos"
          valor={formatearPeso(resumen.ingresos)}
          detalle="servicios entregados"
        />
        <TarjetaIndicador
          etiqueta="Ticket promedio"
          valor={formatearPeso(resumen.promedio)}
          detalle="por vehículo"
        />
      </section>

      <section className="bloque">
        <h2>Lavados por tipo de servicio</h2>
        <div className="tabla-contenedor">
          <table className="tabla">
            <thead>
              <tr>
                <th>Servicio</th>
                <th>Cantidad de órdenes</th>
                <th>Valor acumulado</th>
              </tr>
            </thead>
            <tbody>
              {servicios.map((servicio) => (
                <tr key={servicio}>
                  <td>{servicio}</td>
                  <td>{resumen.cantidades[servicio]}</td>
                  <td>{formatearPeso(resumen.valores[servicio])}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </>
  );
}
