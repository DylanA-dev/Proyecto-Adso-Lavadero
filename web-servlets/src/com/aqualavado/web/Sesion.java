package com.aqualavado.web;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

/**
 * Utilidades compartidas por los servlets de la aplicación.
 */
public final class Sesion {

    private Sesion() {
    }

    public static boolean activa(HttpServletRequest solicitud) {
        HttpSession sesion = solicitud.getSession(false);
        return sesion != null && sesion.getAttribute("usuario") != null;
    }
}
