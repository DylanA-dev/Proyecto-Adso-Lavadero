# -*- coding: utf-8 -*-
"""Documentos de la actividad GA7-220501096-AA2 (codificación de módulos)."""
import sys

from sena_doc import SenaDoc

FECHA = "Noviembre 2026"
REPO = "https://github.com/DylanA-dev/Proyecto-Adso-Lavadero"
CAPTURAS = r"C:\Users\dylan\Documents\OpenCode\ADSO\proyectos\lavadero\interfaz\capturas"


def ev01():
    d = SenaDoc(
        "GA7-220501096-AA2-EV01",
        "Codificación de módulos del software",
        FECHA,
    )
    d.intro([
        "La codificación de los módulos de un sistema de información requiere articular "
        "el diseño elaborado en las fases anteriores con una tecnología de persistencia "
        "que garantice la integridad de los datos. En esta evidencia se presenta la "
        "codificación del módulo de gestión de clientes, vehículos, servicios y órdenes "
        "de lavado del sistema AquaLavado, implementado en Java con conexión a una base "
        "de datos MySQL mediante JDBC.",
        "El documento describe la arquitectura del módulo, el modelo relacional, la "
        "conexión JDBC, las operaciones de inserción, consulta, actualización y "
        "eliminación, los estándares de codificación aplicados y las pruebas ejecutadas. "
        "El código fuente se encuentra versionado en el repositorio del proyecto y se "
        "entrega junto con el script de la base de datos y las instrucciones de "
        "ejecución.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Codificar el módulo de gestión de AquaLavado en Java, estableciendo la conexión "
        "con la base de datos MySQL por medio de JDBC e implementando las operaciones de "
        "inserción, consulta, actualización y eliminación, de acuerdo con el diseño y los "
        "estándares de codificación del proyecto.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Implementar el modelo relacional del sistema en MySQL.",
        "Establecer la conexión JDBC y centralizar su configuración en una clase reutilizable.",
        "Codificar las clases del modelo y los objetos de acceso a datos con operaciones CRUD.",
        "Aplicar consultas parametrizadas y cierre automático de recursos.",
        "Ejecutar pruebas de inserción, consulta, actualización y eliminación sobre la base de datos.",
        "Versionar el código y documentar su ejecución en el repositorio del proyecto.",
    ])

    d.h2("2. Artefactos de entrada")
    d.p("La codificación toma como base los artefactos elaborados en las fases de análisis "
        "y diseño del proyecto formativo. La siguiente tabla relaciona cada artefacto con "
        "su aplicación en el módulo.")
    d.tabla(
        ["Artefacto", "Aplicación en la codificación"],
        [
            ["Historias de usuario", "Definen las operaciones de registro, consulta, actualización y eliminación de clientes, vehículos, servicios y órdenes."],
            ["Diagrama de casos de uso", "Establece las acciones del administrador y del operario sobre cada módulo."],
            ["Diagrama de clases", "Orienta la creación de las clases Cliente, Vehiculo, Servicio y OrdenLavado."],
            ["Diseño de la base de datos", "Define las tablas, llaves primarias, llaves foráneas y restricciones de integridad."],
            ["Prototipos e interfaz", "Determinan los datos que debe capturar y mostrar cada módulo."],
            ["Informe técnico del plan de trabajo", "Fija las tecnologías, los estándares y el flujo de versionamiento."],
        ],
        anchos=[4.2, 11.4],
        caption="Artefactos de entrada del módulo de codificación.",
    )

    d.h2("3. Arquitectura del módulo")
    d.p("El módulo se organiza con el patrón DAO (Data Access Object), que separa las "
        "clases del modelo de las operaciones de acceso a datos. Esta separación permite "
        "reutilizar la lógica de persistencia en la aplicación de escritorio, en la "
        "aplicación web y en los servicios, y facilita las pruebas de cada capa.")
    d.tabla(
        ["Capa", "Clases", "Responsabilidad"],
        [
            ["Conexión", "ConexionBD", "Abrir conexiones JDBC con la configuración del sistema."],
            ["Modelo", "Cliente, Vehiculo, Servicio, OrdenLavado, Usuario", "Representar las entidades del negocio."],
            ["Acceso a datos", "ClienteDAO, VehiculoDAO, ServicioDAO, OrdenLavadoDAO, UsuarioDAO", "Ejecutar las operaciones CRUD y mapear los resultados."],
            ["Aplicación", "Principal", "Ofrecer el menú de operación por consola."],
            ["Pruebas", "PruebasCRUD", "Verificar el ciclo completo de persistencia."],
        ],
        anchos=[3.4, 7.0, 5.2],
        caption="Capas y clases del módulo JDBC.",
    )

    d.h2("4. Modelo de datos")
    d.p("La base de datos aqualavado se compone de seis tablas relacionadas. El modelo "
        "registra los clientes y sus vehículos, los servicios ofrecidos, las órdenes de "
        "lavado generadas en la entrada del vehículo y los pagos realizados en la "
        "entrega.")
    d.tabla(
        ["Tabla", "Campos principales", "Relación"],
        [
            ["usuarios", "id_usuario, nombre, correo, clave_hash, rol, activo", "Origen de las órdenes asignadas a un operario."],
            ["clientes", "id_cliente, documento, nombre, teléfono, correo, dirección", "Un cliente puede tener varios vehículos."],
            ["vehiculos", "id_vehiculo, placa, marca, modelo, color, id_cliente", "Pertenece a un cliente."],
            ["servicios", "id_servicio, nombre, descripción, precio, duración, activo", "Se asocia a las órdenes de lavado."],
            ["ordenes_lavado", "id_orden, id_vehiculo, id_servicio, id_operario, fechas, estado, valor", "Relaciona vehículo, servicio y operario."],
            ["pagos", "id_pago, id_orden, método, valor, fecha_pago", "Registra el pago de una orden entregada."],
        ],
        anchos=[3.4, 8.6, 3.6],
        caption="Tablas del modelo relacional de AquaLavado.",
        size=7.5,
    )
    d.p("Los estados de una orden son EN_COLA, EN_PROCESO, FINALIZADO y ENTREGADO. La "
        "fecha de salida se registra cuando la orden pasa a ENTREGADO y el pago se "
        "almacena en la tabla pagos. Las llaves foráneas restringen la eliminación de "
        "registros que tengan órdenes asociadas, con el fin de conservar la integridad "
        "del historial.")
    d.imagen(f"{CAPTURAS}\\bd_esquema.png",
             "Tablas de la base de datos y órdenes registradas.", 15.0)

    d.h2("5. Conexión JDBC")
    d.p("La clase ConexionBD centraliza la URL, el usuario y la clave de la base de datos. "
        "La configuración se puede sobrescribir con propiedades del sistema, lo que "
        "permite ejecutar el mismo código en diferentes entornos. El controlador de MySQL "
        "se carga de forma explícita para garantizar su registro en cualquier contenedor "
        "de servlets.")
    d.codigo(
        "public final class ConexionBD {\n"
        "\n"
        "    private static final String URL = System.getProperty(\n"
        "            \"aqualavado.url\",\n"
        "            \"jdbc:mysql://localhost:3306/aqualavado?useSSL=false\"\n"
        "                    + \"&allowPublicKeyRetrieval=true\"\n"
        "                    + \"&serverTimezone=America/Bogota\"\n"
        "                    + \"&characterEncoding=UTF-8\");\n"
        "\n"
        "    static {\n"
        "        try {\n"
        "            Class.forName(\"com.mysql.cj.jdbc.Driver\");\n"
        "        } catch (ClassNotFoundException error) {\n"
        "            throw new IllegalStateException(\n"
        "                    \"No se encontró el controlador JDBC de MySQL.\", error);\n"
        "        }\n"
        "    }\n"
        "\n"
        "    public static Connection obtener() throws SQLException {\n"
        "        return DriverManager.getConnection(URL, USUARIO, CLAVE);\n"
        "    }\n"
        "}")

    d.h2("6. Operaciones CRUD")
    d.p("Cada DAO implementa las operaciones de inserción, consulta, actualización y "
        "eliminación con PreparedStatement, lo que evita la concatenación de valores en "
        "las consultas y reduce el riesgo de inyección SQL. Los recursos se cierran con "
        "try-with-resources.")
    d.h3("6.1 Inserción")
    d.codigo(
        "public int insertar(Cliente cliente) throws SQLException {\n"
        "    String sql = \"INSERT INTO clientes (documento, nombre, telefono, \"\n"
        "            + \"correo, direccion) VALUES (?, ?, ?, ?, ?)\";\n"
        "    try (Connection conexion = ConexionBD.obtener();\n"
        "         PreparedStatement sentencia = conexion.prepareStatement(\n"
        "                 sql, Statement.RETURN_GENERATED_KEYS)) {\n"
        "        sentencia.setString(1, cliente.getDocumento());\n"
        "        sentencia.setString(2, cliente.getNombre());\n"
        "        sentencia.setString(3, cliente.getTelefono());\n"
        "        sentencia.setString(4, cliente.getCorreo());\n"
        "        sentencia.setString(5, cliente.getDireccion());\n"
        "        sentencia.executeUpdate();\n"
        "        try (ResultSet claves = sentencia.getGeneratedKeys()) {\n"
        "            if (claves.next()) {\n"
        "                cliente.setIdCliente(claves.getInt(1));\n"
        "            }\n"
        "        }\n"
        "        return cliente.getIdCliente();\n"
        "    }\n"
        "}")
    d.h3("6.2 Consulta")
    d.codigo(
        "public List<Cliente> listar() throws SQLException {\n"
        "    String sql = \"SELECT id_cliente, documento, nombre, telefono, \"\n"
        "            + \"correo, direccion FROM clientes ORDER BY nombre\";\n"
        "    List<Cliente> clientes = new ArrayList<>();\n"
        "    try (Connection conexion = ConexionBD.obtener();\n"
        "         PreparedStatement sentencia = conexion.prepareStatement(sql);\n"
        "         ResultSet resultado = sentencia.executeQuery()) {\n"
        "        while (resultado.next()) {\n"
        "            clientes.add(mapear(resultado));\n"
        "        }\n"
        "    }\n"
        "    return clientes;\n"
        "}")
    d.h3("6.3 Actualización")
    d.codigo(
        "public boolean actualizar(Cliente cliente) throws SQLException {\n"
        "    String sql = \"UPDATE clientes SET documento = ?, nombre = ?, \"\n"
        "            + \"telefono = ?, correo = ?, direccion = ? \"\n"
        "            + \"WHERE id_cliente = ?\";\n"
        "    try (Connection conexion = ConexionBD.obtener();\n"
        "         PreparedStatement sentencia = conexion.prepareStatement(sql)) {\n"
        "        sentencia.setString(1, cliente.getDocumento());\n"
        "        sentencia.setString(2, cliente.getNombre());\n"
        "        sentencia.setString(3, cliente.getTelefono());\n"
        "        sentencia.setString(4, cliente.getCorreo());\n"
        "        sentencia.setString(5, cliente.getDireccion());\n"
        "        sentencia.setInt(6, cliente.getIdCliente());\n"
        "        return sentencia.executeUpdate() > 0;\n"
        "    }\n"
        "}")
    d.h3("6.4 Eliminación")
    d.codigo(
        "public boolean eliminar(int idCliente) throws SQLException {\n"
        "    try (Connection conexion = ConexionBD.obtener();\n"
        "         PreparedStatement sentencia = conexion.prepareStatement(\n"
        "                 \"DELETE FROM clientes WHERE id_cliente = ?\")) {\n"
        "        sentencia.setInt(1, idCliente);\n"
        "        return sentencia.executeUpdate() > 0;\n"
        "    }\n"
        "}")
    d.p("La misma estructura se aplica a vehículos, servicios y órdenes. El DAO de "
        "órdenes incluye una consulta con tres uniones para recuperar la placa del "
        "vehículo, el nombre del servicio y el nombre del operario, además de la "
        "operación cambiarEstado, que actualiza el estado y registra la fecha de salida "
        "cuando la orden se entrega.")

    d.h2("7. Estándares aplicados")
    d.bullets([
        "Paquetes en minúsculas con el dominio invertido: com.aqualavado.conexion, com.aqualavado.dao, com.aqualavado.modelo.",
        "Clases en PascalCase y en singular: Cliente, OrdenLavado, ClienteDAO.",
        "Métodos en camelCase con verbo: insertar, listar, buscarPorId, actualizar, eliminar.",
        "Constantes en mayúsculas: ESTADO_EN_COLA, ESTADO_EN_PROCESO.",
        "Consultas parametrizadas con PreparedStatement en todas las operaciones.",
        "Cierre de conexiones, sentencias y resultados con try-with-resources.",
        "Documentación JavaDoc en clases y métodos públicos.",
        "Manejo de excepciones con SQLException y mensajes claros para el usuario.",
    ])

    d.h2("8. Estructura del proyecto")
    d.codigo(
        "jdbc/\n"
        "├── src/com/aqualavado/\n"
        "│   ├── conexion/ConexionBD.java\n"
        "│   ├── modelo/Cliente.java, Vehiculo.java, Servicio.java, OrdenLavado.java\n"
        "│   ├── dao/ClienteDAO.java, VehiculoDAO.java, ServicioDAO.java, OrdenLavadoDAO.java\n"
        "│   ├── app/Principal.java\n"
        "│   └── pruebas/PruebasCRUD.java\n"
        "├── compilar.bat\n"
        "├── ejecutar.bat\n"
        "└── ejecutar-pruebas.bat"
    )

    d.h2("9. Pruebas ejecutadas")
    d.p("Se ejecutó la clase PruebasCRUD, que recorre el ciclo completo de persistencia "
        "sobre la base de datos real. La prueba crea un cliente, lo consulta, actualiza su "
        "teléfono, registra un vehículo y un servicio, genera una orden, cambia su estado "
        "a EN_PROCESO y ENTREGADO y, finalmente, elimina los registros creados. El "
        "resultado se presenta en la siguiente tabla.")
    d.tabla(
        ["Grupo", "Pruebas", "Resultado"],
        [
            ["Conexión", "Apertura de la conexión con la base de datos aqualavado.", "Aprobada"],
            ["Clientes", "Insertar, consultar, actualizar y verificar la actualización.", "4 aprobadas"],
            ["Vehículos", "Insertar y consultar el vehículo con su cliente.", "2 aprobadas"],
            ["Servicios", "Insertar y actualizar el precio del servicio.", "2 aprobadas"],
            ["Órdenes", "Insertar, cambiar a EN_PROCESO, cambiar a ENTREGADO y consultar.", "4 aprobadas"],
            ["Eliminación", "Eliminar orden, servicio, vehículo y cliente, y confirmar.", "5 aprobadas"],
        ],
        anchos=[3.0, 10.4, 2.2],
        caption="Resultados de las pruebas CRUD.",
    )
    d.p("El total fue de 18 pruebas aprobadas y 0 fallidas, con resultado final APROBADO. "
        "La evidencia de ejecución se muestra a continuación.")
    d.imagen(f"{CAPTURAS}\\jdbc_pruebas.png",
             "Ejecución de las pruebas CRUD con JDBC.", 15.5)

    d.h2("10. Ejecución del módulo")
    d.p("El proyecto se compila y se ejecuta desde la carpeta jdbc. Los scripts incluidos "
        "configuran la codificación UTF-8 y el classpath con el controlador de MySQL.")
    d.codigo(
        "compilar.bat\n"
        "ejecutar-pruebas.bat\n"
        "ejecutar.bat"
    )
    d.p("El script ejecutar.bat abre el menú de operación, desde el cual se pueden listar "
        "clientes, registrar clientes, actualizar su teléfono, eliminar clientes, listar "
        "vehículos, registrar vehículos, consultar servicios, listar órdenes, registrar "
        "una orden y avanzar su estado.")

    d.h2("11. Repositorio y entrega")
    d.p("El código se encuentra versionado en el repositorio " + REPO + ", en la carpeta "
        "jdbc. La entrega se realiza en un archivo comprimido que contiene los archivos "
        "del proyecto, el script de la base de datos, el controlador JDBC y un archivo de "
        "texto con el enlace del repositorio.")
    d.tabla(
        ["Archivo", "Contenido"],
        [
            ["DylanArias_AA2_EV01.zip", "Carpeta jdbc, carpeta base-datos, controlador y enlace del repositorio."],
            ["ENLACE_REPOSITORIO.txt", "Dirección del repositorio en GitHub."],
            ["aqualavado.sql", "Script de creación de la base de datos y datos iniciales."],
        ],
        anchos=[5.6, 10.0],
        caption="Archivos de la entrega AA2-EV01.",
    )

    d.conclusion([
        "La codificación del módulo permitió implementar la persistencia del sistema "
        "AquaLavado con JDBC y MySQL, aplicando el patrón DAO y las operaciones CRUD "
        "requeridas. La separación entre el modelo, el acceso a datos y la aplicación "
        "facilita la reutilización del código en las versiones web y móvil del sistema.",
        "Las 18 pruebas ejecutadas sobre la base de datos confirmaron el funcionamiento "
        "de las operaciones y la integridad de las relaciones. El uso de consultas "
        "parametrizadas, el cierre automático de recursos y la documentación del código "
        "garantizan un módulo mantenible y alineado con los estándares definidos para el "
        "proyecto.",
    ])

    d.bibliografia([
        "Oracle. (2025). JDBC API specification. https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/",
        "MySQL. (2024). MySQL 8.0 reference manual. https://dev.mysql.com/doc/refman/8.0/en/",
        "Oracle. (2025). Java Platform, Standard Edition Documentation. https://docs.oracle.com/en/java/",
        "Gamma, E., Helm, R., Johnson, R. y Vlissides, J. (1994). Design patterns: Elements of reusable object-oriented software. Addison-Wesley.",
        "Sommerville, I. (2016). Software engineering (10.ª ed.). Pearson.",
    ])
    return d.guardar()


