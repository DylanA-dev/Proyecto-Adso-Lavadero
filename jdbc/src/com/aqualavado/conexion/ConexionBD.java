package com.aqualavado.conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * Centraliza la conexión con la base de datos MySQL del sistema AquaLavado.
 */
public final class ConexionBD {

    private static final String URL = System.getProperty(
            "aqualavado.url",
            "jdbc:mysql://localhost:3306/aqualavado?useSSL=false"
                    + "&allowPublicKeyRetrieval=true"
                    + "&serverTimezone=America/Bogota"
                    + "&characterEncoding=UTF-8");
    private static final String USUARIO = System.getProperty("aqualavado.usuario", "root");
    private static final String CLAVE = System.getProperty("aqualavado.clave", "");

    private ConexionBD() {
        // Clase de utilidad: no se instancia.
    }

    static {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException error) {
            throw new IllegalStateException(
                    "No se encontró el controlador JDBC de MySQL.", error);
        }
    }

    /**
     * Abre una conexión nueva con la base de datos.
     *
     * @return conexión activa
     * @throws SQLException si no es posible establecer la conexión
     */
    public static Connection obtener() throws SQLException {
        return DriverManager.getConnection(URL, USUARIO, CLAVE);
    }
}
