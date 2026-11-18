package com.aqualavado.api.controlador;

import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.dao.ServicioDAO;
import com.aqualavado.modelo.OrdenLavado;
import com.aqualavado.modelo.Servicio;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import java.sql.SQLException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;

/**
 * Servicios REST para el registro y control de órdenes de lavado.
 */
@RestController
@RequestMapping("/api/ordenes")
public class OrdenController {

    private final OrdenLavadoDAO ordenDAO = new OrdenLavadoDAO();
    private final ServicioDAO servicioDAO = new ServicioDAO();

    public record NuevaOrden(int vehiculo, int servicio, int operario,
                             String observaciones) {
    }

    @GetMapping
    public List<OrdenLavado> listar() throws SQLException {
        return ordenDAO.listar();
    }

    @GetMapping("/estado/{estado}")
    public List<OrdenLavado> listarPorEstado(@PathVariable String estado) throws SQLException {
        return ordenDAO.listarPorEstado(estado);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public OrdenLavado crear(@RequestBody NuevaOrden solicitud) throws SQLException {
        Servicio servicio = servicioDAO.buscarPorId(solicitud.servicio());
        if (servicio == null) {
            throw new IllegalArgumentException("El servicio no existe.");
        }
        OrdenLavado orden = new OrdenLavado(
                solicitud.vehiculo(),
                solicitud.servicio(),
                solicitud.operario(),
                OrdenLavado.ESTADO_EN_COLA,
                servicio.getPrecio(),
                solicitud.observaciones());
        ordenDAO.insertar(orden);
        return ordenDAO.buscarPorId(orden.getIdOrden());
    }

    @PutMapping("/{id}/estado")
    public OrdenLavado avanzar(@PathVariable int id) throws SQLException {
        OrdenLavado orden = ordenDAO.buscarPorId(id);
        if (orden == null) {
            throw new IllegalArgumentException("La orden no existe.");
        }
        String siguiente = switch (orden.getEstado()) {
            case OrdenLavado.ESTADO_EN_COLA -> OrdenLavado.ESTADO_EN_PROCESO;
            case OrdenLavado.ESTADO_EN_PROCESO -> OrdenLavado.ESTADO_FINALIZADO;
            case OrdenLavado.ESTADO_FINALIZADO -> OrdenLavado.ESTADO_ENTREGADO;
            default -> null;
        };
        if (siguiente == null) {
            return orden;
        }
        LocalDateTime salida = OrdenLavado.ESTADO_ENTREGADO.equals(siguiente)
                ? LocalDateTime.now() : null;
        ordenDAO.cambiarEstado(id, siguiente, salida);
        return ordenDAO.buscarPorId(id);
    }

    @PutMapping("/{id}/entregar")
    public Map<String, Boolean> entregar(@PathVariable int id) throws SQLException {
        return Map.of("actualizada", ordenDAO.cambiarEstado(
                id, OrdenLavado.ESTADO_ENTREGADO, LocalDateTime.now()));
    }
}
