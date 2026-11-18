import { useState } from "react";
import Boton from "./Boton.jsx";

const VACIO = { vehiculo: "", servicio: "", operario: "2", observaciones: "" };

/**
 * Formulario para registrar una orden de lavado.
 */
export default function FormularioOrden({ vehiculos, servicios, alGuardar }) {
  const [datos, setDatos] = useState(VACIO);
  const [enviando, setEnviando] = useState(false);

  function cambiar(campo, valor) {
    setDatos((previos) => ({ ...previos, [campo]: valor }));
  }

  async function manejarEnvio(evento) {
    evento.preventDefault();
    setEnviando(true);
    try {
      await alGuardar({
        vehiculo: Number(datos.vehiculo),
        servicio: Number(datos.servicio),
        operario: Number(datos.operario),
        observaciones: datos.observaciones.trim()
      });
      setDatos(VACIO);
    } finally {
      setEnviando(false);
    }
  }

  return (
    <form className="formulario" onSubmit={manejarEnvio}>
      <div className="campo">
        <label htmlFor="vehiculo">Vehículo</label>
        <select
          id="vehiculo"
          value={datos.vehiculo}
          onChange={(evento) => cambiar("vehiculo", evento.target.value)}
          required
        >
          <option value="">Seleccione un vehículo</option>
          {vehiculos.map((vehiculo) => (
            <option key={vehiculo.idVehiculo} value={vehiculo.idVehiculo}>
              {vehiculo.placa} - {vehiculo.marca} {vehiculo.modelo}
            </option>
          ))}
        </select>
      </div>

      <div className="campo">
        <label htmlFor="servicio">Servicio</label>
        <select
          id="servicio"
          value={datos.servicio}
          onChange={(evento) => cambiar("servicio", evento.target.value)}
          required
        >
          <option value="">Seleccione un servicio</option>
          {servicios.map((servicio) => (
            <option key={servicio.idServicio} value={servicio.idServicio}>
              {servicio.nombre} - ${Number(servicio.precio).toLocaleString("es-CO")}
            </option>
          ))}
        </select>
      </div>

      <div className="campo">
        <label htmlFor="operario">Operario</label>
        <select
          id="operario"
          value={datos.operario}
          onChange={(evento) => cambiar("operario", evento.target.value)}
          required
        >
          <option value="1">Administrador</option>
          <option value="2">Juan Pérez</option>
          <option value="3">Camilo Ríos</option>
        </select>
      </div>

      <div className="campo campo-amplio">
        <label htmlFor="observaciones">Observaciones</label>
        <input
          id="observaciones"
          type="text"
          value={datos.observaciones}
          onChange={(evento) => cambiar("observaciones", evento.target.value)}
          maxLength={200}
          placeholder="Detalles del vehículo o del servicio"
        />
      </div>

      <Boton tipo="submit" bloqueado={enviando}>
        {enviando ? "Registrando..." : "Registrar orden"}
      </Boton>
    </form>
  );
}
