package com.aqualavado.dao;

import com.aqualavado.conexion.ConexionBD;
import com.aqualavado.modelo.Cliente;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * Operaciones CRUD sobre la tabla clientes.
 */
public class ClienteDAO {

    private static final String INSERTAR =
            "INSERT INTO clientes (documento, nombre, telefono, correo, direccion) "
                    + "VALUES (?, ?, ?, ?, ?)";
    private static final String LISTAR =
            "SELECT id_cliente, documento, nombre, telefono, correo, direccion "
                    + "FROM clientes ORDER BY nombre";
    private static final String BUSCAR =
            "SELECT id_cliente, documento, nombre, telefono, correo, direccion "
                    + "FROM clientes WHERE id_cliente = ?";
    private static final String ACTUALIZAR =
            "UPDATE clientes SET documento = ?, nombre = ?, telefono = ?, "
                    + "correo = ?, direccion = ? WHERE id_cliente = ?";
    private static final String ELIMINAR =
            "DELETE FROM clientes WHERE id_cliente = ?";

    public int insertar(Cliente cliente) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(
                     INSERTAR, Statement.RETURN_GENERATED_KEYS)) {
            sentencia.setString(1, cliente.getDocumento());
            sentencia.setString(2, cliente.getNombre());
            sentencia.setString(3, cliente.getTelefono());
            sentencia.setString(4, cliente.getCorreo());
            sentencia.setString(5, cliente.getDireccion());
            sentencia.executeUpdate();
            try (ResultSet claves = sentencia.getGeneratedKeys()) {
                if (claves.next()) {
                    cliente.setIdCliente(claves.getInt(1));
                }
            }
            return cliente.getIdCliente();
        }
    }

    public List<Cliente> listar() throws SQLException {
        List<Cliente> clientes = new ArrayList<>();
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(LISTAR);
             ResultSet resultado = sentencia.executeQuery()) {
            while (resultado.next()) {
                clientes.add(mapear(resultado));
            }
        }
        return clientes;
    }

    public Cliente buscarPorId(int idCliente) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(BUSCAR)) {
            sentencia.setInt(1, idCliente);
            try (ResultSet resultado = sentencia.executeQuery()) {
                return resultado.next() ? mapear(resultado) : null;
            }
        }
    }

    public boolean actualizar(Cliente cliente) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(ACTUALIZAR)) {
            sentencia.setString(1, cliente.getDocumento());
            sentencia.setString(2, cliente.getNombre());
            sentencia.setString(3, cliente.getTelefono());
            sentencia.setString(4, cliente.getCorreo());
            sentencia.setString(5, cliente.getDireccion());
            sentencia.setInt(6, cliente.getIdCliente());
            return sentencia.executeUpdate() > 0;
        }
    }

    public boolean eliminar(int idCliente) throws SQLException {
        try (Connection conexion = ConexionBD.obtener();
             PreparedStatement sentencia = conexion.prepareStatement(ELIMINAR)) {
            sentencia.setInt(1, idCliente);
            return sentencia.executeUpdate() > 0;
        }
    }

    private Cliente mapear(ResultSet resultado) throws SQLException {
        Cliente cliente = new Cliente();
        cliente.setIdCliente(resultado.getInt("id_cliente"));
        cliente.setDocumento(resultado.getString("documento"));
        cliente.setNombre(resultado.getString("nombre"));
        cliente.setTelefono(resultado.getString("telefono"));
        cliente.setCorreo(resultado.getString("correo"));
        cliente.setDireccion(resultado.getString("direccion"));
        return cliente;
    }
}
