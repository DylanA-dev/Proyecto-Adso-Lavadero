# -*- coding: utf-8 -*-
"""Documentos de la actividad GA7-220501096-AA1 (planeación y versionamiento)."""
import sys

from sena_doc import SenaDoc

REPO = "https://github.com/DylanA-dev/Proyecto-Adso-Lavadero"
FECHA = "Noviembre 2026"


def ev01():
    d = SenaDoc(
        "GA7-220501096-AA1-EV01",
        "Informe técnico de plan de trabajo para construcción de software",
        FECHA,
    )
    d.intro([
        "La construcción de un sistema de información exige una planeación previa que "
        "ordene las actividades, defina las herramientas de trabajo y establezca los "
        "mecanismos de control sobre el código fuente. En esta evidencia se presenta el "
        "informe técnico del plan de trabajo para la construcción del software "
        "AquaLavado, sistema de gestión de lavadero de vehículos, tomando como base el "
        "diseño y los artefactos elaborados en las fases anteriores del proyecto "
        "formativo.",
        "El documento describe el alcance del software, la arquitectura definida, las "
        "tecnologías seleccionadas y las herramientas de versionamiento que se "
        "utilizarán durante la codificación. Igualmente, organiza el trabajo en fases, "
        "define los entregables de cada una y establece el flujo de trabajo con Git y "
        "GitHub, de manera que el equipo pueda construir el software de forma ordenada, "
        "trazable y verificable.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Definir el plan de trabajo y las herramientas tecnológicas para la construcción "
        "del software AquaLavado, de acuerdo con el diseño establecido y con las "
        "metodologías de desarrollo adoptadas en el proyecto formativo.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Delimitar el alcance funcional del sistema de gestión de lavadero de vehículos.",
        "Establecer la arquitectura y las tecnologías que se utilizarán en la codificación.",
        "Seleccionar y justificar las herramientas de versionamiento local y remoto.",
        "Organizar las actividades de construcción en fases, con entregables y criterios de aceptación.",
        "Definir el flujo de trabajo y las políticas de control de cambios del repositorio.",
    ])

    d.h2("2. Descripción del software")
    d.p("AquaLavado es un sistema de información cuyo propósito es apoyar la operación "
        "diaria de un lavadero de vehículos. El sistema registra la entrada del vehículo "
        "al establecimiento, genera la orden de servicio, controla el avance del lavado, "
        "registra la salida y el pago, y produce reportes de la operación. El servicio se "
        "presta de forma presencial en las instalaciones del lavadero; el sistema no "
        "gestiona lavados a domicilio ni desplazamiento de operarios a direcciones "
        "particulares.")
    d.p("Los módulos que componen el software se relacionan a continuación.")
    d.tabla(
        ["Módulo", "Función principal", "Datos que administra"],
        [
            ["Seguridad y usuarios", "Autenticar el acceso y controlar los roles de administrador y operario.", "Usuarios, credenciales y roles."],
            ["Clientes y vehículos", "Registrar y consultar los clientes y los vehículos asociados.", "Documento, nombre, teléfono, placa, marca, modelo y color."],
            ["Servicios", "Administrar los tipos de lavado y sus tarifas.", "Nombre del servicio, descripción, precio y duración estimada."],
            ["Órdenes de lavado", "Registrar la entrada del vehículo y generar la orden de servicio.", "Vehículo, servicio, operario, fecha de ingreso y observaciones."],
            ["Procesos", "Controlar el avance del lavado por estados.", "Estado: en cola, en proceso, finalizado y entregado."],
            ["Salida y pagos", "Registrar la entrega del vehículo y el pago del servicio.", "Valor, método de pago, fecha de salida y responsable."],
            ["Reportes", "Consolidar ingresos, lavados por tipo y ocupación del lavadero.", "Indicadores calculados a partir de las órdenes y los pagos."],
        ],
        anchos=[3.6, 6.6, 5.6],
        caption="Módulos del sistema AquaLavado.",
    )

    d.h2("3. Arquitectura del software")
    d.p("Se adopta una arquitectura por capas, en la que cada capa tiene una "
        "responsabilidad definida y se comunica con la siguiente mediante interfaces. "
        "Esta organización facilita el mantenimiento, las pruebas y la reutilización de "
        "los componentes.")
    d.tabla(
        ["Capa", "Responsabilidad", "Tecnología"],
        [
            ["Presentación", "Interfaz de usuario web y móvil, formularios, tablas y tablero de procesos.", "React, HTML5, CSS3, JavaScript"],
            ["Presentación de escritorio", "Aplicación stand-alone para operación local del lavadero.", "Java Swing"],
            ["Lógica de negocio", "Reglas del lavado, validaciones, cálculo de valores y control de estados.", "Java (Servlets, JSP y Spring Boot)"],
            ["Acceso a datos", "Consultas, inserciones, actualizaciones y eliminaciones.", "JDBC y patrón DAO"],
            ["Persistencia", "Almacenamiento relacional de la información.", "MySQL / MariaDB"],
            ["Infraestructura", "Servidor de aplicaciones y control de versiones.", "Apache Tomcat, Git y GitHub"],
        ],
        anchos=[3.6, 8.2, 4.0],
        caption="Capas de la arquitectura de AquaLavado.",
    )

    d.h2("4. Tecnologías y herramientas seleccionadas")
    d.p("La selección de tecnologías responde a los componentes formativos de la "
        "competencia y a las características del proyecto. Todas las herramientas "
        "empleadas son de uso libre y cuentan con documentación oficial.")
    d.tabla(
        ["Herramienta", "Versión de referencia", "Uso dentro del proyecto"],
        [
            ["Java Development Kit (JDK)", "21 LTS", "Compilación y ejecución del código Java."],
            ["Apache Tomcat", "8.5", "Servidor para servlets y páginas JSP."],
            ["Spring Boot", "3.x", "Construcción de la API REST del sistema."],
            ["MySQL / MariaDB", "8.0 / 10.4", "Base de datos relacional del sistema."],
            ["JDBC", "Incluido en el JDK", "Conexión y operaciones sobre la base de datos."],
            ["React", "18.x", "Componentes de la interfaz web y móvil."],
            ["Vite", "5.x", "Empaquetado y servidor de desarrollo del front-end."],
            ["Git", "2.5x", "Control de versiones local."],
            ["GitHub", "Servicio en la nube", "Repositorio remoto y trabajo colaborativo."],
            ["Visual Studio Code", "1.9x", "Editor de código y terminal integrada."],
        ],
        anchos=[4.4, 3.6, 7.8],
        caption="Tecnologías y herramientas del proyecto.",
    )

    d.h2("5. Herramientas de versionamiento")
    d.p("El control de versiones permite registrar la evolución del código, recuperar "
        "estados anteriores y trabajar de forma colaborativa sin sobrescribir el trabajo "
        "de otros. Para el proyecto se seleccionó **Git** como herramienta local y "
        "**GitHub** como repositorio remoto.")
    d.h3("5.1 Git local")
    d.p("Git es un sistema de control de versiones distribuido que almacena el historial "
        "completo del proyecto en el equipo del desarrollador. Cada confirmación de "
        "cambios (commit) conserva una instantánea del estado del código, lo que permite "
        "comparar versiones, crear ramas y revertir cambios sin depender de una conexión "
        "a Internet.")
    d.h3("5.2 GitHub remoto")
    d.p("GitHub aloja el repositorio remoto del proyecto y actúa como punto de "
        "encuentro del equipo. Allí se publican las ramas, se revisan los cambios "
        "mediante pull requests, se documentan los avances y se conserva una copia de "
        "respaldo del código. El repositorio definido para el proyecto es "
        f"{REPO}.")
    d.h3("5.3 Justificación de la selección")
    d.bullets([
        "Git es la herramienta de control de versiones más utilizada en la industria y cuenta con amplia documentación.",
        "Permite trabajo sin conexión y conserva el historial completo en cada copia del repositorio.",
        "GitHub facilita el respaldo del código, la revisión entre pares y la integración con herramientas de calidad.",
        "Ambas herramientas se integran con Visual Studio Code y con los procesos de integración continua vistos en el componente formativo.",
        "El uso de ramas y pull requests permite aislar los cambios y reducir el riesgo de afectar la rama principal.",
    ])
    d.tabla(
        ["Criterio", "Git + GitHub", "SVN", "Mercurial"],
        [
            ["Modelo", "Distribuido", "Centralizado", "Distribuido"],
            ["Historial local", "Completo", "Parcial", "Completo"],
            ["Trabajo sin conexión", "Sí", "Limitado", "Sí"],
            ["Ramas", "Livianas y rápidas", "Costosas", "Livianas"],
            ["Ecosistema y soporte", "Muy amplio", "Amplio", "Limitado"],
            ["Integración con el proyecto", "Alta", "Media", "Baja"],
        ],
        anchos=[3.8, 4.6, 3.6, 3.6],
        caption="Comparación de herramientas de control de versiones.",
    )

    d.h2("6. Plan de trabajo")
    d.p("El trabajo se organiza en seis fases que van desde la preparación del entorno "
        "hasta la entrega de los módulos probados. Cada fase tiene actividades, "
        "entregables y un criterio de aceptación verificable.")
    d.tabla(
        ["Fase", "Actividades principales", "Entregable", "Criterio de aceptación"],
        [
            ["1. Preparación", "Instalar y configurar JDK, Tomcat, MySQL, Git y el editor. Crear el repositorio y la base de datos.", "Entorno configurado y repositorio inicial.", "El proyecto compila y la base de datos responde."],
            ["2. Estándares", "Definir convenciones de nombres, estructura de clases, manejo de errores y estilo de código.", "Documento de estándares de codificación.", "El código revisado cumple las convenciones."],
            ["3. Persistencia", "Diseñar el modelo relacional e implementar las clases de conexión y los DAO con JDBC.", "Script SQL y módulo de acceso a datos.", "Las operaciones CRUD se ejecutan sin errores."],
            ["4. Lógica y servicios", "Codificar servlets, JSP y la API REST con las reglas del negocio.", "Módulos web y servicios.", "Los formularios registran y consultan información."],
            ["5. Interfaz", "Construir los componentes React y la versión móvil instalable.", "Front-end y PWA.", "Las vistas consumen los servicios y validan los datos."],
            ["6. Pruebas y entrega", "Ejecutar pruebas funcionales y de validación, documentar resultados y publicar en GitHub.", "Módulos probados y evidencia documental.", "Las pruebas aprobadas y el repositorio actualizado."],
        ],
        anchos=[2.9, 6.4, 3.6, 3.3],
        caption="Fases del plan de trabajo.",
        size=7.5,
    )

    d.h2("7. Organización del repositorio")
    d.p("El repositorio se organiza por módulos y por tecnologías, de modo que cada "
        "componente tenga un lugar definido y sea fácil de ubicar por el equipo y por el "
        "instructor.")
    d.codigo(
        "Proyecto-Adso-Lavadero/\n"
        "├── documentos/            Guías, informes y evidencias\n"
        "├── base-datos/            Scripts SQL y respaldos\n"
        "├── escritorio/            Aplicación stand-alone (Java Swing)\n"
        "├── web-servlets/          Aplicación web con servlets y JSP\n"
        "├── api-spring/            API REST con Spring Boot\n"
        "├── frontend-react/        Componentes React y PWA\n"
        "└── README.md              Descripción y modo de ejecución"
    )

    d.h2("8. Flujo de trabajo y control de cambios")
    d.p("El equipo adopta un flujo basado en ramas cortas y confirmaciones frecuentes. "
        "La rama principal conserva el código estable y cada funcionalidad se desarrolla "
        "en una rama independiente que se integra mediante pull request.")
    d.numeros([
        "Actualizar la rama principal con los últimos cambios del repositorio remoto.",
        "Crear una rama de trabajo con un nombre descriptivo, por ejemplo feature/registro-ordenes.",
        "Implementar la funcionalidad y verificar que el proyecto compile.",
        "Registrar los cambios con mensajes claros y descriptivos.",
        "Publicar la rama en GitHub y abrir un pull request.",
        "Revisar el código, corregir observaciones e integrar en la rama principal.",
    ])
    d.p("Los mensajes de confirmación siguen la convención de commits semánticos: "
        "**feat** para nuevas funcionalidades, **fix** para correcciones, **docs** para "
        "documentación, **test** para pruebas y **chore** para tareas de mantenimiento.")

    d.h2("9. Riesgos y plan de mitigación")
    d.tabla(
        ["Riesgo", "Impacto", "Mitigación"],
        [
            ["Pérdida de código por daño del equipo.", "Alto", "Publicar los cambios en GitHub al finalizar cada jornada."],
            ["Cambios sin documentar.", "Medio", "Exigir mensajes de commit descriptivos y pull requests revisados."],
            ["Incompatibilidad de versiones de Java o Tomcat.", "Medio", "Fijar versiones en el README y verificar el entorno antes de codificar."],
            ["Errores en la base de datos.", "Alto", "Versionar los scripts SQL y ejecutar pruebas sobre una copia de la base."],
            ["Retrasos por alcance no definido.", "Medio", "Controlar el alcance por módulos y validar cada entrega."],
        ],
        anchos=[6.2, 2.2, 7.4],
        caption="Riesgos identificados y acciones de mitigación.",
    )

    d.h2("10. Criterios de calidad y entregables")
    d.bullets([
        "El código compila sin errores y sigue los estándares definidos en la evidencia AA1-EV02.",
        "Las operaciones de inserción, consulta, actualización y eliminación funcionan sobre la base de datos.",
        "Los formularios validan los datos antes de enviarlos al servidor.",
        "Cada módulo se prueba con datos válidos y con datos incorrectos.",
        "El repositorio contiene el código, los scripts de base de datos y las instrucciones de ejecución.",
    ])

    d.conclusion([
        "El plan de trabajo definido permite abordar la construcción de AquaLavado de "
        "manera ordenada, con un alcance claro y con herramientas acordes a las "
        "necesidades del proyecto. La arquitectura por capas y la separación de módulos "
        "facilitan la codificación, las pruebas y el mantenimiento del software.",
        "La selección de Git y GitHub garantiza el control de los cambios y la "
        "conservación del historial del proyecto. Con este plan, el equipo cuenta con una "
        "ruta de trabajo verificable que servirá de base para las evidencias de "
        "codificación de los módulos y del front-end.",
    ])

    d.bibliografia([
        "Chacon, S. y Straub, B. (2014). Pro Git (2.ª ed.). Apress. https://git-scm.com/book/es/v2",
        "GitHub. (2026). GitHub Docs: About Git. https://docs.github.com/es/get-started/using-git/about-git",
        "Oracle. (2025). Java Platform, Standard Edition Documentation. https://docs.oracle.com/en/java/",
        "Pressman, R. S. y Maxim, B. R. (2020). Software engineering: A practitioner's approach (9.ª ed.). McGraw-Hill.",
        "React. (2025). React documentation. https://react.dev",
        "Sommerville, I. (2016). Software engineering (10.ª ed.). Pearson.",
        "Spring. (2025). Spring Boot reference documentation. https://docs.spring.io/spring-boot/",
    ])
    return d.guardar()


