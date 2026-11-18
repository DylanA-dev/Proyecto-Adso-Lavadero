# -*- coding: utf-8 -*-
"""Documentos de la actividad GA7-220501096-AA4 (front-end con React)."""
import sys

from sena_doc import SenaDoc

FECHA = "Noviembre 2026"
REPO = "https://github.com/DylanA-dev/Proyecto-Adso-Lavadero"
CAPTURAS = r"C:\Users\dylan\Documents\OpenCode\ADSO\proyectos\lavadero\interfaz\capturas"


def ev01():
    d = SenaDoc(
        "GA7-220501096-AA4-EV01",
        "Taller sobre componentes front-end",
        FECHA,
    )
    d.intro([
        "React es una biblioteca de JavaScript para construir interfaces de usuario a "
        "partir de componentes reutilizables. Su modelo de programación declara cómo debe "
        "verse la interfaz para un estado determinado y la biblioteca se encarga de "
        "actualizar el DOM de forma eficiente cuando ese estado cambia.",
        "En este taller se desarrollan los aspectos solicitados por la guía: la diferencia "
        "entre React y JSX, el concepto de clases en React, los principales eventos de la "
        "biblioteca y un mapa conceptual que organiza sus elementos centrales. Los "
        "conceptos se ilustran con ejemplos aplicados al sistema AquaLavado.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Reconocer las características principales de React y JSX, el uso de clases y "
        "eventos, y organizar conceptualmente los elementos del framework mediante un mapa "
        "conceptual aplicado al proyecto AquaLavado.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Establecer la diferencia entre React y JSX con ejemplos de código.",
        "Explicar qué son las clases en React y cómo se relacionan con los componentes.",
        "Identificar los eventos principales y su sintaxis en React.",
        "Elaborar un mapa conceptual con los conceptos centrales de la biblioteca.",
        "Relacionar los conceptos con los componentes del proyecto AquaLavado.",
    ])

    d.h2("2. Diferencia entre React y JSX")
    d.p("**React** es la biblioteca que administra los componentes, el estado, las props y "
        "el renderizado de la interfaz. **JSX** es una extensión de la sintaxis de "
        "JavaScript que permite escribir estructuras similares a HTML dentro del código y "
        "que se transforma en llamadas a funciones de React antes de ejecutarse en el "
        "navegador.")
    d.p("JSX no es obligatorio para usar React, pero facilita la lectura del código y la "
        "composición de la interfaz. Un archivo JSX debe ser procesado por una herramienta "
        "como Babel o Vite, que convierte las etiquetas en llamadas a React.createElement.")
    d.tabla(
        ["Criterio", "React", "JSX"],
        [
            ["Naturaleza", "Biblioteca de JavaScript para interfaces.", "Extensión de sintaxis de JavaScript."],
            ["Función", "Gestiona componentes, estado y renderizado.", "Describe la estructura visual del componente."],
            ["Sintaxis", "JavaScript puro con funciones y objetos.", "Etiquetas similares a HTML dentro de JavaScript."],
            ["Procesamiento", "Se ejecuta directamente en el navegador.", "Requiere transpilación (Babel o Vite)."],
            ["Expresiones", "Se usan funciones y variables.", "Se insertan expresiones con llaves: {valor}."],
            ["Atributos", "Objetos con propiedades.", "Atributos HTML adaptados: className, htmlFor."],
            ["Ejemplo", "React.createElement('h1', null, 'Hola')", "<h1>Hola</h1>"],
        ],
        anchos=[2.8, 6.4, 6.4],
        caption="Diferencias entre React y JSX.",
        size=7.5,
    )
    d.codigo(
        "// JSX: estructura declarativa del componente\n"
        "function EstadoOrden({ estado }) {\n"
        "  return <span className=\"estado\">{estado}</span>;\n"
        "}\n"
        "\n"
        "// Equivalente sin JSX\n"
        "function EstadoOrden({ estado }) {\n"
        "  return React.createElement(\"span\", { className: \"estado\" }, estado);\n"
        "}")

    d.h2("3. ¿Qué son clases en React?")
    d.p("Las clases en React son componentes definidos con una clase de JavaScript que "
        "extiende React.Component. Antes de la llegada de los hooks, las clases eran la "
        "forma de manejar el estado local y los eventos del ciclo de vida mediante "
        "this.state, this.setState y métodos como componentDidMount.")
    d.p("Un componente de clase debe implementar el método render, que devuelve el JSX que "
        "se mostrará en pantalla. El estado se inicializa en el constructor y se actualiza "
        "con setState, lo que provoca un nuevo renderizado del componente.")
    d.codigo(
        "import React, { Component } from \"react\";\n"
        "\n"
        "class ContadorOrdenes extends Component {\n"
        "  constructor(props) {\n"
        "    super(props);\n"
        "    this.state = { total: 0 };\n"
        "  }\n"
        "\n"
        "  componentDidMount() {\n"
        "    this.setState({ total: this.props.inicial });\n"
        "  }\n"
        "\n"
        "  incrementar = () => {\n"
        "    this.setState({ total: this.state.total + 1 });\n"
        "  };\n"
        "\n"
        "  render() {\n"
        "    return (\n"
        "      <div>\n"
        "        <p>Órdenes registradas: {this.state.total}</p>\n"
        "        <button onClick={this.incrementar}>Agregar</button>\n"
        "      </div>\n"
        "    );\n"
        "  }\n"
        "}")
    d.p("En el proyecto AquaLavado los componentes se implementaron como funciones con "
        "hooks, que es el enfoque recomendado por la documentación actual de React. La "
        "siguiente tabla compara ambos estilos.")
    d.tabla(
        ["Aspecto", "Componente de clase", "Componente de función con hooks"],
        [
            ["Declaración", "class MiComponente extends Component", "function MiComponente()"],
            ["Estado", "this.state y this.setState", "useState"],
            ["Ciclo de vida", "componentDidMount, componentDidUpdate", "useEffect"],
            ["Contexto", "this.context", "useContext"],
            ["Código", "Más extenso y con this", "Más corto y sin this"],
            ["Recomendación actual", "Mantenimiento de código antiguo", "Código nuevo"],
        ],
        anchos=[3.4, 6.2, 6.2],
        caption="Comparación entre clases y funciones en React.",
        size=7.5,
    )

    d.h2("4. Principales eventos de React")
    d.p("React utiliza eventos sintéticos que envuelven los eventos nativos del navegador "
        "para garantizar un comportamiento uniforme. Los manejadores se escriben en "
        "camelCase y se asignan como funciones, no como cadenas de texto; además, reciben "
        "un objeto de evento con métodos como preventDefault y stopPropagation.")
    d.tabla(
        ["Evento", "Cuándo se produce", "Ejemplo de uso"],
        [
            ["onClick", "Al hacer clic sobre un elemento.", "<button onClick={manejarClic}>"],
            ["onChange", "Al cambiar el valor de un campo o una lista.", "<input onChange={manejarCambio} />"],
            ["onSubmit", "Al enviar un formulario.", "<form onSubmit={manejarEnvio}>"],
            ["onFocus", "Cuando un campo recibe el foco.", "<input onFocus={manejarFoco} />"],
            ["onBlur", "Cuando un campo pierde el foco.", "<input onBlur={validarCampo} />"],
            ["onKeyDown", "Al presionar una tecla.", "<input onKeyDown={manejarTecla} />"],
            ["onMouseEnter", "Al pasar el puntero sobre un elemento.", "<div onMouseEnter={resaltar}>"],
            ["onDoubleClick", "Al hacer doble clic.", "<tr onDoubleClick={abrirDetalle}>"],
        ],
        anchos=[3.0, 7.4, 5.2],
        caption="Eventos principales de React.",
        size=7.5,
    )
    d.codigo(
        "function FormularioOrden({ alGuardar }) {\n"
        "  const [vehiculo, setVehiculo] = useState(\"\");\n"
        "\n"
        "  function manejarEnvio(evento) {\n"
        "    evento.preventDefault();\n"
        "    alGuardar({ vehiculo: Number(vehiculo) });\n"
        "  }\n"
        "\n"
        "  return (\n"
        "    <form onSubmit={manejarEnvio}>\n"
        "      <select value={vehiculo} onChange={(e) => setVehiculo(e.target.value)}>\n"
        "        <option value=\"\">Seleccione un vehículo</option>\n"
        "      </select>\n"
        "      <button type=\"submit\">Registrar orden</button>\n"
        "    </form>\n"
        "  );\n"
        "}")

    d.h2("5. Mapa conceptual de React")
    d.p("El mapa organiza los conceptos centrales de React y su relación con la "
        "construcción de interfaces: componentes, JSX, props, estado, eventos, hooks, "
        "ciclo de vida y renderizado.")
    d.imagen(f"{CAPTURAS}\\mapa_react.png",
             "Mapa conceptual de React.", 15.5)

    d.h2("6. Características principales del framework")
    d.bullets([
        "**Componentes:** la interfaz se divide en piezas independientes y reutilizables.",
        "**Props:** permiten pasar datos de un componente padre a un componente hijo.",
        "**Estado:** almacena los datos que cambian durante la ejecución y provocan un nuevo renderizado.",
        "**Hooks:** funciones como useState y useEffect permiten usar estado y ciclo de vida en componentes de función.",
        "**JSX:** sintaxis declarativa que facilita la lectura de la estructura visual.",
        "**DOM virtual:** React compara el árbol anterior con el nuevo y actualiza solo los cambios necesarios.",
        "**Flujo unidireccional:** los datos descienden del componente padre al hijo, lo que facilita el control del estado.",
        "**Ecosistema:** herramientas como Vite, React Router y las pruebas con Jest complementan el desarrollo.",
    ])

    d.h2("7. Aplicación en el proyecto AquaLavado")
    d.p("En AquaLavado los componentes se organizan por dominio: componentes comunes "
        "(Boton, EstadoOrden, TarjetaIndicador), componentes de clientes (TablaClientes, "
        "FormularioCliente) y componentes de órdenes (TablaOrdenes, FormularioOrden). La "
        "aplicación principal conserva el usuario y la sección activa, y las páginas "
        "consumen la API mediante un módulo de servicios.")
    d.p("Esta organización aplica los conceptos del taller: los componentes reciben props, "
        "manejan estado local con useState, atienden eventos con onChange y onSubmit, y "
        "utilizan useEffect para cargar la información al abrir cada sección.")

    d.conclusion([
        "El taller permitió diferenciar React de JSX y comprender que la biblioteca "
        "administra el estado y el renderizado, mientras JSX ofrece una sintaxis declarativa "
        "para describir la interfaz. También se reconocieron las clases como el mecanismo "
        "anterior a los hooks y los eventos sintéticos como la forma de responder a las "
        "acciones del usuario.",
        "El mapa conceptual y los ejemplos aplicados a AquaLavado consolidan una base "
        "conceptual para la codificación del front-end y facilitan la lectura de los "
        "componentes desarrollados en la evidencia AA4-EV03.",
    ])

    d.bibliografia([
        "React. (2025). React documentation. https://react.dev",
        "React. (2025). Writing markup with JSX. https://react.dev/learn/writing-markup-with-jsx",
        "React. (2025). Responding to events. https://react.dev/learn/responding-to-events",
        "React. (2025). React.Component. https://react.dev/reference/react/Component",
        "MDN Web Docs. (2025). JavaScript. https://developer.mozilla.org/es/docs/Web/JavaScript",
    ])
    return d.guardar()


