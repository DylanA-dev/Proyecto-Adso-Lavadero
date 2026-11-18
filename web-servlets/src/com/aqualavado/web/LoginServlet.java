package com.aqualavado.web;

import com.aqualavado.dao.UsuarioDAO;
import com.aqualavado.modelo.Usuario;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.sql.SQLException;

/**
 * Valida las credenciales del usuario y abre la sesión de trabajo.
 */
public class LoginServlet extends HttpServlet {

    private final UsuarioDAO usuarioDAO = new UsuarioDAO();

    @Override
    protected void doPost(HttpServletRequest solicitud, HttpServletResponse respuesta)
            throws ServletException, IOException {
        solicitud.setCharacterEncoding("UTF-8");
        String correo = solicitud.getParameter("correo");
        String clave = solicitud.getParameter("clave");

        try {
            Usuario usuario = usuarioDAO.autenticar(correo, clave);
            if (usuario == null) {
                solicitud.setAttribute("error", "Correo o contraseña incorrectos.");
                solicitud.getRequestDispatcher("/index.jsp").forward(solicitud, respuesta);
                return;
            }
            HttpSession sesion = solicitud.getSession(true);
            sesion.setAttribute("usuario", usuario);
            respuesta.sendRedirect(solicitud.getContextPath() + "/PanelServlet");
        } catch (SQLException error) {
            getServletContext().log("Error de autenticación", error);
            solicitud.setAttribute("error", "No fue posible conectar con la base de datos.");
            solicitud.getRequestDispatcher("/index.jsp").forward(solicitud, respuesta);
        }
    }

    @Override
    protected void doGet(HttpServletRequest solicitud, HttpServletResponse respuesta)
            throws IOException {
        HttpSession sesion = solicitud.getSession(false);
        if (sesion != null) {
            sesion.invalidate();
        }
        respuesta.sendRedirect(solicitud.getContextPath() + "/index.jsp");
    }
}
