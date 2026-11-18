package com.aqualavado.web;

import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.dao.VehiculoDAO;
import com.aqualavado.modelo.OrdenLavado;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.math.BigDecimal;
import java.sql.SQLException;
import java.util.List;

/**
 * Construye los indicadores del panel principal.
 */
public class PanelServlet extends HttpServlet {

    private final ClienteDAO clienteDAO = new ClienteDAO();
    private final VehiculoDAO vehiculoDAO = new VehiculoDAO();
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
            long enCola = ordenes.stream()
                    .filter(o -> OrdenLavado.ESTADO_EN_COLA.equals(o.getEstado())).count();
            long enProceso = ordenes.stream()
                    .filter(o -> OrdenLavado.ESTADO_EN_PROCESO.equals(o.getEstado())).count();
            BigDecimal ingresos = ordenes.stream()
                    .filter(o -> OrdenLavado.ESTADO_ENTREGADO.equals(o.getEstado()))
                    .map(OrdenLavado::getValor)
                    .reduce(BigDecimal.ZERO, BigDecimal::add);

            solicitud.setAttribute("totalClientes", clienteDAO.listar().size());
            solicitud.setAttribute("totalVehiculos", vehiculoDAO.listar().size());
            solicitud.setAttribute("totalOrdenes", ordenes.size());
            solicitud.setAttribute("enCola", enCola);
            solicitud.setAttribute("enProceso", enProceso);
            solicitud.setAttribute("ingresos", ingresos);
            solicitud.setAttribute("ordenes", ordenes);
            solicitud.getRequestDispatcher("/WEB-INF/vistas/panel.jsp")
                    .forward(solicitud, respuesta);
        } catch (SQLException error) {
            throw new ServletException("Error al consultar los indicadores", error);
        }
    }
}
