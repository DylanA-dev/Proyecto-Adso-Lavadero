package com.aqualavado.dao;

import com.aqualavado.conexion.ConexionBD;
import com.aqualavado.modelo.OrdenLavado;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * Operaciones CRUD sobre la tabla ordenes_lavado.
 */
public class OrdenLavadoDAO {

    private static final String SELECT_BASE =
            "SELECT o.id_orden, o.id_vehiculo, v.placa, o.id_servicio, s.nombre AS servicio, "
                    + "o.id_operario, u.nombre AS operario, o.fecha_ingreso, o.fecha_salida, "
                    + "o.estado, o.valor, o.observaciones "
                    + "FROM ordenes_lavado o "
                    + "INNER JOIN vehiculos v ON v.id_vehiculo = o.id_vehiculo "
                    + "INNER JOIN servicios s ON s.id_servicio = o.id_servicio "
                    + "INNER JOIN usuarios u ON u.id_usuario = o.id_operario ";

    public int insertar(OrdenLavado orden) throws SQLException {
        String sql = "INSERT INTO ordenes_lavado (id_vehiculo, id_servicio, id_operario, "
                + "fecha_ingreso, estado, valor, observaciones) VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     sql, Statement.RETURN_GENERATED_KEYS)) {
            sentencia.setInt(1, orden.getIdVehiculo());
            sentencia.setInt(2, orden.getIdServicio());
            sentencia.setInt(3, orden.getIdOperario());
            sentencia.setTimestamp(4, Timestamp.valueOf(
                    orden.getFechaIngreso() == null
                            ? LocalDateTime.now() : orden.getFechaIngreso()));
            sentencia.setString(5, orden.getEstado());
            sentencia.setBigDecimal(6, orden.getValor());
            sentencia.setString(7, orden.getObservaciones());
            sentencia.executeUpdate();
            try (ResultSet claves = sentencia.getGeneratedKeys()) {
                if (claves.next()) {
                    orden.setIdOrden(claves.getInt(1));
                }
            }
            return orden.getIdOrden();
        }
    }

    public List<OrdenLavado> listar() throws SQLException {
        List<OrdenLavado> ordenes = new ArrayList<>();
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     SELECT_BASE + "ORDER BY o.fecha_ingreso DESC");
             ResultSet resultado = sentencia.executeQuery()) {
            while (resultado.next()) {
                ordenes.add(mapear(resultado));
            }
        }
        return ordenes;
    }

    public List<OrdenLavado> listarPorEstado(String estado) throws SQLException {
        List<OrdenLavado> ordenes = new ArrayList<>();
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     SELECT_BASE + "WHERE o.estado = ? ORDER BY o.fecha_ingreso")) {
            sentencia.setString(1, estado);
            try (ResultSet resultado = sentencia.executeQuery()) {
                while (resultado.next()) {
                    ordenes.add(mapear(resultado));
                }
            }
        }
        return ordenes;
    }

    public OrdenLavado buscarPorId(int idOrden) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     SELECT_BASE + "WHERE o.id_orden = ?")) {
            sentencia.setInt(1, idOrden);
            try (ResultSet resultado = sentencia.executeQuery()) {
                return resultado.next() ? mapear(resultado) : null;
            }
        }
    }

    public boolean actualizar(OrdenLavado orden) throws SQLException {
        String sql = "UPDATE ordenes_lavado SET id_vehiculo = ?, id_servicio = ?, "
                + "id_operario = ?, estado = ?, valor = ?, observaciones = ?, "
                + "fecha_salida = ? WHERE id_orden = ?";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setInt(1, orden.getIdVehiculo());
            sentencia.setInt(2, orden.getIdServicio());
            sentencia.setInt(3, orden.getIdOperario());
            sentencia.setString(4, orden.getEstado());
            sentencia.setBigDecimal(5, orden.getValor());
            sentencia.setString(6, orden.getObservaciones());
            sentencia.setTimestamp(7, orden.getFechaSalida() == null
                    ? null : Timestamp.valueOf(orden.getFechaSalida()));
            sentencia.setInt(8, orden.getIdOrden());
            return sentencia.executeUpdate() > 0;
        }
    }

    public boolean cambiarEstado(int idOrden, String estado,
                                 LocalDateTime fechaSalida) throws SQLException {
        String sql = "UPDATE ordenes_lavado SET estado = ?, fecha_salida = ? "
                + "WHERE id_orden = ?";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setString(1, estado);
            sentencia.setTimestamp(2, fechaSalida == null
                    ? null : Timestamp.valueOf(fechaSalida));
            sentencia.setInt(3, idOrden);
            return sentencia.executeUpdate() > 0;
        }
    }

    public boolean eliminar(int idOrden) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     "DELETE FROM ordenes_lavado WHERE id_orden = ?")) {
            sentencia.setInt(1, idOrden);
            return sentencia.executeUpdate() > 0;
        }
    }

    private OrdenLavado mapear(ResultSet resultado) throws SQLException {
        OrdenLavado orden = new OrdenLavado();
        orden.setIdOrden(resultado.getInt("id_orden"));
        orden.setIdVehiculo(resultado.getInt("id_vehiculo"));
        orden.setPlaca(resultado.getString("placa"));
        orden.setIdServicio(resultado.getInt("id_servicio"));
        orden.setNombreServicio(resultado.getString("servicio"));
        orden.setIdOperario(resultado.getInt("id_operario"));
        orden.setNombreOperario(resultado.getString("operario"));
        Timestamp ingreso = resultado.getTimestamp("fecha_ingreso");
        if (ingreso != null) {
            orden.setFechaIngreso(ingreso.toLocalDateTime());
        }
        Timestamp salida = resultado.getTimestamp("fecha_salida");
        if (salida != null) {
            orden.setFechaSalida(salida.toLocalDateTime());
        }
        orden.setEstado(resultado.getString("estado"));
        orden.setValor(resultado.getBigDecimal("valor"));
        orden.setObservaciones(resultado.getString("observaciones"));
        return orden;
    }
}
