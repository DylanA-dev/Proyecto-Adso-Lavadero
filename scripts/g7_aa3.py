# -*- coding: utf-8 -*-
"""Documentos de la actividad GA7-220501096-AA3 (stand-alone, web y móvil)."""
import sys

from sena_doc import SenaDoc

FECHA = "Noviembre 2026"
REPO = "https://github.com/DylanA-dev/Proyecto-Adso-Lavadero"
CAPTURAS = r"C:\Users\dylan\Documents\OpenCode\ADSO\proyectos\lavadero\interfaz\capturas"


def ev01():
    d = SenaDoc(
        "GA7-220501096-AA3-EV01",
        "Codificación de módulos del software stand-alone, web y móvil",
        FECHA,
    )
    d.intro([
        "El sistema AquaLavado se implementó en tres versiones que comparten el mismo "
        "modelo de datos y las mismas reglas del negocio: una aplicación de escritorio "
        "para la operación local del lavadero, una API web construida con Spring Boot y "
        "una aplicación móvil instalable desarrollada con React. Esta organización "
        "permite atender diferentes formas de uso sin duplicar la lógica de persistencia.",
        "En esta evidencia se presenta la codificación de los módulos de las tres "
        "versiones, los frameworks utilizados, la estructura de cada proyecto, los "
        "fragmentos de código más representativos y las capturas de funcionamiento. El "
        "código se encuentra versionado en el repositorio del proyecto y conserva los "
        "estándares de codificación definidos en la evidencia AA1-EV02.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Codificar los módulos del sistema AquaLavado en sus versiones stand-alone, web y "
        "móvil, aplicando frameworks de desarrollo, los estándares de codificación del "
        "proyecto y las herramientas de versionamiento.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Implementar la versión de escritorio con Java Swing y acceso a datos por JDBC.",
        "Construir la API web con Spring Boot y exponer los servicios del sistema.",
        "Desarrollar la versión móvil instalable con React y tecnología PWA.",
        "Reutilizar el modelo de datos y las clases DAO en las tres versiones.",
        "Documentar el código con comentarios y aplicar los estándares definidos.",
        "Versionar cada versión en el repositorio del proyecto.",
    ])

    d.h2("2. Alcance de las tres versiones")
    d.tabla(
        ["Versión", "Tecnología principal", "Uso previsto", "Módulos implementados"],
        [
            ["Stand-alone", "Java Swing", "Operación local en el computador del lavadero.", "Panel, clientes y órdenes de lavado."],
            ["Web", "Spring Boot", "Servicios REST para el front-end y otros clientes.", "Autenticación, clientes, vehículos, servicios, órdenes y reportes."],
            ["Móvil", "React y PWA", "Consulta y registro desde el teléfono del operario.", "Acceso, panel, clientes, órdenes y reportes."],
        ],
        anchos=[2.8, 3.6, 5.0, 4.4],
        caption="Versiones del sistema AquaLavado.",
        size=7.5,
    )
    d.p("Las tres versiones se conectan a la base de datos aqualavado y reutilizan las "
        "clases del modelo y los DAO construidos con JDBC. La versión web expone los "
        "servicios que consume la aplicación React; la versión de escritorio accede "
        "directamente a la base de datos desde el equipo del lavadero.")

    d.h2("3. Arquitectura compartida")
    d.p("El proyecto se organiza en módulos independientes que comparten el núcleo de "
        "datos. La siguiente tabla describe la función de cada carpeta del repositorio.")
    d.tabla(
        ["Carpeta", "Contenido", "Tecnología"],
        [
            ["base-datos", "Script de creación, datos iniciales y consultas de verificación.", "SQL"],
            ["jdbc", "Modelo, conexión, DAO, aplicación de consola y pruebas CRUD.", "Java SE"],
            ["escritorio", "Aplicación de escritorio con interfaz gráfica.", "Java Swing"],
            ["web-servlets", "Aplicación web con servlets y JSP.", "Servlet, JSP, Tomcat"],
            ["api-spring", "API REST del sistema.", "Spring Boot"],
            ["frontend-react", "Componentes, vistas y PWA.", "React, Vite"],
        ],
        anchos=[3.4, 8.8, 3.4],
        caption="Módulos del repositorio.",
    )

    d.h2("4. Versión stand-alone")
    d.p("La aplicación de escritorio se construyó con Java Swing y se organiza en un marco "
        "principal con pestañas para el panel de indicadores, los clientes y las órdenes de "
        "lavado. Cada pestaña utiliza los DAO del módulo JDBC, de modo que las operaciones "
        "se ejecutan sobre la misma base de datos del sistema.")
    d.codigo(
        "public class AplicacionEscritorio extends JFrame {\n"
        "\n"
        "    public AplicacionEscritorio(int tabInicial) {\n"
        "        super(\"AquaLavado | Escritorio\");\n"
        "        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n"
        "        setSize(1180, 820);\n"
        "        setLayout(new BorderLayout());\n"
        "\n"
        "        add(construirEncabezado(), BorderLayout.NORTH);\n"
        "\n"
        "        JTabbedPane pestanas = new JTabbedPane();\n"
        "        pestanas.addTab(\"Panel\", new PanelResumen(clienteDAO, ordenDAO));\n"
        "        pestanas.addTab(\"Clientes\", new PanelClientes(clienteDAO));\n"
        "        pestanas.addTab(\"Órdenes de lavado\",\n"
        "                new PanelOrdenes(ordenDAO, vehiculoDAO, servicioDAO));\n"
        "        add(pestanas, BorderLayout.CENTER);\n"
        "    }\n"
        "}")
    d.p("El registro de una orden reutiliza el precio del servicio seleccionado y crea "
        "la orden en estado EN_COLA. El botón Avanzar estado recorre la secuencia "
        "EN_COLA, EN_PROCESO, FINALIZADO y ENTREGADO, y registra la fecha de salida cuando "
        "el vehículo se entrega.")
    d.imagen(f"{CAPTURAS}\\escritorio_panel.png",
             "Versión stand-alone: panel de indicadores.", 14.5)
    d.imagen(f"{CAPTURAS}\\escritorio_clientes.png",
             "Versión stand-alone: gestión de clientes.", 14.5)
    d.imagen(f"{CAPTURAS}\\escritorio_ordenes.png",
             "Versión stand-alone: registro y control de órdenes.", 14.5)

    d.h2("5. Versión web")
    d.p("La versión web se implementó con Spring Boot, que proporciona el servidor "
        "embebido, el manejo de dependencias y la publicación de servicios REST. La API "
        "se organiza en controladores que delegan las operaciones en los DAO y devuelven "
        "las respuestas en formato JSON.")
    d.tabla(
        ["Método", "Ruta", "Función"],
        [
            ["POST", "/api/auth/login", "Validar las credenciales del usuario."],
            ["GET", "/api/clientes", "Listar los clientes registrados."],
            ["POST", "/api/clientes", "Registrar un cliente."],
            ["PUT", "/api/clientes/{id}", "Actualizar un cliente."],
            ["DELETE", "/api/clientes/{id}", "Eliminar un cliente."],
            ["GET", "/api/vehiculos", "Listar los vehículos y su cliente."],
            ["GET", "/api/servicios", "Listar los servicios y sus precios."],
            ["GET", "/api/ordenes", "Listar las órdenes de lavado."],
            ["POST", "/api/ordenes", "Registrar una orden de lavado."],
            ["PUT", "/api/ordenes/{id}/estado", "Avanzar el estado de una orden."],
            ["GET", "/api/reportes/resumen", "Consolidar ingresos y lavados por servicio."],
        ],
        anchos=[2.0, 6.4, 7.2],
        caption="Servicios REST de la versión web.",
        size=7.5,
    )
    d.codigo(
        "@RestController\n"
        "@RequestMapping(\"/api/ordenes\")\n"
        "public class OrdenController {\n"
        "\n"
        "    private final OrdenLavadoDAO ordenDAO = new OrdenLavadoDAO();\n"
        "\n"
        "    @GetMapping\n"
        "    public List<OrdenLavado> listar() throws SQLException {\n"
        "        return ordenDAO.listar();\n"
        "    }\n"
        "\n"
        "    @PostMapping\n"
        "    @ResponseStatus(HttpStatus.CREATED)\n"
        "    public OrdenLavado crear(@RequestBody NuevaOrden solicitud) throws SQLException {\n"
        "        Servicio servicio = servicioDAO.buscarPorId(solicitud.servicio());\n"
        "        OrdenLavado orden = new OrdenLavado(solicitud.vehiculo(),\n"
        "                solicitud.servicio(), solicitud.operario(),\n"
        "                OrdenLavado.ESTADO_EN_COLA, servicio.getPrecio(),\n"
        "                solicitud.observaciones());\n"
        "        ordenDAO.insertar(orden);\n"
        "        return ordenDAO.buscarPorId(orden.getIdOrden());\n"
        "    }\n"
        "}")
    d.p("La API configura CORS para permitir el consumo desde la aplicación React y "
        "centraliza el manejo de errores en un controlador de excepciones que devuelve "
        "mensajes claros en formato JSON. El proyecto se ejecuta en el puerto 8081 y se "
        "conecta a la base de datos mediante las propiedades de Spring.")
    d.codigo(
        "server.port=8081\n"
        "spring.datasource.url=jdbc:mysql://localhost:3306/aqualavado?useSSL=false\n"
        "spring.datasource.username=root\n"
        "spring.datasource.password=")

    d.h2("6. Versión móvil")
    d.p("La versión móvil se construyó con React y se empaquetó como aplicación web "
        "progresiva (PWA). La interfaz se adapta a pantallas pequeñas: el menú lateral se "
        "convierte en una barra inferior, las tarjetas se organizan en una columna y las "
        "tablas permiten desplazamiento horizontal cuando conservan todas sus columnas.")
    d.bullets([
        "Manifiesto web con nombre, colores, icono y modo de visualización independiente.",
        "Service worker que almacena los recursos principales para mejorar la carga.",
        "Diseño responsivo con media queries para teléfonos y tabletas.",
        "Consumo de la API mediante fetch y manejo de estados de carga y error.",
        "Instalación desde el navegador como aplicación en la pantalla de inicio.",
    ])
    d.codigo(
        "{\n"
        "  \"name\": \"AquaLavado — Gestión de lavadero\",\n"
        "  \"short_name\": \"AquaLavado\",\n"
        "  \"start_url\": \"/\",\n"
        "  \"display\": \"standalone\",\n"
        "  \"background_color\": \"#eef2f7\",\n"
        "  \"theme_color\": \"#0e3a7d\",\n"
        "  \"orientation\": \"portrait\",\n"
        "  \"icons\": [{ \"src\": \"/icono.svg\", \"sizes\": \"any\",\n"
        "               \"type\": \"image/svg+xml\" }]\n"
        "}")
    d.imagen(f"{CAPTURAS}\\react_movil.png",
             "Versión móvil instalable: panel principal.", 12.8)

    d.h2("7. Estándares y comentarios en el código")
    d.p("Las tres versiones aplican los estándares definidos para el proyecto: paquetes en "
        "minúsculas, clases en PascalCase, métodos en camelCase, constantes en mayúsculas y "
        "consultas parametrizadas. Los métodos públicos están documentados con JavaDoc y "
        "los componentes React incluyen comentarios sobre su responsabilidad y sus props.")
    d.tabla(
        ["Elemento", "Convención aplicada", "Ejemplo"],
        [
            ["Paquete", "Dominio invertido y capa", "com.aqualavado.api.controlador"],
            ["Clase", "PascalCase singular", "OrdenController"],
            ["Método", "camelCase con verbo", "listarPorEstado"],
            ["Componente", "PascalCase", "TablaOrdenes"],
            ["Hook", "camelCase con prefijo use", "useEffect"],
            ["Constante", "Mayúsculas con guion bajo", "ESTADO_EN_COLA"],
        ],
        anchos=[3.4, 6.4, 5.8],
        caption="Convenciones aplicadas en las tres versiones.",
    )

    d.h2("8. Estructura de los proyectos")
    d.codigo(
        "lavadero/\n"
        "├── base-datos/aqualavado.sql\n"
        "├── jdbc/src/com/aqualavado/{conexion,modelo,dao,app,pruebas}\n"
        "├── escritorio/src/com/aqualavado/escritorio/\n"
        "├── web-servlets/src/com/aqualavado/web/ y web/WEB-INF/vistas/\n"
        "├── api-spring/src/main/java/com/aqualavado/api/\n"
        "└── frontend-react/src/{componentes,paginas,servicios}/")

    d.h2("9. Pruebas de funcionamiento")
    d.tabla(
        ["Versión", "Prueba", "Resultado"],
        [
            ["Stand-alone", "Abrir la aplicación y consultar clientes y órdenes.", "Aprobada"],
            ["Stand-alone", "Registrar una orden y avanzar su estado.", "Aprobada"],
            ["Web", "Consultar /api/ordenes y /api/reportes/resumen.", "Aprobada"],
            ["Web", "Registrar una orden con el precio del servicio.", "Aprobada"],
            ["Móvil", "Iniciar sesión y consultar el panel desde pantalla pequeña.", "Aprobada"],
            ["Móvil", "Registrar una orden y consultar los reportes.", "Aprobada"],
        ],
        anchos=[3.2, 9.4, 3.0],
        caption="Pruebas de funcionamiento por versión.",
    )

    d.h2("10. Repositorio y entrega")
    d.p("El código de las tres versiones se encuentra en el repositorio " + REPO + ". La "
        "entrega se realiza en un archivo comprimido con las carpetas del proyecto, el "
        "script de la base de datos, el controlador JDBC y el archivo con el enlace del "
        "repositorio.")
    d.tabla(
        ["Archivo", "Contenido"],
        [
            ["DylanArias_AA3_EV01.zip", "Proyectos stand-alone, web y móvil, base de datos y controlador."],
            ["ENLACE_REPOSITORIO.txt", "Dirección del repositorio en GitHub."],
            ["README.md", "Instrucciones de compilación y ejecución."],
        ],
        anchos=[5.6, 10.0],
        caption="Archivos de la entrega AA3-EV01.",
    )

    d.conclusion([
        "La codificación de las tres versiones permitió llevar el sistema AquaLavado a "
        "diferentes entornos de uso sin duplicar la lógica del negocio. La aplicación de "
        "escritorio atiende la operación local, la API de Spring Boot expone los servicios "
        "del sistema y la aplicación React ofrece una versión móvil instalable.",
        "La reutilización del modelo y de los DAO, junto con la aplicación de los "
        "estándares de codificación y el versionamiento en GitHub, garantiza coherencia "
        "entre las versiones y facilita su mantenimiento y evolución.",
    ])

    d.bibliografia([
        "Oracle. (2025). Java Platform, Standard Edition Documentation. https://docs.oracle.com/en/java/",
        "Oracle. (2025). Creating a GUI with Swing. https://docs.oracle.com/javase/tutorial/uiswing/",
        "Spring. (2025). Spring Boot reference documentation. https://docs.spring.io/spring-boot/",
        "React. (2025). React documentation. https://react.dev",
        "MDN Web Docs. (2025). Progressive web apps. https://developer.mozilla.org/es/docs/Web/Progressive_web_apps",
        "MySQL. (2024). MySQL 8.0 reference manual. https://dev.mysql.com/doc/refman/8.0/en/",
    ])
    return d.guardar()


