package com.aqualavado.dao;

import com.aqualavado.conexion.ConexionBD;
import com.aqualavado.modelo.Vehiculo;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * Operaciones CRUD sobre la tabla vehiculos.
 */
public class VehiculoDAO {

    private static final String SELECT_BASE =
            "SELECT v.id_vehiculo, v.placa, v.marca, v.modelo, v.color, "
                    + "v.id_cliente, c.nombre AS nombre_cliente "
                    + "FROM vehiculos v INNER JOIN clientes c ON c.id_cliente = v.id_cliente ";

    public int insertar(Vehiculo vehiculo) throws SQLException {
        String sql = "INSERT INTO vehiculos (placa, marca, modelo, color, id_cliente) "
                + "VALUES (?, ?, ?, ?, ?)";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     sql, Statement.RETURN_GENERATED_KEYS)) {
            sentencia.setString(1, vehiculo.getPlaca());
            sentencia.setString(2, vehiculo.getMarca());
            sentencia.setString(3, vehiculo.getModelo());
            sentencia.setString(4, vehiculo.getColor());
            sentencia.setInt(5, vehiculo.getIdCliente());
            sentencia.executeUpdate();
            try (ResultSet claves = sentencia.getGeneratedKeys()) {
                if (claves.next()) {
                    vehiculo.setIdVehiculo(claves.getInt(1));
                }
            }
            return vehiculo.getIdVehiculo();
        }
    }

    public List<Vehiculo> listar() throws SQLException {
        List<Vehiculo> vehiculos = new ArrayList<>();
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(SELECT_BASE + "ORDER BY v.placa");
             ResultSet resultado = sentencia.executeQuery()) {
            while (resultado.next()) {
                vehiculos.add(mapear(resultado));
            }
        }
        return vehiculos;
    }

    public Vehiculo buscarPorId(int idVehiculo) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     SELECT_BASE + "WHERE v.id_vehiculo = ?")) {
            sentencia.setInt(1, idVehiculo);
            try (ResultSet resultado = sentencia.executeQuery()) {
                return resultado.next() ? mapear(resultado) : null;
            }
        }
    }

    public boolean actualizar(Vehiculo vehiculo) throws SQLException {
        String sql = "UPDATE vehiculos SET placa = ?, marca = ?, modelo = ?, "
                + "color = ?, id_cliente = ? WHERE id_vehiculo = ?";
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setString(1, vehiculo.getPlaca());
            sentencia.setString(2, vehiculo.getMarca());
            sentencia.setString(3, vehiculo.getModelo());
            sentencia.setString(4, vehiculo.getColor());
            sentencia.setInt(5, vehiculo.getIdCliente());
            sentencia.setInt(6, vehiculo.getIdVehiculo());
            return sentencia.executeUpdate() > 0;
        }
    }

    public boolean eliminar(int idVehiculo) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     "DELETE FROM vehiculos WHERE id_vehiculo = ?")) {
            sentencia.setInt(1, idVehiculo);
            return sentencia.executeUpdate() > 0;
        }
    }

    private Vehiculo mapear(ResultSet resultado) throws SQLException {
        Vehiculo vehiculo = new Vehiculo();
        vehiculo.setIdVehiculo(resultado.getInt("id_vehiculo"));
        vehiculo.setPlaca(resultado.getString("placa"));
        vehiculo.setMarca(resultado.getString("marca"));
        vehiculo.setModelo(resultado.getString("modelo"));
        vehiculo.setColor(resultado.getString("color"));
        vehiculo.setIdCliente(resultado.getInt("id_cliente"));
        vehiculo.setNombreCliente(resultado.getString("nombre_cliente"));
        return vehiculo;
    }
}
