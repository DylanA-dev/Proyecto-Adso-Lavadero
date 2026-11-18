package com.aqualavado.web;

import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.modelo.Cliente;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;
import java.util.List;

/**
 * Gestiona el listado, registro y eliminación de clientes.
 */
public class ClienteServlet extends HttpServlet {

    private final ClienteDAO clienteDAO = new ClienteDAO();

    @Override
    protected void doGet(HttpServletRequest solicitud, HttpServletResponse respuesta)
            throws ServletException, IOException {
        if (!Sesion.activa(solicitud)) {
            respuesta.sendRedirect(solicitud.getContextPath() + "/index.jsp");
            return;
        }
        try {
            List<Cliente> clientes = clienteDAO.listar();
            solicitud.setAttribute("clientes", clientes);
            solicitud.getRequestDispatcher("/WEB-INF/vistas/clientes.jsp")
                    .forward(solicitud, respuesta);
        } catch (SQLException error) {
            throw new ServletException("Error al listar los clientes", error);
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
        String accion = solicitud.getParameter("accion");
        try {
            if ("eliminar".equals(accion)) {
                clienteDAO.eliminar(Integer.parseInt(solicitud.getParameter("id")));
            } else {
                Cliente cliente = new Cliente(
                        solicitud.getParameter("documento").trim(),
                        solicitud.getParameter("nombre").trim(),
                        solicitud.getParameter("telefono").trim(),
                        solicitud.getParameter("correo").trim(),
                        solicitud.getParameter("direccion").trim());
                clienteDAO.insertar(cliente);
            }
            respuesta.sendRedirect(solicitud.getContextPath() + "/ClienteServlet");
        } catch (SQLException error) {
            solicitud.setAttribute("error", "No fue posible guardar el cliente: "
                    + error.getMessage());
            doGet(solicitud, respuesta);
        } catch (NumberFormatException error) {
            solicitud.setAttribute("error", "El identificador no es válido.");
            doGet(solicitud, respuesta);
        }
    }
}
