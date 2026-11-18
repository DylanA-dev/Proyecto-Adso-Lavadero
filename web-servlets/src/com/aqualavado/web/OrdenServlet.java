package com.aqualavado.web;

import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.dao.ServicioDAO;
import com.aqualavado.dao.VehiculoDAO;
import com.aqualavado.modelo.OrdenLavado;
import com.aqualavado.modelo.Servicio;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.math.BigDecimal;
import java.sql.SQLException;
import java.time.LocalDateTime;

/**
 * Gestiona el registro de órdenes y el avance de su estado.
 */
public class OrdenServlet extends HttpServlet {

    private final OrdenLavadoDAO ordenDAO = new OrdenLavadoDAO();
    private final VehiculoDAO vehiculoDAO = new VehiculoDAO();
    private final ServicioDAO servicioDAO = new ServicioDAO();

    @Override
    protected void doGet(HttpServletRequest solicitud, HttpServletResponse respuesta)
            throws ServletException, IOException {
        if (!Sesion.activa(solicitud)) {
            respuesta.sendRedirect(solicitud.getContextPath() + "/index.jsp");
            return;
        }
        try {
            String accion = solicitud.getParameter("accion");
            if ("avanzar".equals(accion)) {
                avanzar(Integer.parseInt(solicitud.getParameter("id")));
            }
            cargarVista(solicitud);
            solicitud.getRequestDispatcher("/WEB-INF/vistas/ordenes.jsp")
                    .forward(solicitud, respuesta);
        } catch (SQLException error) {
            throw new ServletException("Error al consultar las órdenes", error);
        }
    }

    @Override
    protected void doPost(HttpServletRequest solicitud, HttpServletResponse respuesta)
            throws ServletException, IOException {
        if (!Sesion.activa(solicitud)) {
            respuesta.sendRedirect(solicitud.getContextPath() + "/index.jsp");
            return;
        }
        solicitud.setCharacterEncoding("UTF-8");
        try {
            int idServicio = Integer.parseInt(solicitud.getParameter("servicio"));
            Servicio servicio = servicioDAO.buscarPorId(idServicio);
            if (servicio == null) {
                throw new SQLException("El servicio seleccionado no existe.");
            }
            OrdenLavado orden = new OrdenLavado(
                    Integer.parseInt(solicitud.getParameter("vehiculo")),
                    idServicio,
                    Integer.parseInt(solicitud.getParameter("operario")),
                    OrdenLavado.ESTADO_EN_COLA,
                    servicio.getPrecio(),
                    solicitud.getParameter("observaciones"));
            ordenDAO.insertar(orden);
            respuesta.sendRedirect(solicitud.getContextPath() + "/OrdenServlet");
        } catch (SQLException error) {
            solicitud.setAttribute("error", "No fue posible registrar la orden.");
            cargarVistaSegura(solicitud);
            solicitud.getRequestDispatcher("/WEB-INF/vistas/ordenes.jsp")
                    .forward(solicitud, respuesta);
        } catch (NumberFormatException error) {
            solicitud.setAttribute("error", "Verifique los datos del formulario.");
            cargarVistaSegura(solicitud);
            solicitud.getRequestDispatcher("/WEB-INF/vistas/ordenes.jsp")
                    .forward(solicitud, respuesta);
        }
    }

    private void cargarVistaSegura(HttpServletRequest solicitud) throws ServletException {
        try {
            cargarVista(solicitud);
        } catch (SQLException error) {
            throw new ServletException("Error al cargar las órdenes", error);
        }
    }

    private void avanzar(int idOrden) throws SQLException {
        OrdenLavado orden = ordenDAO.buscarPorId(idOrden);
        if (orden == null) {
            return;
        }
        String siguiente = switch (orden.getEstado()) {
            case OrdenLavado.ESTADO_EN_COLA -> OrdenLavado.ESTADO_EN_PROCESO;
            case OrdenLavado.ESTADO_EN_PROCESO -> OrdenLavado.ESTADO_FINALIZADO;
            case OrdenLavado.ESTADO_FINALIZADO -> OrdenLavado.ESTADO_ENTREGADO;
            default -> null;
        };
        if (siguiente != null) {
            LocalDateTime salida = OrdenLavado.ESTADO_ENTREGADO.equals(siguiente)
                    ? LocalDateTime.now() : null;
            ordenDAO.cambiarEstado(idOrden, siguiente, salida);
        }
    }

    private void cargarVista(HttpServletRequest solicitud) throws SQLException {
        solicitud.setAttribute("ordenes", ordenDAO.listar());
        solicitud.setAttribute("vehiculos", vehiculoDAO.listar());
        solicitud.setAttribute("servicios", servicioDAO.listar());
        solicitud.setAttribute("operarios", ListaOperarios.obtener());
    }
}
