import { useEffect, useState } from "react";
import { api } from "../servicios/api.js";
import TablaClientes from "../componentes/TablaClientes.jsx";
import FormularioCliente from "../componentes/FormularioCliente.jsx";

/**
 * Módulo de gestión de clientes.
 */
export default function Clientes() {
  const [clientes, setClientes] = useState([]);
  const [error, setError] = useState("");
  const [mensaje, setMensaje] = useState("");

  useEffect(() => {
    cargar();
  }, []);

  async function cargar() {
    try {
      setClientes(await api.clientes());
    } catch (fallo) {
      setError(fallo.message);
    }
  }

  async function guardar(cliente) {
    setError("");
    setMensaje("");
    try {
      await api.crearCliente(cliente);
      setMensaje("Cliente registrado correctamente.");
      await cargar();
    } catch (fallo) {
      setError(fallo.message);
      throw fallo;
    }
  }

  async function eliminar(cliente) {
    if (!window.confirm(`¿Eliminar el cliente ${cliente.nombre}?`)) {
      return;
    }
    setError("");
    setMensaje("");
    try {
      await api.eliminarCliente(cliente.idCliente);
      setMensaje("Cliente eliminado.");
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
          <h2>Clientes registrados</h2>
          <span className="contador">{clientes.length} clientes</span>
        </div>
        <TablaClientes clientes={clientes} alEliminar={eliminar} />
      </section>

      <section className="bloque">
        <h2>Registrar cliente</h2>
        <FormularioCliente alGuardar={guardar} />
      </section>
    </>
  );
}
