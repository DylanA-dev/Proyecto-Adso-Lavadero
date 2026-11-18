import { useState } from "react";
import Boton from "./Boton.jsx";

const VACIO = {
  documento: "",
  nombre: "",
  telefono: "",
  correo: "",
  direccion: ""
};

/**
 * Formulario de registro de clientes con validación de datos.
 */
export default function FormularioCliente({ alGuardar }) {
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
        ...datos,
        documento: datos.documento.trim(),
        nombre: datos.nombre.trim(),
        telefono: datos.telefono.trim(),
        correo: datos.correo.trim(),
        direccion: datos.direccion.trim()
      });
      setDatos(VACIO);
    } finally {
      setEnviando(false);
    }
  }

  return (
    <form className="formulario" onSubmit={manejarEnvio}>
      <div className="campo">
        <label htmlFor="documento">Documento</label>
        <input
          id="documento"
          type="text"
          value={datos.documento}
          onChange={(evento) => cambiar("documento", evento.target.value)}
          required
          pattern="[0-9]{6,15}"
          maxLength={15}
          title="Entre 6 y 15 dígitos"
        />
      </div>

      <div className="campo">
        <label htmlFor="nombre">Nombre completo</label>
        <input
          id="nombre"
          type="text"
          value={datos.nombre}
          onChange={(evento) => cambiar("nombre", evento.target.value)}
          required
          maxLength={80}
        />
      </div>

      <div className="campo">
        <label htmlFor="telefono">Teléfono</label>
        <input
          id="telefono"
          type="tel"
          value={datos.telefono}
          onChange={(evento) => cambiar("telefono", evento.target.value)}
          required
          pattern="[0-9]{7,15}"
          maxLength={15}
          title="Entre 7 y 15 dígitos"
        />
      </div>

      <div className="campo">
        <label htmlFor="correo">Correo</label>
        <input
          id="correo"
          type="email"
          value={datos.correo}
          onChange={(evento) => cambiar("correo", evento.target.value)}
          maxLength={100}
        />
      </div>

      <div className="campo campo-amplio">
        <label htmlFor="direccion">Dirección</label>
        <input
          id="direccion"
          type="text"
          value={datos.direccion}
          onChange={(evento) => cambiar("direccion", evento.target.value)}
          maxLength={120}
        />
      </div>

      <Boton tipo="submit" bloqueado={enviando}>
        {enviando ? "Guardando..." : "Guardar cliente"}
      </Boton>
    </form>
  );
}