def ev02():
    d = SenaDoc(
        "GA7-220501096-AA4-EV02",
        "Verificación de procedimientos para la definición de componentes front-end de la aplicación",
        FECHA,
    )
    d.intro([
        "La definición de los componentes front-end determina la forma en que la interfaz "
        "se organiza, se reutiliza y se mantiene. Para el sistema AquaLavado se "
        "seleccionaron componentes que representan las entidades y las acciones del "
        "negocio, con responsabilidades delimitadas y una comunicación clara mediante "
        "props y eventos.",
        "En esta evidencia se describen los componentes de React utilizados en la "
        "aplicación, su responsabilidad, las props que reciben, el estado que administran "
        "y la justificación de su selección. La definición toma como base los prototipos, "
        "las historias de usuario y el diseño de la interfaz elaborados previamente.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Definir y justificar los componentes de React que conforman el front-end del "
        "sistema AquaLavado, estableciendo su responsabilidad, sus props, su estado y su "
        "relación con los requisitos del proyecto.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Identificar los componentes necesarios para cubrir las historias de usuario.",
        "Delimitar la responsabilidad de cada componente.",
        "Definir las props y el estado de cada uno.",
        "Justificar la selección y la reutilización de los componentes.",
        "Establecer criterios de composición, accesibilidad y diseño responsivo.",
    ])

    d.h2("2. Criterios de selección")
    d.p("Los componentes se definieron con los siguientes criterios: una sola "
        "responsabilidad por componente, reutilización en más de una vista cuando sea "
        "posible, separación entre la presentación y el acceso a datos, comunicación "
        "mediante props y eventos, y adaptación a pantallas pequeñas.")
    d.tabla(
        ["Criterio", "Aplicación en el proyecto"],
        [
            ["Responsabilidad única", "Cada componente realiza una tarea: mostrar una tabla, capturar un formulario o presentar un indicador."],
            ["Reutilización", "Boton, EstadoOrden y TarjetaIndicador se usan en varias páginas."],
            ["Composición", "Las páginas combinan componentes pequeños en lugar de concentrar toda la lógica."],
            ["Separación de datos", "Las llamadas a la API se centralizan en servicios/api.js."],
            ["Accesibilidad", "Los formularios asocian etiquetas con campos y los botones tienen texto descriptivo."],
            ["Responsividad", "El menú, las tarjetas y las tablas se adaptan a teléfonos y tabletas."],
        ],
        anchos=[4.0, 11.6],
        caption="Criterios para la definición de componentes.",
    )

    d.h2("3. Arquitectura de componentes")
    d.p("La aplicación se organiza en tres niveles: el componente raíz, las páginas y los "
        "componentes de presentación. El componente raíz conserva la sesión y la sección "
        "activa; las páginas cargan los datos y componen la vista; los componentes de "
        "presentación reciben props y notifican eventos.")
    d.codigo(
        "App\n"
        "├── Login\n"
        "├── BarraLateral\n"
        "├── Encabezado\n"
        "├── Panel\n"
        "│   ├── TarjetaIndicador\n"
        "│   └── TablaOrdenes (compacta)\n"
        "├── Clientes\n"
        "│   ├── TablaClientes\n"
        "│   └── FormularioCliente\n"
        "├── Ordenes\n"
        "│   ├── TablaOrdenes\n"
        "│   ├── EstadoOrden\n"
        "│   └── FormularioOrden\n"
        "└── Reportes\n"
        "    └── TarjetaIndicador")

    d.h2("4. Componentes definidos")
    d.tabla(
        ["Componente", "Responsabilidad", "Props / estado", "Justificación"],
        [
            ["App", "Conservar la sesión y la sección activa.", "usuario, seccion (estado).", "Centraliza la navegación y evita repetir la lógica en cada página."],
            ["Login", "Capturar y validar las credenciales.", "alIngresar (prop); correo, clave, error (estado).", "Aísla el acceso y reutiliza el servicio de autenticación."],
            ["BarraLateral", "Permitir la navegación entre módulos.", "seccion, usuario, alCambiar, alCerrarSesion.", "Se reutiliza en todas las páginas y se adapta a móvil."],
            ["Encabezado", "Mostrar el título y la descripción de la sección.", "titulo, descripcion.", "Evita duplicar el mismo bloque en cada vista."],
            ["TarjetaIndicador", "Presentar un indicador con su detalle.", "etiqueta, valor, detalle.", "Se reutiliza en el panel y en los reportes."],
            ["EstadoOrden", "Mostrar el estado con un color distintivo.", "estado.", "Unifica la presentación de los estados y su semántica visual."],
            ["TablaOrdenes", "Listar órdenes y permitir avanzar su estado.", "ordenes, alAvanzar, compacta.", "Se usa en el panel y en el módulo de órdenes con dos configuraciones."],
            ["FormularioOrden", "Capturar los datos de una nueva orden.", "vehiculos, servicios, alGuardar; datos (estado).", "Concentra la validación y el envío de la orden."],
            ["TablaClientes", "Listar clientes y permitir su eliminación.", "clientes, alEliminar.", "Presenta la información y delega la acción al contenedor."],
            ["FormularioCliente", "Capturar los datos de un cliente.", "alGuardar; datos (estado).", "Aplica las validaciones de documento, teléfono y correo."],
            ["Boton", "Presentar acciones con variantes visuales.", "children, tipo, variante, bloqueado, alHacerClic.", "Unifica el estilo y el comportamiento de los botones."],
        ],
        anchos=[2.9, 4.8, 4.4, 3.5],
        caption="Componentes del front-end de AquaLavado.",
        size=7,
    )

    d.h2("5. Descripción de los componentes principales")
    d.h3("App")
    d.p("Es el componente raíz. Recupera el usuario de sessionStorage, controla la sección "
        "activa y decide si muestra el inicio de sesión o la aplicación. Su función es "
        "mantener el estado global mínimo y delegar la lógica a las páginas.")
    d.h3("BarraLateral")
    d.p("Presenta el menú de navegación y la información del usuario. En pantallas "
        "grandes se muestra como una barra lateral fija; en pantallas pequeñas se convierte "
        "en una barra inferior con las cuatro secciones principales. Recibe la sección "
        "activa y las funciones para cambiarla y cerrar la sesión.")
    d.h3("Panel")
    d.p("Consulta el resumen y las órdenes mediante la API y compone las tarjetas de "
        "indicadores con la tabla de últimas órdenes. Es el punto de entrada después del "
        "inicio de sesión y ofrece el acceso directo al registro de una orden.")
    d.h3("TablaOrdenes")
    d.p("Recibe la lista de órdenes y la función para avanzar de estado. Admite una "
        "variante compacta para el panel, en la que se ocultan columnas secundarias. "
        "Presenta el estado mediante el componente EstadoOrden y desactiva la acción "
        "cuando la orden ya fue entregada.")
    d.h3("FormularioOrden")
    d.p("Captura el vehículo, el servicio, el operario y las observaciones. Mantiene el "
        "estado local del formulario, valida la selección obligatoria y envía los datos al "
        "componente contenedor, que se encarga de llamar a la API y recargar la lista.")
    d.h3("FormularioCliente y TablaClientes")
    d.p("El formulario aplica patrones numéricos para el documento y el teléfono, longitudes "
        "máximas y validación del correo. La tabla presenta los clientes y solicita "
        "confirmación antes de eliminar un registro.")
    d.h3("EstadoOrden")
    d.p("Traduce el código del estado a una etiqueta legible y aplica una clase de color "
        "según la etapa del lavado. Se reutiliza en todas las tablas y facilita la lectura "
        "rápida del proceso.")

    d.h2("6. Composición y reutilización")
    d.p("La composición permite construir vistas complejas a partir de componentes "
        "pequeños. Por ejemplo, la página de órdenes combina el formulario, la tabla, la "
        "etiqueta de estado y el botón; el panel reutiliza la tabla en modo compacto y la "
        "tarjeta de indicador. De esta forma se evita duplicar código y se mantiene un "
        "único estilo visual.")
    d.tabla(
        ["Componente reutilizado", "Lugares de uso"],
        [
            ["Boton", "Inicio de sesión, panel, clientes, órdenes y formularios."],
            ["TarjetaIndicador", "Panel principal y reportes."],
            ["TablaOrdenes", "Panel principal y módulo de órdenes."],
            ["EstadoOrden", "Tabla de órdenes del panel y del módulo de órdenes."],
            ["Encabezado", "Todas las secciones internas."],
        ],
        anchos=[4.6, 11.0],
        caption="Reutilización de componentes.",
    )

    d.h2("7. Accesibilidad y diseño responsivo")
    d.bullets([
        "Cada campo de formulario tiene una etiqueta asociada mediante htmlFor e id.",
        "Los botones incluyen texto descriptivo y no dependen solo del color.",
        "Los estados se acompañan de texto, además del color.",
        "El contraste entre texto y fondo cumple con una lectura clara.",
        "La navegación se adapta a teclado y a pantallas táctiles.",
        "Las tablas permiten desplazamiento horizontal en pantallas pequeñas.",
        "El menú inferior de la versión móvil mantiene las acciones principales al alcance.",
    ])

    d.conclusion([
        "La definición de componentes permitió organizar el front-end de AquaLavado en "
        "piezas con responsabilidades claras, comunicadas mediante props y eventos. La "
        "reutilización de Boton, TarjetaIndicador, TablaOrdenes y EstadoOrden reduce la "
        "duplicación y mantiene la consistencia visual.",
        "Los criterios de composición, accesibilidad y diseño responsivo orientan la "
        "codificación del front-end y aseguran que la interfaz pueda adaptarse a los "
        "diferentes dispositivos desde los que se opera el lavadero.",
    ])

    d.bibliografia([
        "React. (2025). React documentation. https://react.dev",
        "React. (2025). Passing props to a component. https://react.dev/learn/passing-props-to-a-component",
        "React. (2025). Sharing state between components. https://react.dev/learn/sharing-state-between-components",
        "MDN Web Docs. (2025). Accessibility. https://developer.mozilla.org/es/docs/Web/Accessibility",
        "W3C. (2023). Web content accessibility guidelines (WCAG) 2.2. https://www.w3.org/TR/WCAG22/",
    ])
    return d.guardar()


