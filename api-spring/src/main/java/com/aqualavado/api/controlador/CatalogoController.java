package com.aqualavado.api.controlador;

import com.aqualavado.dao.ServicioDAO;
import com.aqualavado.dao.VehiculoDAO;
import com.aqualavado.modelo.Servicio;
import com.aqualavado.modelo.Vehiculo;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.sql.SQLException;
import java.util.List;

/**
 * Servicios REST de consulta para vehículos y servicios de lavado.
 */
@RestController
@RequestMapping("/api")
public class CatalogoController {

    private final VehiculoDAO vehiculoDAO = new VehiculoDAO();
    private final ServicioDAO servicioDAO = new ServicioDAO();

    @GetMapping("/vehiculos")
    public List<Vehiculo> vehiculos() throws SQLException {
        return vehiculoDAO.listar();
    }

    @GetMapping("/servicios")
    public List<Servicio> servicios() throws SQLException {
        return servicioDAO.listar();
    }
}
