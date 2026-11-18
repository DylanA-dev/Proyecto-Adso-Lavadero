package com.aqualavado.api.controlador;

import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.modelo.Cliente;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import java.sql.SQLException;
import java.util.List;
import java.util.Map;

/**
 * Servicios REST para la gestión de clientes.
 */
@RestController
@RequestMapping("/api/clientes")
public class ClienteController {

    private final ClienteDAO clienteDAO = new ClienteDAO();

    @GetMapping
    public List<Cliente> listar() throws SQLException {
        return clienteDAO.listar();
    }

    @GetMapping("/{id}")
    public Cliente buscar(@PathVariable int id) throws SQLException {
        return clienteDAO.buscarPorId(id);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Cliente crear(@RequestBody Cliente cliente) throws SQLException {
        clienteDAO.insertar(cliente);
        return cliente;
    }

    @PutMapping("/{id}")
    public Cliente actualizar(@PathVariable int id, @RequestBody Cliente cliente)
            throws SQLException {
        cliente.setIdCliente(id);
        clienteDAO.actualizar(cliente);
        return cliente;
    }

    @DeleteMapping("/{id}")
    public Map<String, Boolean> eliminar(@PathVariable int id) throws SQLException {
        return Map.of("eliminado", clienteDAO.eliminar(id));
    }
}
