import { useState } from "react";
import Login from "./paginas/Login.jsx";
import Panel from "./paginas/Panel.jsx";
import Clientes from "./paginas/Clientes.jsx";
import Ordenes from "./paginas/Ordenes.jsx";
import Reportes from "./paginas/Reportes.jsx";
import BarraLateral from "./componentes/BarraLateral.jsx";
import Encabezado from "./componentes/Encabezado.jsx";

const SECCIONES = {
  panel: {
    titulo: "Panel principal",
    descripcion: "Indicadores generales de la operación del lavadero"
  },
  clientes: {
    titulo: "Clientes",
    descripcion: "Registro y consulta de los clientes del lavadero"
  },
  ordenes: {
    titulo: "Órdenes de lavado",
    descripcion: "Entrada, proceso y entrega de los vehículos"
  },
  reportes: {
    titulo: "Reportes",
    descripcion: "Ingresos y lavados por tipo de servicio"
  }
};

export default function App() {
  const [usuario, setUsuario] = useState(() => {
    const guardado = sessionStorage.getItem("aqualavado_usuario");
    return guardado ? JSON.parse(guardado) : null;
  });
  const [seccion, setSeccion] = useState("panel");

  function ingresar(datos) {
    sessionStorage.setItem("aqualavado_usuario", JSON.stringify(datos));
    setUsuario(datos);
  }

  function cerrarSesion() {
    sessionStorage.removeItem("aqualavado_usuario");
    setUsuario(null);
    setSeccion("panel");
  }

  if (!usuario) {
    return <Login alIngresar={ingresar} />;
  }

  const actual = SECCIONES[seccion];

  return (
    <div className="contenedor">
      <BarraLateral
        seccion={seccion}
        alCambiar={setSeccion}
        usuario={usuario}
        alCerrarSesion={cerrarSesion}
      />

      <main className="contenido">
        <Encabezado titulo={actual.titulo} descripcion={actual.descripcion} />
        {seccion === "panel" && <Panel alNavegar={setSeccion} />}
        {seccion === "clientes" && <Clientes />}
        {seccion === "ordenes" && <Ordenes />}
        {seccion === "reportes" && <Reportes />}
      </main>
    </div>
  );
}