def ev02():
    d = SenaDoc(
        "GA7-220501096-AA3-EV02",
        "Módulos de software stand-alone, web y móvil codificados y probados",
        FECHA,
    )
    d.intro([
        "La verificación del software permite comprobar que los módulos codificados "
        "cumplen las historias de usuario y que las validaciones protegen la información "
        "del sistema. En esta evidencia se presentan las pruebas ejecutadas sobre las "
        "versiones stand-alone, web y móvil de AquaLavado, con la descripción de cada "
        "historia de usuario y la captura de la interfaz correspondiente.",
        "También se documentan las pruebas de validación de fechas, números, textos, "
        "caracteres especiales y longitudes, y se incluye el guion del video que muestra "
        "la funcionalidad del módulo con sus respectivas validaciones.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Ejecutar y documentar las pruebas funcionales y de validación de los módulos "
        "stand-alone, web y móvil de AquaLavado, verificando el cumplimiento de las "
        "historias de usuario y el comportamiento del sistema frente a datos válidos e "
        "inválidos.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Relacionar cada historia de usuario con la pantalla que la evidencia.",
        "Verificar el registro y la consulta de clientes y órdenes.",
        "Comprobar el avance de estados y el cálculo del valor del servicio.",
        "Validar fechas, números, textos, caracteres especiales y longitudes.",
        "Consolidar los resultados de las pruebas ejecutadas.",
        "Documentar el guion del video de funcionamiento.",
    ])

    d.h2("2. Historias de usuario")
    d.tabla(
        ["Código", "Historia de usuario", "Criterio de aceptación"],
        [
            ["HU-01", "Como usuario quiero iniciar sesión para acceder al sistema.", "El acceso se permite solo con credenciales válidas."],
            ["HU-02", "Como administrador quiero ver los indicadores del lavadero.", "El panel muestra órdenes activas, entregadas, ingresos y promedio."],
            ["HU-03", "Como operario quiero registrar clientes.", "El cliente se guarda con documento, nombre y teléfono válidos."],
            ["HU-04", "Como operario quiero registrar la entrada de un vehículo.", "La orden se crea en estado EN_COLA con el valor del servicio."],
            ["HU-05", "Como operario quiero avanzar el estado del lavado.", "La orden cambia a EN_PROCESO, FINALIZADO y ENTREGADO."],
            ["HU-06", "Como administrador quiero consultar los reportes.", "Se presentan ingresos, ticket promedio y lavados por servicio."],
            ["HU-07", "Como operario quiero operar el sistema desde el computador del lavadero.", "La aplicación de escritorio permite gestionar clientes y órdenes."],
            ["HU-08", "Como operario quiero consultar el sistema desde el teléfono.", "La versión móvil se adapta a la pantalla y permite registrar órdenes."],
        ],
        anchos=[2.0, 7.6, 6.2],
        caption="Historias de usuario del sistema AquaLavado.",
        size=7.5,
    )

    d.h2("3. Evidencias por historia de usuario")
    d.h3("HU-01. Inicio de sesión")
    d.p("El usuario ingresa su correo y contraseña. El sistema valida las credenciales "
        "contra el hash almacenado y, si son correctas, abre la sesión; en caso contrario "
        "muestra un mensaje de error y conserva el formulario.")
    d.imagen(f"{CAPTURAS}\\react_login.png",
             "Pantalla de inicio de sesión de la versión web y móvil.", 12.5)

    d.h3("HU-02. Panel de indicadores")
    d.p("El panel presenta las órdenes activas, los lavados entregados, los ingresos y el "
        "ticket promedio, además de las últimas órdenes registradas con su estado.")
    d.imagen(f"{CAPTURAS}\\react_panel.png",
             "Panel principal con indicadores de la operación.", 14.0)

    d.h3("HU-03. Registro de clientes")
    d.p("El formulario solicita documento, nombre, teléfono, correo y dirección. Los "
        "campos obligatorios y los patrones de documento y teléfono impiden el envío de "
        "datos incompletos. Al guardar, el cliente aparece en la tabla superior.")
    d.imagen(f"{CAPTURAS}\\react_clientes.png",
             "Registro y listado de clientes en la versión web.", 14.0)

    d.h3("HU-04. Registro de orden de lavado")
    d.p("El operario selecciona el vehículo, el servicio y el operario. El sistema toma el "
        "precio del servicio, registra la fecha de ingreso y crea la orden en estado "
        "EN_COLA.")
    d.imagen(f"{CAPTURAS}\\react_ordenes.png",
             "Registro de órdenes y avance de estado.", 14.0)

    d.h3("HU-05. Control de estados")
    d.p("Cada orden recorre los estados EN_COLA, EN_PROCESO, FINALIZADO y ENTREGADO. El "
        "botón Avanzar actualiza el estado y, al llegar a ENTREGADO, registra la fecha de "
        "salida del vehículo. Las órdenes entregadas ya no muestran la acción.")
    d.p("La misma operación se verificó en la aplicación de escritorio, donde el estado "
        "se actualiza en la tabla y se conserva en la base de datos.")
    d.imagen(f"{CAPTURAS}\\escritorio_ordenes.png",
             "Control de órdenes en la versión stand-alone.", 14.0)

    d.h3("HU-06. Reportes")
    d.p("El reporte consolida los lavados entregados, los ingresos, el ticket promedio y "
        "la cantidad de órdenes por tipo de servicio, con el valor acumulado de cada uno.")
    d.imagen(f"{CAPTURAS}\\react_reportes.png",
             "Reporte de ingresos y lavados por servicio.", 13.5)

    d.h3("HU-07. Operación desde el escritorio")
    d.p("La versión stand-alone permite consultar los clientes, registrar nuevos clientes "
        "y gestionar las órdenes desde el computador del lavadero, con acceso directo a la "
        "base de datos.")
    d.imagen(f"{CAPTURAS}\\escritorio_clientes.png",
             "Gestión de clientes en la aplicación de escritorio.", 14.0)

    d.h3("HU-08. Operación desde el teléfono")
    d.p("La versión móvil presenta el panel en una columna, una barra de navegación "
        "inferior y las acciones principales al alcance del pulgar. La aplicación puede "
        "instalarse en la pantalla de inicio del teléfono.")
    d.imagen(f"{CAPTURAS}\\react_movil.png",
             "Panel principal en la versión móvil instalable.", 12.0)

    d.h2("4. Pruebas de validación")
    d.p("Se probaron los formularios con datos válidos e inválidos para comprobar que el "
        "sistema rechaza la información incorrecta y conserva la integridad de la base de "
        "datos.")
    d.tabla(
        ["Tipo", "Dato ingresado", "Comportamiento esperado", "Resultado"],
        [
            ["Número", "Documento con letras (ABC123).", "El navegador impide el envío por el patrón numérico.", "Aprobada"],
            ["Longitud", "Documento de 5 dígitos.", "Se rechaza porque el mínimo es 6.", "Aprobada"],
            ["Longitud", "Documento de 16 dígitos.", "Se rechaza porque el máximo es 15.", "Aprobada"],
            ["Número", "Teléfono con letras.", "Se rechaza por el patrón numérico.", "Aprobada"],
            ["Longitud", "Teléfono de 6 dígitos.", "Se rechaza porque el mínimo es 7.", "Aprobada"],
            ["Texto", "Nombre vacío.", "El campo obligatorio impide el envío.", "Aprobada"],
            ["Texto", "Nombre de 81 caracteres.", "Se limita a 80 caracteres.", "Aprobada"],
            ["Correo", "Correo sin arroba.", "El tipo email impide el envío.", "Aprobada"],
            ["Especiales", "Nombre María Gómez y operario Camilo Ríos.", "Se almacenan y muestran con tildes.", "Aprobada"],
            ["Especiales", "Observación con comillas y punto y coma.", "Se guarda como texto, sin afectar la consulta.", "Aprobada"],
            ["Fecha", "Ingreso de una orden.", "La fecha se genera automáticamente, no se digita.", "Aprobada"],
            ["Número", "Intento de modificar el valor desde el formulario.", "El valor se toma del precio del servicio.", "Aprobada"],
            ["Selección", "Orden sin vehículo o sin servicio.", "El formulario exige la selección.", "Aprobada"],
            ["Longitud", "Observación de 201 caracteres.", "Se limita a 200 caracteres.", "Aprobada"],
        ],
        anchos=[2.2, 5.0, 6.6, 2.0],
        caption="Pruebas de validación de datos.",
        size=7.5,
    )

    d.h2("5. Resultados consolidados")
    d.tabla(
        ["Historia", "Pruebas", "Aprobadas", "Fallidas"],
        [
            ["HU-01", "Credenciales válidas e inválidas.", "2", "0"],
            ["HU-02", "Indicadores y últimas órdenes.", "2", "0"],
            ["HU-03", "Registro y validación de clientes.", "5", "0"],
            ["HU-04", "Registro de orden y cálculo del valor.", "2", "0"],
            ["HU-05", "Avance de estados y fecha de salida.", "3", "0"],
            ["HU-06", "Reportes y totales.", "2", "0"],
            ["HU-07", "Operación desde el escritorio.", "2", "0"],
            ["HU-08", "Operación desde el móvil.", "2", "0"],
        ],
        anchos=[2.4, 9.0, 2.2, 2.0],
        caption="Consolidado de pruebas por historia de usuario.",
    )
    d.p("El total fue de 20 pruebas aprobadas y 0 fallidas. Las validaciones se aplican "
        "tanto en el navegador como en el servidor, y las consultas utilizan parámetros "
        "para evitar la alteración de las sentencias SQL.")

    d.h2("6. Guion del video")
    d.p("El video muestra la funcionalidad del módulo y las validaciones. Se recomienda "
        "grabarlo en una sola toma, con el nombre del aprendiz al inicio y una duración "
        "entre cinco y siete minutos.")
    d.tabla(
        ["Escena", "Contenido", "Duración"],
        [
            ["1. Presentación", "Nombre del aprendiz, programa y nombre del sistema.", "15 s"],
            ["2. Acceso", "Inicio de sesión con credenciales válidas e intento con clave incorrecta.", "30 s"],
            ["3. Panel", "Recorrido por los indicadores y las últimas órdenes.", "30 s"],
            ["4. Clientes", "Registro de un cliente y validación de documento y teléfono.", "60 s"],
            ["5. Órdenes", "Registro de una orden y cálculo del valor del servicio.", "60 s"],
            ["6. Estados", "Avance de EN_COLA a ENTREGADO y fecha de salida.", "45 s"],
            ["7. Reportes", "Consulta de ingresos y lavados por servicio.", "30 s"],
            ["8. Escritorio", "Operación desde la aplicación stand-alone.", "45 s"],
            ["9. Móvil", "Apertura de la versión instalable y registro desde pantalla pequeña.", "45 s"],
            ["10. Cierre", "Conclusiones y despedida.", "15 s"],
        ],
        anchos=[3.2, 10.4, 2.2],
        caption="Guion del video de funcionamiento.",
        size=7.5,
    )

    d.h2("7. Repositorio y entrega")
    d.p("Las pruebas se ejecutaron sobre el código publicado en " + REPO + ". La entrega "
        "incluye los archivos del proyecto, este documento, el video y el archivo con el "
        "enlace del repositorio, comprimidos en DylanArias_AA3_EV02.zip.")

    d.conclusion([
        "Las pruebas ejecutadas sobre las tres versiones confirmaron el cumplimiento de "
        "las historias de usuario y el funcionamiento de las validaciones. El sistema "
        "rechaza documentos, teléfonos y correos inválidos, controla las longitudes y "
        "conserva la integridad de la información almacenada.",
        "La documentación de cada historia con su pantalla y el guion del video permiten "
        "verificar la trazabilidad entre los requisitos y la implementación. El módulo "
        "queda probado y disponible para la sustentación del proyecto.",
    ])

    d.bibliografia([
        "Sommerville, I. (2016). Software engineering (10.ª ed.). Pearson.",
        "Pressman, R. S. y Maxim, B. R. (2020). Software engineering: A practitioner's approach (9.ª ed.). McGraw-Hill.",
        "MDN Web Docs. (2025). Constraint validation. https://developer.mozilla.org/es/docs/Web/HTML/Constraint_validation",
        "React. (2025). React documentation. https://react.dev",
        "MySQL. (2024). MySQL 8.0 reference manual. https://dev.mysql.com/doc/refman/8.0/en/",
    ])
    return d.guardar()


if __name__ == "__main__":
    cual = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cual in ("all", "ev01"):
        print(ev01())
    if cual in ("all", "ev02"):
        print(ev02())
