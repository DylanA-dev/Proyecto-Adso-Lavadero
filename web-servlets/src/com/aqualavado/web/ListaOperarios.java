package com.aqualavado.web;

import com.aqualavado.conexion.ConexionBD;
import com.aqualavado.modelo.Usuario;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * Obtiene los operarios disponibles para asignar una orden.
 */
public final class ListaOperarios {

    private ListaOperarios() {
    }

    public static List<Usuario> obtener() throws SQLException {
        List<Usuario> operarios = new ArrayList<>();
        String sql = "SELECT id_usuario, nombre, correo, rol FROM usuarios "
                + "WHERE activo = TRUE ORDER BY nombre";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(sql);
             ResultSet resultado = sentencia.executeQuery()) {
            while (resultado.next()) {
                operarios.add(new Usuario(
                        resultado.getInt("id_usuario"),
                        resultado.getString("nombre"),
                        resultado.getString("correo"),
                        resultado.getString("rol")));
            }
        }
        return operarios;
    }
}
