import { useEffect, useState } from "react";
import { api, formatearPeso } from "../servicios/api.js";
import TarjetaIndicador from "../componentes/TarjetaIndicador.jsx";
import TablaOrdenes from "../componentes/TablaOrdenes.jsx";
import Boton from "../componentes/Boton.jsx";

/**
 * Panel principal con los indicadores de la operación.
 */
export default function Panel({ alNavegar }) {
  const [resumen, setResumen] = useState(null);
  const [ordenes, setOrdenes] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    cargar();
  }, []);

  async function cargar() {
    try {
      const [datosResumen, datosOrdenes] = await Promise.all([
        api.resumen(),
        api.ordenes()
      ]);
      setResumen(datosResumen);
      setOrdenes(datosOrdenes);
    } catch (fallo) {
      setError(fallo.message);
    }
  }

  if (error) {
    return <p className="mensaje-error">{error}</p>;
  }

  if (!resumen) {
    return <p className="texto-suave">Cargando indicadores...</p>;
  }

  return (
    <>
      <section className="tarjetas">
        <TarjetaIndicador
          etiqueta="Órdenes activas"
          valor={`${resumen.enCola} / ${resumen.enProceso}`}
          detalle="en cola / en proceso"
        />
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
          detalle="por vehículo entregado"
        />
      </section>

      <section className="bloque">
        <div className="titulo-bloque">
          <h2>Últimas órdenes de lavado</h2>
          <Boton alHacerClic={() => alNavegar("ordenes")}>Registrar orden</Boton>
        </div>
        <TablaOrdenes ordenes={ordenes.slice(0, 8)} compacta />
      </section>
    </>
  );
}
