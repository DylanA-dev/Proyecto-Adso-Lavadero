package com.aqualavado.web;

import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.modelo.OrdenLavado;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.math.BigDecimal;
import java.sql.SQLException;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Consolida los ingresos y la cantidad de lavados por servicio.
 */
public class ReporteServlet extends HttpServlet {

    private final OrdenLavadoDAO ordenDAO = new OrdenLavadoDAO();

    @Override
    protected void doGet(HttpServletRequest solicitud, HttpServletResponse respuesta)
            throws ServletException, IOException {
        if (!Sesion.activa(solicitud)) {
            respuesta.sendRedirect(solicitud.getContextPath() + "/index.jsp");
            return;
        }
        try {
            List<OrdenLavado> ordenes = ordenDAO.listar();
            Map<String, Integer> cantidades = new LinkedHashMap<>();
            Map<String, BigDecimal> valores = new LinkedHashMap<>();
            int entregadas = 0;
            BigDecimal total = BigDecimal.ZERO;

            for (OrdenLavado orden : ordenes) {
                cantidades.merge(orden.getNombreServicio(), 1, Integer::sum);
                valores.merge(orden.getNombreServicio(), orden.getValor(), BigDecimal::add);
                if (OrdenLavado.ESTADO_ENTREGADO.equals(orden.getEstado())) {
                    entregadas++;
                    total = total.add(orden.getValor());
                }
            }

            solicitud.setAttribute("cantidades", cantidades);
            solicitud.setAttribute("valores", valores);
            solicitud.setAttribute("entregadas", entregadas);
            solicitud.setAttribute("totalIngresos", total);
            solicitud.setAttribute("promedio", entregadas == 0 ? BigDecimal.ZERO
                    : total.divide(BigDecimal.valueOf(entregadas), 2, java.math.RoundingMode.HALF_UP));
            solicitud.getRequestDispatcher("/WEB-INF/vistas/reportes.jsp")
                    .forward(solicitud, respuesta);
        } catch (SQLException error) {
            throw new ServletException("Error al generar el reporte", error);
        }
    }
}
