<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.util.List" %>
<%@ page import="java.math.BigDecimal" %>
<%@ page import="com.aqualavado.modelo.OrdenLavado" %>
<%@ include file="comun/encabezado.jsp" %>

<%
    List<OrdenLavado> ordenes = (List<OrdenLavado>) request.getAttribute("ordenes");
    BigDecimal ingresos = (BigDecimal) request.getAttribute("ingresos");
%>

<section class="tarjetas">
    <article class="tarjeta">
        <span class="etiqueta">Clientes</span>
        <strong><%= request.getAttribute("totalClientes") %></strong>
        <small>registrados en el sistema</small>
    </article>
    <article class="tarjeta">
        <span class="etiqueta">Vehículos</span>
        <strong><%= request.getAttribute("totalVehiculos") %></strong>
        <small>asociados a clientes</small>
    </article>
    <article class="tarjeta">
        <span class="etiqueta">Órdenes activas</span>
        <strong><%= request.getAttribute("enCola") %> / <%= request.getAttribute("enProceso") %></strong>
        <small>en cola / en proceso</small>
    </article>
    <article class="tarjeta">
        <span class="etiqueta">Ingresos entregados</span>
        <strong>$<%= String.format("%,.0f", ingresos) %></strong>
        <small>lavados entregados</small>
    </article>
</section>

<section class="bloque">
    <div class="titulo-bloque">
        <h2>Últimas órdenes de lavado</h2>
        <a class="boton" href="<%= request.getContextPath() %>/OrdenServlet">Registrar orden</a>
    </div>
    <table class="tabla">
        <thead>
        <tr>
            <th>Orden</th>
            <th>Placa</th>
            <th>Servicio</th>
            <th>Operario</th>
            <th>Ingreso</th>
            <th>Estado</th>
            <th>Valor</th>
        </tr>
        </thead>
        <tbody>
        <%
            int limite = 0;
            for (OrdenLavado orden : ordenes) {
                if (limite++ >= 8) {
                    break;
                }
        %>
        <tr>
            <td><%= orden.getIdOrden() %></td>
            <td><%= orden.getPlaca() %></td>
            <td><%= orden.getNombreServicio() %></td>
            <td><%= orden.getNombreOperario() %></td>
            <td><%= orden.getFechaIngreso() %></td>
            <td><span class="estado estado-<%= orden.getEstado().toLowerCase() %>">
                <%= orden.getEstado().replace('_', ' ') %></span></td>
            <td>$<%= String.format("%,.0f", orden.getValor()) %></td>
        </tr>
        <% } %>
        </tbody>
    </table>
</section>

<%@ include file="comun/pie.jsp" %>
