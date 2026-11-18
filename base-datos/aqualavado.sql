-- ============================================================
-- Base de datos del sistema AquaLavado
-- Gestión de lavadero de vehículos (servicio presencial)
-- ============================================================

DROP DATABASE IF EXISTS aqualavado;
CREATE DATABASE aqualavado CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE aqualavado;

-- ------------------------------------------------------------
-- Usuarios del sistema
-- ------------------------------------------------------------
CREATE TABLE usuarios (
    id_usuario   INT AUTO_INCREMENT PRIMARY KEY,
    nombre       VARCHAR(80)  NOT NULL,
    correo       VARCHAR(100) NOT NULL UNIQUE,
    clave_hash   VARCHAR(64)  NOT NULL,
    rol          ENUM('ADMINISTRADOR','OPERARIO') NOT NULL DEFAULT 'OPERARIO',
    activo       BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Clientes
-- ------------------------------------------------------------
CREATE TABLE clientes (
    id_cliente   INT AUTO_INCREMENT PRIMARY KEY,
    documento    VARCHAR(15)  NOT NULL UNIQUE,
    nombre       VARCHAR(80)  NOT NULL,
    telefono     VARCHAR(15)  NOT NULL,
    correo       VARCHAR(100),
    direccion    VARCHAR(120),
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Vehículos
-- ------------------------------------------------------------
CREATE TABLE vehiculos (
    id_vehiculo  INT AUTO_INCREMENT PRIMARY KEY,
    placa        VARCHAR(6)  NOT NULL UNIQUE,
    marca        VARCHAR(40) NOT NULL,
    modelo       VARCHAR(40) NOT NULL,
    color        VARCHAR(30) NOT NULL,
    id_cliente   INT NOT NULL,
    CONSTRAINT fk_vehiculo_cliente FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Servicios de lavado
-- ------------------------------------------------------------
CREATE TABLE servicios (
    id_servicio  INT AUTO_INCREMENT PRIMARY KEY,
    nombre       VARCHAR(50) NOT NULL UNIQUE,
    descripcion  VARCHAR(150),
    precio       DECIMAL(10,2) NOT NULL,
    duracion_min INT NOT NULL,
    activo       BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Órdenes de lavado
-- ------------------------------------------------------------
CREATE TABLE ordenes_lavado (
    id_orden     INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo  INT NOT NULL,
    id_servicio  INT NOT NULL,
    id_operario  INT NOT NULL,
    fecha_ingreso DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_salida  DATETIME NULL,
    estado       ENUM('EN_COLA','EN_PROCESO','FINALIZADO','ENTREGADO') NOT NULL DEFAULT 'EN_COLA',
    valor        DECIMAL(10,2) NOT NULL,
    observaciones VARCHAR(200),
    CONSTRAINT fk_orden_vehiculo FOREIGN KEY (id_vehiculo)
        REFERENCES vehiculos(id_vehiculo) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_orden_servicio FOREIGN KEY (id_servicio)
        REFERENCES servicios(id_servicio) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_orden_operario FOREIGN KEY (id_operario)
        REFERENCES usuarios(id_usuario) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Pagos
-- ------------------------------------------------------------
CREATE TABLE pagos (
    id_pago      INT AUTO_INCREMENT PRIMARY KEY,
    id_orden     INT NOT NULL,
    metodo       ENUM('EFECTIVO','TARJETA','TRANSFERENCIA') NOT NULL,
    valor        DECIMAL(10,2) NOT NULL,
    fecha_pago   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_pago_orden FOREIGN KEY (id_orden)
        REFERENCES ordenes_lavado(id_orden) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Datos iniciales
-- ------------------------------------------------------------
INSERT INTO usuarios (nombre, correo, clave_hash, rol) VALUES
('Administrador', 'admin@aqualavado.com', SHA2('admin123', 256), 'ADMINISTRADOR'),
('Juan Pérez', 'juan@aqualavado.com', SHA2('operario123', 256), 'OPERARIO'),
('Camilo Ríos', 'camilo@aqualavado.com', SHA2('operario123', 256), 'OPERARIO');

INSERT INTO clientes (documento, nombre, telefono, correo, direccion) VALUES
('1114523887', 'Carlos Muñoz', '3105552241', 'carlos@correo.com', 'Calle 12 # 4-15'),
('1098774120', 'María Gómez', '3127748890', 'maria@correo.com', 'Carrera 8 # 21-40'),
('1005221456', 'Julián Ríos', '3152209965', 'julian@correo.com', 'Avenida 30 # 9-12'),
('1132908335', 'Luisa Torres', '3168834451', 'luisa@correo.com', 'Calle 5 # 7-33');

INSERT INTO vehiculos (placa, marca, modelo, color, id_cliente) VALUES
('ABC123', 'Renault', 'Logan', 'Blanco', 1),
('XYZ789', 'Mazda', '2', 'Rojo', 2),
('QWE456', 'Chevrolet', 'Onix', 'Gris', 3),
('RTY741', 'Kia', 'Picanto', 'Azul', 4);

INSERT INTO servicios (nombre, descripcion, precio, duracion_min) VALUES
('Básico', 'Lavado exterior con agua y jabón.', 18000.00, 25),
('Completo', 'Lavado exterior e interior con aspirado.', 32000.00, 45),
('Premium', 'Lavado completo con cera y brillo.', 45000.00, 60),
('Detallado', 'Lavado completo con pulido y tratamiento.', 60000.00, 90);

INSERT INTO ordenes_lavado (id_vehiculo, id_servicio, id_operario, fecha_ingreso, estado, valor, observaciones) VALUES
(1, 3, 2, '2026-11-17 08:15:00', 'ENTREGADO', 45000.00, 'Sin novedad'),
(2, 2, 3, '2026-11-17 09:30:00', 'FINALIZADO', 32000.00, 'Aspirado profundo'),
(3, 1, 2, '2026-11-17 10:05:00', 'EN_PROCESO', 18000.00, ''),
(4, 4, 3, '2026-11-17 10:40:00', 'EN_COLA', 60000.00, 'Cliente espera en sala');

INSERT INTO pagos (id_orden, metodo, valor, fecha_pago) VALUES
(1, 'EFECTIVO', 45000.00, '2026-11-17 09:20:00');
