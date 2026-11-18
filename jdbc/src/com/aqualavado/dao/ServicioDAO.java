package com.aqualavado.dao;

import com.aqualavado.conexion.ConexionBD;
import com.aqualavado.modelo.Servicio;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * Operaciones CRUD sobre la tabla servicios.
 */
public class ServicioDAO {

    private static final String SELECT_BASE =
            "SELECT id_servicio, nombre, descripcion, precio, duracion_min, activo "
                    + "FROM servicios ";

    public int insertar(Servicio servicio) throws SQLException {
        String sql = "INSERT INTO servicios (nombre, descripcion, precio, duracion_min, activo) "
                + "VALUES (?, ?, ?, ?, ?)";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     sql, Statement.RETURN_GENERATED_KEYS)) {
            sentencia.setString(1, servicio.getNombre());
            sentencia.setString(2, servicio.getDescripcion());
            sentencia.setBigDecimal(3, servicio.getPrecio());
            sentencia.setInt(4, servicio.getDuracionMin());
            sentencia.setBoolean(5, servicio.isActivo());
            sentencia.executeUpdate();
            try (ResultSet claves = sentencia.getGeneratedKeys()) {
                if (claves.next()) {
                    servicio.setIdServicio(claves.getInt(1));
                }
            }
            return servicio.getIdServicio();
        }
    }

    public List<Servicio> listar() throws SQLException {
        List<Servicio> servicios = new ArrayList<>();
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     SELECT_BASE + "ORDER BY nombre");
             ResultSet resultado = sentencia.executeQuery()) {
            while (resultado.next()) {
                servicios.add(mapear(resultado));
            }
        }
        return servicios;
    }

    public Servicio buscarPorId(int idServicio) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     SELECT_BASE + "WHERE id_servicio = ?")) {
            sentencia.setInt(1, idServicio);
            try (ResultSet resultado = sentencia.executeQuery()) {
                return resultado.next() ? mapear(resultado) : null;
            }
        }
    }

    public boolean actualizar(Servicio servicio) throws SQLException {
        String sql = "UPDATE servicios SET nombre = ?, descripcion = ?, precio = ?, "
                + "duracion_min = ?, activo = ? WHERE id_servicio = ?";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setString(1, servicio.getNombre());
            sentencia.setString(2, servicio.getDescripcion());
            sentencia.setBigDecimal(3, servicio.getPrecio());
            sentencia.setInt(4, servicio.getDuracionMin());
            sentencia.setBoolean(5, servicio.isActivo());
            sentencia.setInt(6, servicio.getIdServicio());
            return sentencia.executeUpdate() > 0;
        }
    }

    public boolean eliminar(int idServicio) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     "DELETE FROM servicios WHERE id_servicio = ?")) {
            sentencia.setInt(1, idServicio);
            return sentencia.executeUpdate() > 0;
        }
    }

    private Servicio mapear(ResultSet resultado) throws SQLException {
        Servicio servicio = new Servicio();
        servicio.setIdServicio(resultado.getInt("id_servicio"));
        servicio.setNombre(resultado.getString("nombre"));
        servicio.setDescripcion(resultado.getString("descripcion"));
        servicio.setPrecio(resultado.getBigDecimal("precio"));
        servicio.setDuracionMin(resultado.getInt("duracion_min"));
        servicio.setActivo(resultado.getBoolean("activo"));
        return servicio;
    }
}
