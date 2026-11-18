<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.util.Map" %>
<%@ page import="java.math.BigDecimal" %>
<%@ include file="comun/encabezado.jsp" %>

<%
    Map<String, Integer> cantidades = (Map<String, Integer>) request.getAttribute("cantidades");
    Map<String, BigDecimal> valores = (Map<String, BigDecimal>) request.getAttribute("valores");
    BigDecimal totalIngresos = (BigDecimal) request.getAttribute("totalIngresos");
    BigDecimal promedio = (BigDecimal) request.getAttribute("promedio");
%>

<section class="tarjetas">
    <article class="tarjeta">
        <span class="etiqueta">Lavados entregados</span>
        <strong><%= request.getAttribute("entregadas") %></strong>
        <small>órdenes cerradas</small>
    </article>
    <article class="tarjeta">
        <span class="etiqueta">Ingresos</span>
        <strong>$<%= String.format("%,.0f", totalIngresos) %></strong>
        <small>valor de los servicios entregados</small>
    </article>
    <article class="tarjeta">
        <span class="etiqueta">Ticket promedio</span>
        <strong>$<%= String.format("%,.0f", promedio) %></strong>
        <small>por vehículo entregado</small>
    </article>
</section>

<section class="bloque">
    <h2>Lavados por tipo de servicio</h2>
    <table class="tabla">
        <thead>
        <tr>
            <th>Servicio</th>
            <th>Cantidad de órdenes</th>
            <th>Valor acumulado</th>
        </tr>
        </thead>
        <tbody>
        <% for (String servicio : cantidades.keySet()) { %>
        <tr>
            <td><%= servicio %></td>
            <td><%= cantidades.get(servicio) %></td>
            <td>$<%= String.format("%,.0f", valores.get(servicio)) %></td>
        </tr>
        <% } %>
        </tbody>
    </table>
</section>

<%@ include file="comun/pie.jsp" %>
