package com.aqualavado.dao;

import com.aqualavado.conexion.ConexionBD;
import com.aqualavado.modelo.Usuario;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * Consultas relacionadas con los usuarios del sistema.
 */
public class UsuarioDAO {

    private static final String AUTENTICAR =
            "SELECT id_usuario, nombre, correo, rol FROM usuarios "
                    + "WHERE correo = ? AND clave_hash = SHA2(?, 256) AND activo = TRUE";

    public Usuario autenticar(String correo, String clave) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(AUTENTICAR)) {
            sentencia.setString(1, correo);
            sentencia.setString(2, clave);
            try (ResultSet resultado = sentencia.executeQuery()) {
                if (resultado.next()) {
                    return new Usuario(
                            resultado.getInt("id_usuario"),
                            resultado.getString("nombre"),
                            resultado.getString("correo"),
                            resultado.getString("rol"));
                }
            }
        }
        return null;
    }

    /**
     * Lista los usuarios activos para asignarlos a una orden de lavado.
     *
     * @return usuarios activos ordenados por nombre
     * @throws SQLException si ocurre un error al consultar
     */
    public List<Usuario> listarActivos() throws SQLException {
        List<Usuario> usuarios = new ArrayList<>();
        String sql = "SELECT id_usuario, nombre, correo, rol FROM usuarios "
                + "WHERE activo = TRUE ORDER BY nombre";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(sql);
             ResultSet resultado = sentencia.executeQuery()) {
            while (resultado.next()) {
                usuarios.add(new Usuario(
                        resultado.getInt("id_usuario"),
                        resultado.getString("nombre"),
                        resultado.getString("correo"),
                        resultado.getString("rol")));
            }
        }
        return usuarios;
    }
}
