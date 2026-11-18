# AquaLavado — Sistema de gestión de lavadero

Sistema de información para la operación de un lavadero de vehículos. Registra la
entrada del vehículo, genera la orden de lavado, controla el avance del proceso,
registra la salida y el pago, y consolida los reportes del establecimiento.

El servicio se presta de forma presencial en las instalaciones del lavadero. El
sistema no gestiona lavados a domicilio.

## Alcance

- Registro de clientes y de sus vehículos.
- Administración de servicios de lavado y tarifas.
- Registro de órdenes con operario, servicio y observaciones.
- Control de estados: en cola, en proceso, finalizado y entregado.
- Registro de la salida del vehículo y del pago.
- Reportes de ingresos, ticket promedio y lavados por tipo de servicio.

## Módulos

- `base-datos`: script de creación y datos iniciales.
- `jdbc`: modelo, conexión, DAO, aplicación de consola y pruebas CRUD.
- `escritorio`: aplicación stand-alone con Java Swing.
- `web-servlets`: aplicación web con servlets y JSP.
- `api-spring`: API REST con Spring Boot.
- `frontend-react`: interfaz web y móvil instalable (PWA) con React.

## Tecnologías

- Java 21 LTS (compatible con versiones superiores).
- JDBC y MySQL / MariaDB.
- Apache Tomcat 8.5 para servlets y JSP.
- Spring Boot 3.5 para la API REST.
- React 18 y Vite para el front-end.
- Git y GitHub para el control de versiones.

## Base de datos

```sql
source base-datos/aqualavado.sql
```

El script crea la base `aqualavado`, las tablas `usuarios`, `clientes`,
`vehiculos`, `servicios`, `ordenes_lavado` y `pagos`, y carga los datos iniciales.

## Ejecución

### Aplicación de consola y pruebas JDBC

```bash
cd jdbc
compilar.bat
ejecutar-pruebas.bat
ejecutar.bat
```

### Aplicación de escritorio

```bash
cd escritorio
compilar.bat
ejecutar.bat
```

### Aplicación web con servlets y JSP

```bash
cd web-servlets
compilar.bat
desplegar.bat
C:\xampp\tomcat\bin\startup.bat
```

La aplicación queda disponible en `http://localhost:8080/aqualavado/`.

### API REST

```bash
cd api-spring
mvn spring-boot:run
```

La API queda disponible en `http://localhost:8081/api/`.

### Front-end React

```bash
cd frontend-react
npm install
npm run dev
```

La aplicación queda disponible en `http://localhost:5173/`.

## Usuarios de prueba

| Correo | Contraseña | Rol |
|---|---|---|
| admin@aqualavado.com | admin123 | Administrador |
| juan@aqualavado.com | operario123 | Operario |
| camilo@aqualavado.com | operario123 | Operario |

## Autor

Dylan Arias — SENA, Análisis y Desarrollo de Software, ficha 3186703.
