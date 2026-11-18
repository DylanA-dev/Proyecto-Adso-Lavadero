import { useState } from "react";
import { api } from "../servicios/api.js";
import Boton from "../componentes/Boton.jsx";

/**
 * Pantalla de acceso al sistema.
 */
export default function Login({ alIngresar }) {
  const [correo, setCorreo] = useState("admin@aqualavado.com");
  const [clave, setClave] = useState("");
  const [error, setError] = useState("");
  const [cargando, setCargando] = useState(false);

  async function manejarEnvio(evento) {
    evento.preventDefault();
    setError("");
    setCargando(true);
    try {
      const respuesta = await api.login(correo.trim(), clave);
      alIngresar(respuesta.usuario);
    } catch (fallo) {
      setError(fallo.message);
    } finally {
      setCargando(false);
    }
  }

  return (
    <main className="pantalla-login">
      <section className="tarjeta-login">
        <div className="marca">
          <span className="logo">AQUA</span>
          <span className="logo-acento">LAVADO</span>
          <p>Sistema de gestión de lavadero de vehículos</p>
        </div>

        <form onSubmit={manejarEnvio}>
          <label htmlFor="correo">Correo electrónico</label>
          <input
            id="correo"
            type="email"
            value={correo}
            onChange={(evento) => setCorreo(evento.target.value)}
            required
            autoComplete="username"
          />

          <label htmlFor="clave">Contraseña</label>
          <input
            id="clave"
            type="password"
            value={clave}
            onChange={(evento) => setClave(evento.target.value)}
            minLength={6}
            required
            autoComplete="current-password"
            placeholder="Ingrese su contraseña"
          />

          <Boton tipo="submit" variante="principal" bloqueado={cargando}>
            {cargando ? "Validando..." : "Ingresar"}
          </Boton>
        </form>

        {error && <p className="mensaje-error">{error}</p>}

        <p className="pie-login">
          El servicio se presta en las instalaciones del lavadero.
        </p>
      </section>
    </main>
  );
}
