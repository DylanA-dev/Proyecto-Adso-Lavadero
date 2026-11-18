<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="com.aqualavado.modelo.Usuario" %>
<%
    Usuario usuarioSesion = (Usuario) session.getAttribute("usuario");
    if (usuarioSesion == null) {
        response.sendRedirect(request.getContextPath() + "/index.jsp");
        return;
    }
    String seccion = request.getParameter("seccion");
%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AquaLavado | Gestión de lavadero</title>
    <link rel="stylesheet" href="<%= request.getContextPath() %>/css/estilo.css">
</head>
<body>
<div class="contenedor">
    <aside class="barra-lateral">
        <div class="marca-lateral">
            <span class="logo">AQUA</span><span class="logo-acento">LAVADO</span>
            <small>Gestión de lavadero</small>
        </div>
        <nav>
            <a href="<%= request.getContextPath() %>/PanelServlet">Panel principal</a>
            <a href="<%= request.getContextPath() %>/ClienteServlet">Clientes</a>
            <a href="<%= request.getContextPath() %>/OrdenServlet">Órdenes de lavado</a>
            <a href="<%= request.getContextPath() %>/ReporteServlet">Reportes</a>
        </nav>
        <div class="sesion">
            <strong><%= usuarioSesion.getNombre() %></strong>
            <span><%= usuarioSesion.getRol() %></span>
            <a class="cerrar" href="<%= request.getContextPath() %>/LoginServlet">Cerrar sesión</a>
        </div>
    </aside>

    <main class="contenido">
        <header class="cabecera">
            <h1>Gestión de lavadero de vehículos</h1>
            <p>Entrada, proceso y salida de vehículos en el establecimiento</p>
        </header>
