import { useEffect, useState } from "react";
import { api } from "../servicios/api.js";
import TablaOrdenes from "../componentes/TablaOrdenes.jsx";
import FormularioOrden from "../componentes/FormularioOrden.jsx";

/**
 * Módulo de registro y control de órdenes de lavado.
 */
export default function Ordenes() {
  const [ordenes, setOrdenes] = useState([]);
  const [vehiculos, setVehiculos] = useState([]);
  const [servicios, setServicios] = useState([]);
  const [error, setError] = useState("");
  const [mensaje, setMensaje] = useState("");

  useEffect(() => {
    cargar();
  }, []);

  async function cargar() {
    try {
      const [datosOrdenes, datosVehiculos, datosServicios] = await Promise.all([
        api.ordenes(),
        api.vehiculos(),
        api.servicios()
      ]);
      setOrdenes(datosOrdenes);
      setVehiculos(datosVehiculos);
      setServicios(datosServicios);
    } catch (fallo) {
      setError(fallo.message);
    }
  }

  async function registrar(orden) {
    setError("");
    setMensaje("");
    try {
      await api.crearOrden(orden);
      setMensaje("Orden registrada y asignada a la cola de trabajo.");
      await cargar();
    } catch (fallo) {
      setError(fallo.message);
      throw fallo;
    }
  }

  async function avanzar(id) {
    setError("");
    setMensaje("");
    try {
      const actualizada = await api.avanzarOrden(id);
      setMensaje(`La orden ${id} pasó al estado ${actualizada.estado}.`);
      await cargar();
    } catch (fallo) {
      setError(fallo.message);
    }
  }

  return (
    <>
      {mensaje && <p className="mensaje-ok">{mensaje}</p>}
      {error && <p className="mensaje-error">{error}</p>}

      <section className="bloque">
        <div className="titulo-bloque">
          <h2>Órdenes de lavado</h2>
          <span className="contador">{ordenes.length} órdenes</span>
        </div>
        <TablaOrdenes ordenes={ordenes} alAvanzar={avanzar} />
      </section>

      <section className="bloque">
        <h2>Registrar orden de lavado</h2>
        <FormularioOrden
          vehiculos={vehiculos}
          servicios={servicios}
          alGuardar={registrar}
        />
      </section>
    </>
  );
}