def ev02():
    d = SenaDoc(
        "GA7-220501096-AA1-EV02",
        "Definir estándares de codificación, de acuerdo con la plataforma de desarrollo elegida",
        FECHA,
    )
    d.intro([
        "Los estándares de codificación son el conjunto de reglas que orientan la "
        "escritura del código fuente para que sea legible, consistente y fácil de "
        "mantener. Su aplicación reduce los errores, facilita la revisión entre "
        "compañeros y permite que cualquier integrante del equipo comprenda el código "
        "sin depender de quien lo escribió.",
        "En esta evidencia se definen los estándares de codificación del proyecto "
        "AquaLavado, sistema de gestión de lavadero de vehículos, teniendo en cuenta la "
        "plataforma de desarrollo seleccionada: Java para la lógica y el acceso a datos, "
        "React para la interfaz y SQL para la persistencia. Las reglas se acompañan de "
        "ejemplos aplicados al dominio del lavadero.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Establecer los estándares de codificación que se aplicarán en la construcción "
        "del software AquaLavado, definiendo convenciones para el nombramiento de "
        "variables, clases, métodos y paquetes, así como criterios de estructura, "
        "comentarios, manejo de errores y organización del código.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Unificar la forma de nombrar los elementos del código en Java, React y SQL.",
        "Definir la estructura interna de clases, métodos y componentes.",
        "Establecer reglas de documentación y de manejo de excepciones.",
        "Fijar criterios de seguridad y eficiencia en el acceso a la base de datos.",
        "Facilitar la revisión de código y el trabajo colaborativo en el repositorio.",
    ])

    d.h2("2. Plataforma de desarrollo y alcance")
    d.tabla(
        ["Plataforma", "Tecnología", "Estándar de referencia"],
        [
            ["Backend", "Java 21 LTS", "Oracle Code Conventions y Google Java Style Guide"],
            ["Web", "Servlets, JSP y Spring Boot", "Convenciones Java y especificación Jakarta Servlet"],
            ["Front-end", "React 18 y JavaScript moderno", "Airbnb JavaScript Style Guide y documentación de React"],
            ["Base de datos", "MySQL / MariaDB", "Convenciones SQL y buenas prácticas de MySQL"],
            ["Control de versiones", "Git y GitHub", "Conventional Commits"],
        ],
        anchos=[3.4, 5.2, 7.2],
        caption="Plataformas y estándares de referencia.",
    )
    d.p("Las reglas descritas aplican a todo el código del repositorio "
        f"{REPO}. Cuando una situación no esté prevista, se aplica el criterio de "
        "claridad: el código debe poder entenderse sin explicaciones adicionales.")

    d.h2("3. Convenciones generales")
    d.bullets([
        "**Codificación de caracteres:** UTF-8 sin marca de orden de bytes en todos los archivos.",
        "**Idioma:** nombres de clases, métodos, variables y componentes en español; palabras reservadas y APIs en su idioma original.",
        "**Indentación:** cuatro espacios en Java y SQL; dos espacios en JavaScript y JSX. No se utilizan tabulaciones.",
        "**Longitud de línea:** máximo 100 caracteres en Java y 100 en JavaScript.",
        "**Llaves:** se abren en la misma línea de la declaración y se cierran en una línea independiente.",
        "**Espacios:** un espacio alrededor de los operadores y después de cada coma; ninguna línea termina con espacios.",
        "**Líneas en blanco:** una línea para separar métodos y bloques lógicos; ninguna línea en blanco al inicio o al final del archivo.",
        "**Archivos:** terminan con una línea vacía y no contienen código comentado sin justificación.",
    ])

    d.h2("4. Nombramiento de los elementos del código")
    d.p("Los nombres deben ser descriptivos, pronunciables y coherentes con el dominio "
        "del negocio. Se evitan abreviaturas arbitrarias y nombres genéricos como dato, "
        "cosa o variable1.")
    d.tabla(
        ["Elemento", "Convención", "Ejemplo correcto", "Ejemplo incorrecto"],
        [
            ["Paquete", "minúsculas, dominio invertido y capa", "com.aqualavado.dao", "com.Aqua.Lavadero"],
            ["Clase", "PascalCase, sustantivo singular", "OrdenLavado", "orden_lavado"],
            ["Interfaz", "PascalCase, adjetivo o sustantivo", "Calculable", "icalculable"],
            ["Método", "camelCase, verbo en infinitivo", "registrarOrden", "OrdenRegistrar"],
            ["Variable", "camelCase, sustantivo descriptivo", "fechaIngreso", "f1"],
            ["Constante", "MAYÚSCULAS con guion bajo", "ESTADO_EN_COLA", "estadoCola"],
            ["Booleano", "prefijo es, tiene o puede", "esEntregado", "entregado1"],
            ["Tabla SQL", "minúsculas, plural, guion bajo", "ordenes_lavado", "OrdenesLavado"],
            ["Columna SQL", "minúsculas, singular, guion bajo", "fecha_ingreso", "FechaDeIngreso"],
            ["Componente React", "PascalCase", "TableroProcesos", "tablero_procesos"],
            ["Hook", "camelCase con prefijo use", "useOrdenes", "obtenerOrdenes"],
            ["Archivo Java", "igual al nombre de la clase", "OrdenLavado.java", "orden.java"],
            ["Archivo React", "PascalCase para componentes", "OrdenForm.jsx", "orden-form.jsx"],
        ],
        anchos=[3.0, 5.0, 4.2, 3.6],
        caption="Convenciones de nombramiento.",
        size=7.5,
    )

    d.h2("5. Declaración de clases")
    d.p("Cada clase representa una entidad o una responsabilidad del sistema. La "
        "declaración debe incluir el paquete, las importaciones ordenadas, la "
        "documentación de la clase y los miembros organizados de la siguiente forma: "
        "constantes, atributos, constructores, métodos de acceso, métodos de negocio y "
        "métodos auxiliares.")
    d.codigo(
        "package com.aqualavado.modelo;\n"
        "\n"
        "/**\n"
        " * Representa una orden de lavado registrada en el establecimiento.\n"
        " */\n"
        "public class OrdenLavado {\n"
        "\n"
        "    public static final String ESTADO_EN_COLA = \"EN_COLA\";\n"
        "    public static final String ESTADO_EN_PROCESO = \"EN_PROCESO\";\n"
        "\n"
        "    private int idOrden;\n"
        "    private String placa;\n"
        "    private int idServicio;\n"
        "    private String estado;\n"
        "    private LocalDateTime fechaIngreso;\n"
        "\n"
        "    public OrdenLavado() {\n"
        "    }\n"
        "\n"
        "    public int getIdOrden() {\n"
        "        return idOrden;\n"
        "    }\n"
        "\n"
        "    public void setIdOrden(int idOrden) {\n"
        "        this.idOrden = idOrden;\n"
        "    }\n"
        "}"
    )
    d.p("Las clases de acceso a datos agregan el sufijo DAO, las clases de servicio el "
        "sufijo Servicio y los servlets el sufijo Servlet. Una clase pública ocupa un "
        "archivo propio y su nombre coincide exactamente con el nombre del archivo.")

    d.h2("6. Declaración de métodos")
    d.p("Los métodos se nombran con un verbo que describe la acción y se declaran con "
        "el menor número de parámetros posible. Deben tener una única responsabilidad y "
        "documentar su propósito, sus parámetros, su valor de retorno y las excepciones "
        "que pueden generar.")
    d.codigo(
        "/**\n"
        " * Registra una orden de lavado y calcula el valor a pagar.\n"
        " *\n"
        " * @param orden datos de la orden de lavado\n"
        " * @return identificador asignado a la orden\n"
        " * @throws SQLException si ocurre un error al acceder a la base de datos\n"
        " */\n"
        "public int registrarOrden(OrdenLavado orden) throws SQLException {\n"
        "    validarOrden(orden);\n"
        "    return ordenDAO.insertar(orden);\n"
        "}"
    )
    d.tabla(
        ["Regla", "Aplicación"],
        [
            ["Nombre", "Verbo en infinitivo seguido del objeto: registrarCliente, listarOrdenes, actualizarServicio."],
            ["Parámetros", "Máximo cuatro; si se requieren más, se agrupan en un objeto."],
            ["Retorno", "Se declara explícitamente; void solo cuando no hay resultado que entregar."],
            ["Excepciones", "Se declaran las excepciones verificadas y se documentan con @throws."],
            ["Tamaño", "Preferiblemente menos de 40 líneas; si crece, se divide en métodos auxiliares."],
            ["Visibilidad", "Privada por defecto; pública solo cuando hace parte de la interfaz de la clase."],
        ],
        anchos=[3.0, 12.6],
        caption="Reglas para la declaración de métodos.",
    )

    d.h2("7. Variables y constantes")
    d.p("Las variables se declaran en el lugar donde se utilizan y con el tipo más "
        "específico posible. No se declaran variables sin inicializar si pueden "
        "inicializarse al momento de la declaración, y no se reutiliza el mismo nombre "
        "para propósitos diferentes.")
    d.codigo(
        "// Correcto\n"
        "double valorServicio = 32000.0;\n"
        "int cantidadLavados = 0;\n"
        "final int CAPACIDAD_DIARIA = 40;\n"
        "\n"
        "// Incorrecto\n"
        "double x = 32000.0;\n"
        "int a, b, c;\n"
        "final int capacidad = 40;"
    )
    d.p("Las constantes se declaran con final, en mayúsculas y con guion bajo. Los "
        "valores que representan estados del negocio se agrupan en constantes o en "
        "enumeraciones para evitar cadenas de texto repetidas.")

    d.h2("8. Comentarios y documentación")
    d.bullets([
        "La documentación de clases y métodos públicos se escribe con JavaDoc.",
        "Los comentarios explican el porqué de una decisión, no repiten lo que el código ya dice.",
        "No se conservan comentarios obsoletos ni bloques de código comentado.",
        "Las tareas pendientes se registran en el gestor de incidencias, no en el código.",
        "En React se documentan los componentes con una descripción breve de sus props y su comportamiento.",
        "En SQL se documentan las tablas y las columnas con la cláusula COMMENT cuando aporta claridad.",
    ])

    d.h2("9. Manejo de excepciones y recursos")
    d.p("Las excepciones se capturan únicamente cuando se puede hacer algo con ellas: "
        "informar al usuario, registrar el error o revertir una transacción. Nunca se "
        "deja un bloque catch vacío. Los recursos de base de datos se cierran con "
        "try-with-resources para evitar fugas de conexiones.")
    d.codigo(
        "public List<Cliente> listar() throws SQLException {\n"
        "    String sql = \"SELECT id_cliente, nombre, telefono FROM clientes ORDER BY nombre\";\n"
        "    List<Cliente> clientes = new ArrayList<>();\n"
        "    try (Connection conexion = ConexionBD.obtener();\n"
        "         PreparedStatement sentencia = conexion.prepareStatement(sql);\n"
        "         ResultSet resultado = sentencia.executeQuery()) {\n"
        "        while (resultado.next()) {\n"
        "            clientes.add(mapear(resultado));\n"
        "        }\n"
        "    }\n"
        "    return clientes;\n"
        "}"
    )

    d.h2("10. Estándares de base de datos y JDBC")
    d.tabla(
        ["Regla", "Descripción"],
        [
            ["Nombres", "Tablas en plural y minúsculas; columnas en singular y minúsculas; llaves primarias con el nombre id_entidad."],
            ["Llaves foráneas", "Nombre fk_tabla_origen_tabla_destino y acción explícita ON DELETE y ON UPDATE."],
            ["Tipos", "DECIMAL para valores monetarios, DATE o DATETIME para fechas, VARCHAR con longitud justificada."],
            ["Consultas", "Siempre con PreparedStatement y parámetros, nunca concatenando texto del usuario."],
            ["Transacciones", "Se agrupan las operaciones que deben ejecutarse de forma atómica y se confirman o revierten."],
            ["Recursos", "Conexiones, sentencias y resultados se cierran con try-with-resources."],
            ["Scripts", "Versionados en la carpeta base-datos y con nombre descriptivo."],
        ],
        anchos=[3.2, 12.4],
        caption="Estándares para la base de datos y JDBC.",
    )

    d.h2("11. Estándares del front-end con React")
    d.bullets([
        "Cada componente se declara como función y en un archivo con su mismo nombre en PascalCase.",
        "Las props se reciben por desestructuración y se documentan cuando el componente es reutilizable.",
        "El estado local se maneja con useState y los efectos con useEffect, sin modificar el estado directamente.",
        "Los eventos se nombran con el prefijo manejar: manejarEnvio, manejarCambio, manejarClic.",
        "Las clases CSS se escriben en minúsculas y con guion: tabla-ordenes, boton-principal.",
        "Las llamadas a la API se centralizan en un módulo de servicios y manejan los estados de carga y error.",
        "Los componentes se organizan por dominio: componentes/comunes, componentes/ordenes, componentes/clientes.",
    ])
    d.codigo(
        "export default function EstadoOrden({ estado }) {\n"
        "  const estilos = {\n"
        "    EN_COLA: 'estado estado-cola',\n"
        "    EN_PROCESO: 'estado estado-proceso',\n"
        "    FINALIZADO: 'estado estado-finalizado'\n"
        "  };\n"
        "\n"
        "  return <span className={estilos[estado]}>{estado}</span>;\n"
        "}")

    d.h2("12. Estándares de versionamiento")
    d.tabla(
        ["Aspecto", "Regla"],
        [
            ["Rama principal", "main conserva el código estable y siempre compilable."],
            ["Ramas de trabajo", "feature/nombre-funcionalidad, fix/nombre-error, docs/nombre-documento."],
            ["Commits", "Mensajes en imperativo y con prefijo: feat, fix, docs, test, chore."],
            ["Tamaño", "Un commit por cambio coherente; se evita mezclar refactorizaciones con funcionalidades."],
            ["Revisión", "Todo cambio se integra mediante pull request revisado."],
            ["Archivos ignorados", ".gitignore excluye binarios, dependencias, configuraciones locales y respaldos."],
        ],
        anchos=[3.4, 12.2],
        caption="Estándares de control de versiones.",
    )

    d.h2("13. Verificación de los estándares")
    d.p("El cumplimiento de los estándares se verifica con herramientas automáticas y "
        "con la revisión de código. La siguiente tabla relaciona las herramientas "
        "previstas y el aspecto que controlan.")
    d.tabla(
        ["Herramienta", "Aspecto que verifica"],
        [
            ["EditorConfig", "Indentación, codificación y fin de línea."],
            ["Checkstyle", "Convenciones de nombres, estructura y documentación en Java."],
            ["ESLint", "Reglas de estilo y errores frecuentes en JavaScript y React."],
            ["Prettier", "Formato uniforme de archivos JavaScript, JSX, CSS y JSON."],
            ["Revisión de pares", "Legibilidad, diseño, seguridad y cumplimiento de las reglas."],
        ],
        anchos=[4.0, 11.6],
        caption="Herramientas de verificación de estándares.",
    )

    d.conclusion([
        "La definición de estándares de codificación proporciona al proyecto "
        "AquaLavado un lenguaje común para escribir y revisar el código. Las reglas de "
        "nombramiento, la estructura de clases y métodos, el manejo de excepciones y las "
        "convenciones de base de datos reducen la ambigüedad y facilitan el mantenimiento "
        "del software.",
        "La aplicación de estos estándares en Java, React y SQL permite que los módulos "
        "desarrollados por diferentes integrantes se integren con menor esfuerzo. Además, "
        "la verificación automática y la revisión entre pares convierten los estándares "
        "en un mecanismo de calidad verificable dentro del repositorio.",
    ])

    d.bibliografia([
        "Airbnb. (2023). JavaScript style guide. https://github.com/airbnb/javascript",
        "Conventional Commits. (2023). Conventional Commits 1.0.0. https://www.conventionalcommits.org/es/v1.0.0/",
        "Google. (2025). Google Java Style Guide. https://google.github.io/styleguide/javaguide.html",
        "Meta. (2024). React: Reference. https://react.dev/reference/react",
        "MySQL. (2024). MySQL 8.0 reference manual. https://dev.mysql.com/doc/refman/8.0/en/",
        "Oracle. (1999). Code conventions for the Java programming language. https://www.oracle.com/java/technologies/javase/codeconventions-contents.html",
        "Oracle. (2025). JDBC API specification. https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/",
    ])
    return d.guardar()