def ev02():
    d = SenaDoc(
        "GA7-220501096-AA2-EV02",
        "Módulos de software codificados y probados",
        FECHA,
    )
    d.intro([
        "La versión web del sistema AquaLavado se construyó con la tecnología de "
        "servlets y páginas JSP, ejecutada sobre el servidor Apache Tomcat. Esta "
        "tecnología permite recibir las peticiones del navegador, procesar las reglas del "
        "negocio en Java y generar las vistas con los datos almacenados en MySQL.",
        "En esta evidencia se presenta la codificación y las pruebas del módulo web: "
        "formularios HTML, servlets con métodos GET y POST, elementos JSP, control de "
        "sesión y acceso a datos mediante JDBC. El documento incluye la estructura del "
        "proyecto, los fragmentos de código más representativos y las capturas de las "
        "pantallas obtenidas durante la ejecución.",
    ])

    d.desarrollo()
    d.h2("1. Objetivo")
    d.p("Codificar y probar el módulo web del sistema AquaLavado con servlets, JSP y "
        "formularios HTML, integrado con la base de datos MySQL mediante JDBC y desplegado "
        "en Apache Tomcat.")
    d.p("**Objetivos específicos**")
    d.bullets([
        "Implementar formularios HTML para el inicio de sesión y el registro de clientes y órdenes.",
        "Codificar servlets que atiendan peticiones GET y POST.",
        "Construir las vistas con elementos JSP y hojas de estilo.",
        "Controlar la sesión del usuario y proteger las páginas internas.",
        "Verificar el funcionamiento de las operaciones sobre la base de datos.",
        "Desplegar la aplicación en Tomcat y documentar el proceso.",
    ])

    d.h2("2. Arquitectura web")
    d.p("La aplicación sigue el modelo de petición y respuesta propio de los servlets. El "
        "navegador envía una solicitud HTTP, el contenedor de servlets la dirige al "
        "servlet correspondiente, este ejecuta la lógica y consulta la base de datos, y "
        "finalmente reenvía la respuesta a una página JSP que presenta la información.")
    d.tabla(
        ["Componente", "Función", "Tecnología"],
        [
            ["Navegador", "Presenta los formularios y las tablas al usuario.", "HTML5 y CSS3"],
            ["Contenedor", "Recibe las peticiones y administra el ciclo de vida de los servlets.", "Apache Tomcat 8.5"],
            ["Controladores", "Procesan las acciones y aplican las reglas del negocio.", "Servlets Java"],
            ["Vistas", "Generan el HTML con los datos de la aplicación.", "JSP y scriptlets"],
            ["Persistencia", "Ejecuta las consultas y actualizaciones.", "JDBC y DAO"],
            ["Base de datos", "Almacena clientes, vehículos, servicios, órdenes y pagos.", "MySQL"],
        ],
        anchos=[3.2, 8.4, 4.0],
        caption="Componentes de la aplicación web.",
    )

    d.h2("3. Estructura del proyecto")
    d.codigo(
        "web-servlets/\n"
        "├── src/com/aqualavado/web/\n"
        "│   ├── LoginServlet.java\n"
        "│   ├── PanelServlet.java\n"
        "│   ├── ClienteServlet.java\n"
        "│   ├── OrdenServlet.java\n"
        "│   ├── ReporteServlet.java\n"
        "│   └── Sesion.java\n"
        "├── web/\n"
        "│   ├── index.jsp\n"
        "│   ├── css/estilo.css\n"
        "│   └── WEB-INF/\n"
        "│       ├── web.xml\n"
        "│       └── vistas/panel.jsp, clientes.jsp, ordenes.jsp, reportes.jsp\n"
        "├── compilar.bat\n"
        "└── desplegar.bat"
    )
    d.p("Las vistas internas se ubican dentro de WEB-INF para que no puedan solicitarse "
        "directamente desde el navegador; el acceso se realiza únicamente a través de los "
        "servlets, que verifican la sesión antes de reenviar la respuesta.")

    d.h2("4. Configuración de los servlets")
    d.p("El archivo web.xml declara los servlets y asigna la URL con la que se invoca cada "
        "uno. También define el tiempo de sesión y la página de bienvenida.")
    d.codigo(
        "<servlet>\n"
        "    <servlet-name>ClienteServlet</servlet-name>\n"
        "    <servlet-class>com.aqualavado.web.ClienteServlet</servlet-class>\n"
        "</servlet>\n"
        "<servlet-mapping>\n"
        "    <servlet-name>ClienteServlet</servlet-name>\n"
        "    <url-pattern>/ClienteServlet</url-pattern>\n"
        "</servlet-mapping>\n"
        "<session-config>\n"
        "    <session-timeout>30</session-timeout>\n"
        "</session-config>")

    d.h2("5. Formularios HTML")
    d.p("Los formularios se construyen con HTML5 y validaciones del lado del cliente: "
        "campos obligatorios, tipos de dato, longitudes máximas y patrones para documentos "
        "y teléfonos. El envío se realiza por el método POST y los listados por GET.")
    d.codigo(
        "<form method=\"post\" action=\"<%= request.getContextPath() %>/ClienteServlet\"\n"
        "      class=\"formulario\">\n"
        "    <div class=\"campo\">\n"
        "        <label for=\"documento\">Documento</label>\n"
        "        <input type=\"text\" id=\"documento\" name=\"documento\" required\n"
        "               maxlength=\"15\" pattern=\"[0-9]{6,15}\">\n"
        "    </div>\n"
        "    <div class=\"campo\">\n"
        "        <label for=\"nombre\">Nombre completo</label>\n"
        "        <input type=\"text\" id=\"nombre\" name=\"nombre\" required maxlength=\"80\">\n"
        "    </div>\n"
        "    <button type=\"submit\" class=\"boton-principal\">Guardar cliente</button>\n"
        "</form>")
    d.p("El formulario de órdenes utiliza listas desplegables para seleccionar el "
        "vehículo, el servicio y el operario. El valor de cada opción corresponde al "
        "identificador de la entidad, de modo que el servlet recibe los datos necesarios "
        "para registrar la orden y calcular el valor con el precio del servicio.")

    d.h2("6. Servlets y métodos GET y POST")
    d.p("Cada servlet extiende HttpServlet y sobrescribe doGet o doPost según la acción. "
        "El método GET se utiliza para consultar y listar información, mientras que POST "
        "se emplea para registrar datos y evitar que los valores viajen en la URL.")
    d.h3("6.1 Inicio de sesión (POST)")
    d.codigo(
        "protected void doPost(HttpServletRequest solicitud, HttpServletResponse respuesta)\n"
        "        throws ServletException, IOException {\n"
        "    solicitud.setCharacterEncoding(\"UTF-8\");\n"
        "    String correo = solicitud.getParameter(\"correo\");\n"
        "    String clave = solicitud.getParameter(\"clave\");\n"
        "\n"
        "    Usuario usuario = usuarioDAO.autenticar(correo, clave);\n"
        "    if (usuario == null) {\n"
        "        solicitud.setAttribute(\"error\", \"Correo o contraseña incorrectos.\");\n"
        "        solicitud.getRequestDispatcher(\"/index.jsp\").forward(solicitud, respuesta);\n"
        "        return;\n"
        "    }\n"
        "    solicitud.getSession(true).setAttribute(\"usuario\", usuario);\n"
        "    respuesta.sendRedirect(solicitud.getContextPath() + \"/PanelServlet\");\n"
        "}")
    d.p("La autenticación se realiza con una consulta parametrizada que compara el correo "
        "y el hash SHA-256 de la contraseña. La contraseña no se almacena en texto plano "
        "en la base de datos.")
    d.h3("6.2 Registro de clientes (POST)")
    d.codigo(
        "protected void doPost(HttpServletRequest solicitud, HttpServletResponse respuesta)\n"
        "        throws ServletException, IOException {\n"
        "    solicitud.setCharacterEncoding(\"UTF-8\");\n"
        "    String accion = solicitud.getParameter(\"accion\");\n"
        "    if (\"eliminar\".equals(accion)) {\n"
        "        clienteDAO.eliminar(Integer.parseInt(solicitud.getParameter(\"id\")));\n"
        "    } else {\n"
        "        Cliente cliente = new Cliente(\n"
        "                solicitud.getParameter(\"documento\").trim(),\n"
        "                solicitud.getParameter(\"nombre\").trim(),\n"
        "                solicitud.getParameter(\"telefono\").trim(),\n"
        "                solicitud.getParameter(\"correo\").trim(),\n"
        "                solicitud.getParameter(\"direccion\").trim());\n"
        "        clienteDAO.insertar(cliente);\n"
        "    }\n"
        "    respuesta.sendRedirect(solicitud.getContextPath() + \"/ClienteServlet\");\n"
        "}")
    d.h3("6.3 Listado y avance de órdenes (GET)")
    d.codigo(
        "protected void doGet(HttpServletRequest solicitud, HttpServletResponse respuesta)\n"
        "        throws ServletException, IOException {\n"
        "    String accion = solicitud.getParameter(\"accion\");\n"
        "    if (\"avanzar\".equals(accion)) {\n"
        "        avanzar(Integer.parseInt(solicitud.getParameter(\"id\")));\n"
        "    }\n"
        "    solicitud.setAttribute(\"ordenes\", ordenDAO.listar());\n"
        "    solicitud.setAttribute(\"vehiculos\", vehiculoDAO.listar());\n"
        "    solicitud.setAttribute(\"servicios\", servicioDAO.listar());\n"
        "    solicitud.getRequestDispatcher(\"/WEB-INF/vistas/ordenes.jsp\")\n"
        "            .forward(solicitud, respuesta);\n"
        "}")

    d.h2("7. Elementos JSP")
    d.p("Las páginas JSP combinan HTML con elementos de Java. Se utilizan directivas para "
        "definir el tipo de contenido y las importaciones, scriptlets para recorrer las "
        "colecciones y expresiones para imprimir los valores. Además, se emplean "
        "inclusiones estáticas para reutilizar el encabezado y el pie de las páginas.")
    d.codigo(
        "<%@ page contentType=\"text/html; charset=UTF-8\" pageEncoding=\"UTF-8\" %>\n"
        "<%@ page import=\"java.util.List\" %>\n"
        "<%@ page import=\"com.aqualavado.modelo.Cliente\" %>\n"
        "<%@ include file=\"comun/encabezado.jsp\" %>\n"
        "\n"
        "<% List<Cliente> clientes = (List<Cliente>) request.getAttribute(\"clientes\"); %>\n"
        "\n"
        "<% for (Cliente cliente : clientes) { %>\n"
        "<tr>\n"
        "    <td><%= cliente.getDocumento() %></td>\n"
        "    <td><%= cliente.getNombre() %></td>\n"
        "    <td><%= cliente.getTelefono() %></td>\n"
        "</tr>\n"
        "<% } %>")

    d.h2("8. Sesión y seguridad")
    d.bullets([
        "La sesión se crea después de validar las credenciales y almacena el usuario autenticado.",
        "Cada servlet verifica la sesión antes de procesar la petición y redirige al inicio de sesión si no está activa.",
        "Las contraseñas se almacenan como hash SHA-256 y nunca se muestran en las vistas.",
        "Las consultas utilizan PreparedStatement para evitar la inyección SQL.",
        "Las vistas internas se ubican en WEB-INF para impedir el acceso directo.",
        "La codificación UTF-8 se configura en las peticiones y en las respuestas para conservar los caracteres especiales.",
    ])

    d.h2("9. Pantallas de la aplicación")
    d.p("A continuación se presentan las pantallas obtenidas durante la ejecución de la "
        "aplicación en Tomcat, con datos reales almacenados en MySQL.")
    d.imagen(f"{CAPTURAS}\\web_login.png",
             "Pantalla de inicio de sesión.", 13.5)
    d.imagen(f"{CAPTURAS}\\web_panel.png",
             "Panel principal con indicadores de la operación.", 14.5)
    d.imagen(f"{CAPTURAS}\\web_clientes.png",
             "Gestión de clientes: listado y formulario de registro.", 14.5)
    d.imagen(f"{CAPTURAS}\\web_ordenes.png",
             "Órdenes de lavado: listado, avance de estado y registro.", 14.5)
    d.imagen(f"{CAPTURAS}\\web_reportes.png",
             "Reporte de lavados por tipo de servicio.", 14.0)

    d.h2("10. Pruebas realizadas")
    d.p("Las pruebas se ejecutaron sobre la aplicación desplegada en Tomcat y la base de "
        "datos aqualavado. Se verificaron las rutas de navegación, las validaciones de los "
        "formularios y las operaciones de consulta y registro.")
    d.tabla(
        ["Prueba", "Acción", "Resultado esperado", "Estado"],
        [
            ["Inicio de sesión válido", "Ingresar admin@aqualavado.com con la clave correcta.", "Acceso al panel principal.", "Aprobada"],
            ["Inicio de sesión inválido", "Ingresar una clave incorrecta.", "Mensaje de error y permanencia en el formulario.", "Aprobada"],
            ["Listado de clientes", "Abrir el módulo de clientes.", "Tabla con los clientes registrados.", "Aprobada"],
            ["Registro de cliente", "Enviar el formulario con datos válidos.", "Cliente almacenado y visible en la tabla.", "Aprobada"],
            ["Validación de documento", "Enviar letras o menos de seis dígitos.", "El navegador impide el envío.", "Aprobada"],
            ["Registro de orden", "Seleccionar vehículo, servicio y operario.", "Orden creada en estado EN_COLA con el valor del servicio.", "Aprobada"],
            ["Avance de estado", "Pulsar Avanzar en una orden.", "Cambio a EN_PROCESO, FINALIZADO y ENTREGADO.", "Aprobada"],
            ["Reporte", "Abrir el módulo de reportes.", "Totales y cantidades por servicio.", "Aprobada"],
            ["Cierre de sesión", "Pulsar Cerrar sesión.", "Sesión invalidada y retorno al inicio.", "Aprobada"],
        ],
        anchos=[3.4, 5.4, 4.8, 2.0],
        caption="Pruebas funcionales del módulo web.",
        size=7.5,
    )

    d.h2("11. Compilación y despliegue")
    d.p("La aplicación se compila con las fuentes del módulo JDBC y del módulo web, y se "
        "empaqueta en la carpeta build/web. El despliegue copia esa carpeta en webapps de "
        "Tomcat y el servidor la publica en la ruta /aqualavado.")
    d.codigo(
        "compilar.bat\n"
        "desplegar.bat\n"
        "C:\\xampp\\tomcat\\bin\\startup.bat\n"
        "http://localhost:8080/aqualavado/"
    )

    d.h2("12. Repositorio y entrega")
    d.p("El código se encuentra en el repositorio " + REPO + ", en la carpeta "
        "web-servlets. La entrega se realiza en un archivo comprimido con los archivos del "
        "proyecto web, el módulo JDBC, el script de la base de datos, el controlador y el "
        "enlace del repositorio.")
    d.tabla(
        ["Archivo", "Contenido"],
        [
            ["DylanArias_AA2_EV02.zip", "Proyecto web, módulo JDBC, base de datos y controlador."],
            ["ENLACE_REPOSITORIO.txt", "Dirección del repositorio en GitHub."],
            ["web.xml", "Configuración de servlets y sesión."],
        ],
        anchos=[5.4, 10.2],
        caption="Archivos de la entrega AA2-EV02.",
    )

    d.conclusion([
        "La codificación del módulo web permitió integrar los formularios HTML, los "
        "servlets y las páginas JSP con la base de datos del sistema AquaLavado. La "
        "aplicación atiende peticiones GET y POST, controla la sesión del usuario y "
        "presenta la información de clientes, órdenes y reportes.",
        "Las pruebas realizadas en Tomcat confirmaron el funcionamiento de las rutas, las "
        "validaciones y las operaciones de registro. El módulo queda integrado con el "
        "acceso a datos desarrollado con JDBC y preparado para conectarse con la interfaz "
        "React del proyecto.",
    ])

    d.bibliografia([
        "Oracle. (2025). Java Servlet specification. https://javaee.github.io/servlet-spec/",
        "Apache Software Foundation. (2024). Apache Tomcat 8.5 documentation. https://tomcat.apache.org/tomcat-8.5-doc/",
        "Oracle. (2025). JavaServer Pages technology. https://www.oracle.com/java/technologies/jspt.html",
        "Oracle. (2025). JDBC API specification. https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/",
        "MySQL. (2024). MySQL 8.0 reference manual. https://dev.mysql.com/doc/refman/8.0/en/",
    ])
    return d.guardar()


if __name__ == "__main__":
    cual = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cual in ("all", "ev01"):
        print(ev01())
    if cual in ("all", "ev02"):
        print(ev02())