def ev03():
    d = SenaDoc(
        "GA7-220501096-AA4-EV03",
        "Componente front-end del proyecto formativo y proyectos de clase",
        FECHA,
    )
    d.intro([
        "El front-end de AquaLavado se implementó con React y Vite, organizado en "
        "componentes reutilizables que consumen la API REST del sistema. La aplicación "
        "incluye el inicio de sesión, el panel de indicadores, la gestión de clientes, el "
        "registro y control de órdenes y los reportes, con una interfaz adaptada a "
        "computador y teléfono.",
        "En esta evidencia se presenta la codificación del componente front-end: la "
        "estructura del proyecto, la configuración, los componentes principales, el "
        "consumo de los servicios, la configuración como aplicación web progresiva y las "
        "capturas de las pantallas en funcionamiento.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Codificar el componente front-end del proyecto AquaLavado con React, aplicando "
        "los estándares de codificación, el consumo de servicios web y los criterios de "
        "diseño responsivo definidos para el sistema.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Implementar los componentes y las páginas del sistema con React.",
        "Consumir los servicios de la API mediante un módulo centralizado.",
        "Aplicar los estilos y el diseño responsivo definidos en el proyecto.",
        "Configurar la aplicación como PWA instalable.",
        "Verificar la compilación y el funcionamiento de las vistas.",
        "Versionar el código y preparar la entrega del proyecto.",
    ])

    d.h2("2. Estructura del proyecto")
    d.codigo(
        "frontend-react/\n"
        "├── public/\n"
        "│   ├── icono.svg\n"
        "│   ├── manifest.webmanifest\n"
        "│   └── sw.js\n"
        "├── src/\n"
        "│   ├── componentes/\n"
        "│   │   ├── BarraLateral.jsx\n"
        "│   │   ├── Boton.jsx\n"
        "│   │   ├── Encabezado.jsx\n"
        "│   │   ├── EstadoOrden.jsx\n"
        "│   │   ├── FormularioCliente.jsx\n"
        "│   │   ├── FormularioOrden.jsx\n"
        "│   │   ├── TablaClientes.jsx\n"
        "│   │   ├── TablaOrdenes.jsx\n"
        "│   │   └── TarjetaIndicador.jsx\n"
        "│   ├── paginas/\n"
        "│   │   ├── Login.jsx\n"
        "│   │   ├── Panel.jsx\n"
        "│   │   ├── Clientes.jsx\n"
        "│   │   ├── Ordenes.jsx\n"
        "│   │   └── Reportes.jsx\n"
        "│   ├── servicios/api.js\n"
        "│   ├── App.jsx\n"
        "│   ├── main.jsx\n"
        "│   └── estilos.css\n"
        "├── index.html\n"
        "├── package.json\n"
        "└── vite.config.js")

    d.h2("3. Configuración del proyecto")
    d.p("El proyecto utiliza Vite como herramienta de desarrollo y empaquetado. La "
        "configuración define el puerto de desarrollo y un proxy hacia la API para evitar "
        "problemas de origen durante las pruebas locales.")
    d.codigo(
        "export default defineConfig({\n"
        "  plugins: [react()],\n"
        "  server: {\n"
        "    port: 5173,\n"
        "    proxy: {\n"
        "      \"/api\": { target: \"http://localhost:8081\", changeOrigin: true }\n"
        "    }\n"
        "  }\n"
        "});")
    d.p("Las dependencias principales son React 18 y React DOM; las de desarrollo son Vite "
        "y el plugin de React. Los scripts permiten iniciar el servidor, compilar para "
        "producción y previsualizar el resultado.")

    d.h2("4. Componentes implementados")
    d.h3("4.1 Componente raíz")
    d.p("App conserva el usuario y la sección activa, muestra el inicio de sesión cuando no "
        "hay usuario y compone la barra lateral, el encabezado y la página seleccionada.")
    d.codigo(
        "export default function App() {\n"
        "  const [usuario, setUsuario] = useState(() => {\n"
        "    const guardado = sessionStorage.getItem(\"aqualavado_usuario\");\n"
        "    return guardado ? JSON.parse(guardado) : null;\n"
        "  });\n"
        "  const [seccion, setSeccion] = useState(\"panel\");\n"
        "\n"
        "  if (!usuario) {\n"
        "    return <Login alIngresar={ingresar} />;\n"
        "  }\n"
        "\n"
        "  return (\n"
        "    <div className=\"contenedor\">\n"
        "      <BarraLateral seccion={seccion} alCambiar={setSeccion}\n"
        "                    usuario={usuario} alCerrarSesion={cerrarSesion} />\n"
        "      <main className=\"contenido\">\n"
        "        <Encabezado titulo={actual.titulo} descripcion={actual.descripcion} />\n"
        "        {seccion === \"panel\" && <Panel alNavegar={setSeccion} />}\n"
        "        {seccion === \"clientes\" && <Clientes />}\n"
        "        {seccion === \"ordenes\" && <Ordenes />}\n"
        "        {seccion === \"reportes\" && <Reportes />}\n"
        "      </main>\n"
        "    </div>\n"
        "  );\n"
        "}")
    d.h3("4.2 Tabla de órdenes")
    d.p("TablaOrdenes recibe la lista de órdenes y la acción para avanzar de estado. La "
        "prop compacta permite reutilizarla en el panel con menos columnas.")
    d.codigo(
        "export default function TablaOrdenes({ ordenes, alAvanzar, compacta = false }) {\n"
        "  return (\n"
        "    <div className=\"tabla-contenedor\">\n"
        "      <table className={`tabla tabla-ajustada${compacta ? \" tabla-compacta\" : \"\"}`}>\n"
        "        <thead>\n"
        "          <tr>\n"
        "            <th>Orden</th><th>Placa</th><th>Servicio</th><th>Operario</th>\n"
        "            {!compacta && <th>Ingreso</th>}\n"
        "            <th>Estado</th><th>Valor</th>\n"
        "            {!compacta && <th>Acción</th>}\n"
        "          </tr>\n"
        "        </thead>\n"
        "        <tbody>\n"
        "          {ordenes.map((orden) => (\n"
        "            <tr key={orden.idOrden}>\n"
        "              <td>{orden.idOrden}</td>\n"
        "              <td>{orden.placa}</td>\n"
        "              <td className=\"col-opcional\">{orden.nombreServicio}</td>\n"
        "              <td className=\"col-opcional\">{orden.nombreOperario}</td>\n"
        "              {!compacta && <td>{formatearFecha(orden.fechaIngreso)}</td>}\n"
        "              <td><EstadoOrden estado={orden.estado} /></td>\n"
        "              <td>{formatearPeso(orden.valor)}</td>\n"
        "              {!compacta && <td>{accion}</td>}\n"
        "            </tr>\n"
        "          ))}\n"
        "        </tbody>\n"
        "      </table>\n"
        "    </div>\n"
        "  );\n"
        "}")
    d.h3("4.3 Formulario de orden")
    d.p("El formulario administra su estado local, valida la selección y entrega los datos "
        "al componente contenedor mediante la prop alGuardar.")
    d.codigo(
        "const [datos, setDatos] = useState(VACIO);\n"
        "\n"
        "async function manejarEnvio(evento) {\n"
        "  evento.preventDefault();\n"
        "  setEnviando(true);\n"
        "  try {\n"
        "    await alGuardar({\n"
        "      vehiculo: Number(datos.vehiculo),\n"
        "      servicio: Number(datos.servicio),\n"
        "      operario: Number(datos.operario),\n"
        "      observaciones: datos.observaciones.trim()\n"
        "    });\n"
        "    setDatos(VACIO);\n"
        "  } finally {\n"
        "    setEnviando(false);\n"
        "  }\n"
        "}")
    d.h3("4.4 Etiqueta de estado")
    d.p("EstadoOrden convierte el código del estado en una etiqueta legible y aplica la "
        "clase de color correspondiente. Es un componente pequeño que se reutiliza en "
        "todas las tablas.")
    d.codigo(
        "const ETIQUETAS = {\n"
        "  EN_COLA: \"En cola\",\n"
        "  EN_PROCESO: \"En proceso\",\n"
        "  FINALIZADO: \"Finalizado\",\n"
        "  ENTREGADO: \"Entregado\"\n"
        "};\n"
        "\n"
        "export default function EstadoOrden({ estado }) {\n"
        "  return (\n"
        "    <span className={`estado estado-${estado.toLowerCase()}`}>\n"
        "      {ETIQUETAS[estado] ?? estado}\n"
        "    </span>\n"
        "  );\n"
        "}")

    d.h2("5. Consumo de los servicios web")
    d.p("Las llamadas a la API se centralizan en src/servicios/api.js. El módulo define la "
        "URL base, configura las cabeceras, interpreta los errores y expone una función por "
        "cada operación del sistema.")
    d.codigo(
        "const BASE = import.meta.env.VITE_API_URL ?? \"/api\";\n"
        "\n"
        "async function solicitar(ruta, opciones = {}) {\n"
        "  const configuracion = {\n"
        "    headers: { \"Content-Type\": \"application/json\" },\n"
        "    ...opciones\n"
        "  };\n"
        "  const respuesta = await fetch(`${BASE}${ruta}`, configuracion);\n"
        "  if (!respuesta.ok) {\n"
        "    const cuerpo = await respuesta.json();\n"
        "    throw new Error(cuerpo.mensaje || cuerpo.detalle || \"Error en la solicitud\");\n"
        "  }\n"
        "  return respuesta.json();\n"
        "}\n"
        "\n"
        "export const api = {\n"
        "  login: (correo, clave) => solicitar(\"/auth/login\", {\n"
        "    method: \"POST\", body: JSON.stringify({ correo, clave })\n"
        "  }),\n"
        "  ordenes: () => solicitar(\"/ordenes\"),\n"
        "  crearOrden: (orden) => solicitar(\"/ordenes\", {\n"
        "    method: \"POST\", body: JSON.stringify(orden)\n"
        "  }),\n"
        "  avanzarOrden: (id) => solicitar(`/ordenes/${id}/estado`, { method: \"PUT\" })\n"
        "};")

    d.h2("6. Configuración como aplicación web progresiva")
    d.p("La aplicación incluye un manifiesto web y un service worker. El manifiesto define "
        "el nombre, los colores, el icono y el modo independiente; el service worker "
        "almacena los recursos principales para mejorar la carga y permitir el uso con "
        "conexiones lentas.")
    d.codigo(
        "if (\"serviceWorker\" in navigator && import.meta.env.PROD) {\n"
        "  window.addEventListener(\"load\", () => {\n"
        "    navigator.serviceWorker.register(\"/sw.js\").catch(() => {\n"
        "      // La aplicación sigue funcionando sin el service worker.\n"
        "    });\n"
        "  });\n"
        "}")
    d.p("El diseño responsivo se implementa con media queries. En pantallas pequeñas la "
        "barra lateral se convierte en una barra inferior, las tarjetas se organizan en una "
        "columna y las tablas conservan solo las columnas esenciales o permiten "
        "desplazamiento horizontal.")

    d.h2("7. Pantallas implementadas")
    d.p("Las siguientes capturas corresponden a la aplicación en ejecución, conectada a la "
        "API y a la base de datos del sistema.")
    d.imagen(f"{CAPTURAS}\\react_login.png",
             "Inicio de sesión del front-end.", 12.5)
    d.imagen(f"{CAPTURAS}\\react_panel.png",
             "Panel principal con indicadores.", 14.0)
    d.imagen(f"{CAPTURAS}\\react_clientes.png",
             "Gestión de clientes.", 14.0)
    d.imagen(f"{CAPTURAS}\\react_ordenes.png",
             "Registro y control de órdenes de lavado.", 14.0)
    d.imagen(f"{CAPTURAS}\\react_reportes.png",
             "Reportes de ingresos y servicios.", 13.5)
    d.imagen(f"{CAPTURAS}\\react_movil.png",
             "Versión móvil instalable.", 11.5)

    d.h2("8. Compilación y pruebas")
    d.p("La compilación de producción se ejecutó con npm run build. Vite transformó 46 "
        "módulos y generó los archivos optimizados que se relacionan a continuación.")
    d.tabla(
        ["Archivo", "Tamaño", "Tamaño comprimido"],
        [
            ["index.html", "0.68 kB", "0.39 kB"],
            ["assets/index.css", "6.53 kB", "2.02 kB"],
            ["assets/index.js", "158.08 kB", "50.01 kB"],
        ],
        anchos=[6.4, 4.6, 4.6],
        caption="Resultado de la compilación del front-end.",
    )
    d.p("Se verificó el inicio de sesión, la carga del panel, el registro de clientes, el "
        "registro de órdenes, el avance de estados, los reportes y la visualización en "
        "pantalla móvil. Todas las pruebas finalizaron sin errores.")

    d.h2("9. Repositorio y entrega")
    d.p("El código se encuentra en el repositorio " + REPO + ", en la carpeta "
        "frontend-react. La entrega se realiza en DylanArias_AA4_EV03.zip, que contiene los "
        "archivos del proyecto, el archivo con el enlace del repositorio y las instrucciones "
        "para ejecutarlo.")
    d.codigo(
        "npm install\n"
        "npm run dev      # servidor de desarrollo en http://localhost:5173\n"
        "npm run build    # compilación para producción")

    d.conclusion([
        "La codificación del front-end permitió implementar la interfaz de AquaLavado con "
        "componentes reutilizables, consumo de la API y diseño responsivo. Las pantallas de "
        "acceso, panel, clientes, órdenes y reportes funcionan con los datos reales del "
        "sistema y mantienen una presentación coherente en computador y teléfono.",
        "La configuración como PWA y la compilación optimizada dejan el componente listo "
        "para su despliegue. El código conserva los estándares del proyecto y se encuentra "
        "versionado en GitHub, lo que facilita su revisión y mantenimiento.",
    ])

    d.bibliografia([
        "React. (2025). React documentation. https://react.dev",
        "Vite. (2025). Vite guide. https://vite.dev/guide/",
        "MDN Web Docs. (2025). Progressive web apps. https://developer.mozilla.org/es/docs/Web/Progressive_web_apps",
        "MDN Web Docs. (2025). Fetch API. https://developer.mozilla.org/es/docs/Web/API/Fetch_API",
        "W3C. (2023). Web content accessibility guidelines (WCAG) 2.2. https://www.w3.org/TR/WCAG22/",
    ])
    return d.guardar()


if __name__ == "__main__":
    cual = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cual in ("all", "ev01"):
        print(ev01())
    if cual in ("all", "ev02"):
        print(ev02())
    if cual in ("all", "ev03"):
        print(ev03())