def ev03():
    d = SenaDoc(
        "GA7-220501096-AA1-EV03",
        "Identifica herramientas de versionamiento",
        FECHA,
    )
    d.intro([
        "El control de versiones es una práctica indispensable en el desarrollo de "
        "software porque permite registrar la evolución del código, recuperar versiones "
        "anteriores y coordinar el trabajo de varias personas sobre un mismo proyecto. "
        "Git organiza esta labor en dos ámbitos complementarios: el repositorio local, "
        "ubicado en el equipo del desarrollador, y el repositorio remoto, alojado en un "
        "servicio como GitHub.",
        "En esta evidencia se identifican las características del versionamiento local y "
        "remoto, se establecen sus diferencias y se relacionan los comandos básicos de "
        "Git que se utilizan en cada caso. Los conceptos se aplican al repositorio del "
        "proyecto AquaLavado, sistema de gestión de lavadero de vehículos.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Identificar las herramientas y los comandos de versionamiento local y remoto, "
        "estableciendo las diferencias entre ambos entornos y su aplicación en el "
        "control de cambios del proyecto AquaLavado.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Describir el funcionamiento del repositorio local y del repositorio remoto.",
        "Comparar las características, ventajas y limitaciones de cada entorno.",
        "Relacionar los comandos básicos de Git local y Git remoto con su propósito.",
        "Explicar el flujo de trabajo entre el equipo del desarrollador y GitHub.",
    ])

    d.h2("2. Control de versiones")
    d.p("El control de versiones es un sistema que registra los cambios realizados sobre "
        "los archivos de un proyecto a lo largo del tiempo, de manera que sea posible "
        "consultar quién modificó cada línea, cuándo lo hizo y por qué. Git es un sistema "
        "distribuido: cada desarrollador posee una copia completa del historial, lo que "
        "permite trabajar sin conexión y sincronizar los cambios cuando sea necesario.")
    d.p("En Git existen tres áreas principales: el directorio de trabajo, donde se "
        "modifican los archivos; el área de preparación (staging), donde se seleccionan "
        "los cambios que harán parte del siguiente commit; y el repositorio local, donde "
        "se almacena el historial confirmado. El repositorio remoto es una copia "
        "adicional que se sincroniza mediante operaciones de envío y recepción.")

    d.h2("3. Git local y Git remoto")
    d.h3("3.1 Git local")
    d.p("El repositorio local reside en el equipo del desarrollador y se crea con el "
        "comando git init o se obtiene mediante git clone. Contiene todos los commits, "
        "ramas y etiquetas del proyecto, por lo que permite consultar el historial, "
        "crear ramas, comparar versiones y revertir cambios sin conexión a Internet.")
    d.h3("3.2 Git remoto")
    d.p("El repositorio remoto se aloja en un servidor como GitHub, GitLab o Bitbucket. "
        "Su función es centralizar el trabajo del equipo, respaldar el código y facilitar "
        "la colaboración mediante ramas compartidas, pull requests y revisiones. El "
        "repositorio remoto no reemplaza al local: ambos se sincronizan con fetch, pull y "
        "push.")

    d.h2("4. Diferencias entre Git local y Git remoto")
    d.tabla(
        ["Criterio", "Git local", "Git remoto"],
        [
            ["Ubicación", "En el equipo del desarrollador.", "En un servidor o servicio en la nube."],
            ["Creación", "git init o git clone.", "Se crea en GitHub y se enlaza con git remote add."],
            ["Alcance", "Historial y ramas del equipo local.", "Copia compartida del historial y las ramas."],
            ["Conexión", "Funciona sin Internet.", "Requiere conexión para sincronizar."],
            ["Velocidad", "Operaciones inmediatas.", "Depende de la red y del tamaño de los cambios."],
            ["Colaboración", "Individual o mediante archivos compartidos.", "Múltiples desarrolladores con permisos."],
            ["Respaldo", "Depende del equipo y de sus copias.", "Copia central disponible en el servicio."],
            ["Integración", "Commit, branch, merge, rebase.", "Push, pull, fetch, pull request."],
            ["Control de acceso", "Control del sistema operativo.", "Autenticación y permisos por repositorio."],
            ["Uso principal", "Trabajar y versionar los cambios.", "Compartir, revisar y respaldar el proyecto."],
        ],
        anchos=[3.4, 6.2, 6.0],
        caption="Diferencias entre el repositorio local y el repositorio remoto.",
        size=7.5,
    )

    d.h2("5. Comandos básicos de Git local")
    d.p("Los comandos locales operan sobre el directorio de trabajo y el repositorio del "
        "equipo. Se ejecutan en la terminal, dentro de la carpeta del proyecto.")
    d.tabla(
        ["Comando", "Función", "Ejemplo"],
        [
            ["git init", "Crea un repositorio local en la carpeta actual.", "git init"],
            ["git status", "Muestra el estado de los archivos y los cambios pendientes.", "git status"],
            ["git add", "Agrega cambios al área de preparación.", "git add ."],
            ["git commit", "Registra los cambios preparados con un mensaje.", 'git commit -m "feat: registro de orden"'],
            ["git log", "Muestra el historial de confirmaciones.", "git log --oneline --graph"],
            ["git diff", "Compara los cambios entre el directorio y el repositorio.", "git diff"],
            ["git branch", "Lista, crea o elimina ramas.", "git branch feature/ordenes"],
            ["git switch", "Cambia de rama de trabajo.", "git switch feature/ordenes"],
            ["git merge", "Integra una rama en la rama actual.", "git merge feature/ordenes"],
            ["git restore", "Descarta cambios de un archivo o lo saca del área de preparación.", "git restore index.html"],
            ["git reset", "Mueve el puntero de la rama a un commit anterior.", "git reset --soft HEAD~1"],
            ["git stash", "Guarda temporalmente cambios no confirmados.", "git stash"],
            ["git tag", "Marca un commit con una etiqueta de versión.", "git tag v1.0.0"],
        ],
        anchos=[2.8, 7.6, 5.2],
        caption="Comandos básicos de Git local.",
        size=7.5,
    )

    d.h2("6. Comandos básicos de Git remoto")
    d.p("Los comandos remotos permiten enlazar el repositorio local con un servidor, "
        "enviar y recibir cambios y consultar las ramas publicadas.")
    d.tabla(
        ["Comando", "Función", "Ejemplo"],
        [
            ["git remote add", "Enlaza el repositorio local con uno remoto.", "git remote add origin https://github.com/usuario/repositorio.git"],
            ["git remote -v", "Lista los repositorios remotos configurados.", "git remote -v"],
            ["git clone", "Copia un repositorio remoto en el equipo.", "git clone https://github.com/usuario/repositorio.git"],
            ["git fetch", "Descarga los cambios del remoto sin fusionarlos.", "git fetch origin"],
            ["git pull", "Descarga y fusiona los cambios del remoto.", "git pull origin main"],
            ["git push", "Envía los commits locales al repositorio remoto.", "git push origin main"],
            ["git branch -r", "Lista las ramas del repositorio remoto.", "git branch -r"],
            ["git remote remove", "Elimina la conexión con un repositorio remoto.", "git remote remove origin"],
        ],
        anchos=[3.4, 7.0, 5.2],
        caption="Comandos básicos de Git remoto.",
        size=7.5,
    )

    d.h2("7. Flujo de trabajo entre local y remoto")
    d.p("El trabajo diario combina operaciones locales y remotas. El siguiente flujo "
        "resume la secuencia que se aplica en el proyecto AquaLavado.")
    d.numeros([
        "Clonar el repositorio remoto o actualizar la copia local con git pull.",
        "Crear una rama de trabajo con git switch -c feature/nombre-funcionalidad.",
        "Modificar los archivos y revisar el estado con git status.",
        "Preparar los cambios con git add y confirmarlos con git commit.",
        "Publicar la rama con git push -u origin feature/nombre-funcionalidad.",
        "Abrir un pull request en GitHub y solicitar la revisión.",
        "Integrar la rama en main y actualizar la copia local con git pull.",
    ])
    d.codigo(
        "git clone https://github.com/DylanA-dev/Proyecto-Adso-Lavadero.git\n"
        "cd Proyecto-Adso-Lavadero\n"
        "git switch -c feature/registro-ordenes\n"
        "git add .\n"
        "git commit -m \"feat: registro de ordenes de lavado\"\n"
        "git push -u origin feature/registro-ordenes"
    )

    d.h2("8. Aplicación en el proyecto AquaLavado")
    d.p("El repositorio del proyecto se encuentra en " + REPO + ". La rama main "
        "conserva las versiones estables y las ramas feature agrupan el desarrollo de "
        "cada módulo: clientes, servicios, órdenes, procesos y reportes. Los mensajes de "
        "commit describen el cambio realizado y facilitan la trazabilidad entre el código "
        "y las evidencias del proyecto.")
    d.tabla(
        ["Rama", "Propósito"],
        [
            ["main", "Código estable y entregable."],
            ["feature/clientes", "Módulo de clientes y vehículos."],
            ["feature/ordenes", "Registro y control de órdenes de lavado."],
            ["feature/frontend", "Componentes React y versión móvil."],
            ["fix/validaciones", "Corrección de validaciones y errores detectados en pruebas."],
        ],
        anchos=[5.0, 10.6],
        caption="Ramas de trabajo del repositorio AquaLavado.",
    )

    d.h2("9. Buenas prácticas de versionamiento")
    d.bullets([
        "Confirmar cambios pequeños y con un propósito claro.",
        "Escribir mensajes de commit en imperativo y con prefijo semántico.",
        "Actualizar la rama local antes de comenzar una nueva funcionalidad.",
        "No publicar contraseñas, archivos de configuración local ni binarios generados.",
        "Revisar los cambios con git diff antes de confirmarlos.",
        "Mantener la rama main siempre compilable y probada.",
        "Etiquetar las versiones entregadas para identificar hitos del proyecto.",
    ])

    d.conclusion([
        "Git local y Git remoto cumplen funciones complementarias dentro del ciclo de "
        "desarrollo. El repositorio local permite trabajar, experimentar y conservar el "
        "historial detallado de cada cambio; el repositorio remoto centraliza el trabajo "
        "del equipo, respalda el código y facilita la revisión y la colaboración.",
        "El dominio de los comandos básicos de ambos entornos permite aplicar un flujo de "
        "trabajo ordenado en AquaLavado, donde cada funcionalidad se desarrolla en una "
        "rama, se documenta con mensajes claros y se integra mediante revisión. Esta "
        "práctica garantiza la trazabilidad del proyecto y la conservación de su "
        "historial.",
    ])

    d.bibliografia([
        "Chacon, S. y Straub, B. (2014). Pro Git (2.ª ed.). Apress. https://git-scm.com/book/es/v2",
        "Git. (2025). Git reference. https://git-scm.com/docs",
        "GitHub. (2026). GitHub Docs: Repositories. https://docs.github.com/es/repositories",
        "GitHub. (2026). GitHub Docs: About branches. https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches",
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
