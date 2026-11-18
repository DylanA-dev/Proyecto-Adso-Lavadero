package com.aqualavado.api.controlador;

import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.modelo.OrdenLavado;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.sql.SQLException;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Servicios REST para los indicadores y reportes del lavadero.
 */
@RestController
@RequestMapping("/api/reportes")
public class ReporteController {

    private final OrdenLavadoDAO ordenDAO = new OrdenLavadoDAO();

    @GetMapping("/resumen")
    public Map<String, Object> resumen() throws SQLException {
        List<OrdenLavado> ordenes = ordenDAO.listar();
        long enCola = ordenes.stream()
                .filter(o -> OrdenLavado.ESTADO_EN_COLA.equals(o.getEstado())).count();
        long enProceso = ordenes.stream()
                .filter(o -> OrdenLavado.ESTADO_EN_PROCESO.equals(o.getEstado())).count();
        long entregadas = ordenes.stream()
                .filter(o -> OrdenLavado.ESTADO_ENTREGADO.equals(o.getEstado())).count();

        BigDecimal ingresos = ordenes.stream()
                .filter(o -> OrdenLavado.ESTADO_ENTREGADO.equals(o.getEstado()))
                .map(OrdenLavado::getValor)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
        BigDecimal promedio = entregadas == 0 ? BigDecimal.ZERO
                : ingresos.divide(BigDecimal.valueOf(entregadas), 2, RoundingMode.HALF_UP);

        Map<String, Integer> cantidades = new LinkedHashMap<>();
        Map<String, BigDecimal> valores = new LinkedHashMap<>();
        for (OrdenLavado orden : ordenes) {
            cantidades.merge(orden.getNombreServicio(), 1, Integer::sum);
            valores.merge(orden.getNombreServicio(), orden.getValor(), BigDecimal::add);
        }

        Map<String, Object> respuesta = new LinkedHashMap<>();
        respuesta.put("totalOrdenes", ordenes.size());
        respuesta.put("enCola", enCola);
        respuesta.put("enProceso", enProceso);
        respuesta.put("entregadas", entregadas);
        respuesta.put("ingresos", ingresos);
        respuesta.put("promedio", promedio);
        respuesta.put("cantidades", cantidades);
        respuesta.put("valores", valores);
        return respuesta;
    }
}
