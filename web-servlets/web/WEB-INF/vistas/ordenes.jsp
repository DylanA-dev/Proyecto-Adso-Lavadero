<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.util.List" %>
<%@ page import="java.math.BigDecimal" %>
<%@ page import="com.aqualavado.modelo.OrdenLavado" %>
<%@ page import="com.aqualavado.modelo.Vehiculo" %>
<%@ page import="com.aqualavado.modelo.Servicio" %>
<%@ page import="com.aqualavado.modelo.Usuario" %>
<%@ include file="comun/encabezado.jsp" %>

<%
    List<OrdenLavado> ordenes = (List<OrdenLavado>) request.getAttribute("ordenes");
    List<Vehiculo> vehiculos = (List<Vehiculo>) request.getAttribute("vehiculos");
    List<Servicio> servicios = (List<Servicio>) request.getAttribute("servicios");
    List<Usuario> operarios = (List<Usuario>) request.getAttribute("operarios");
%>

<% if (request.getAttribute("error") != null) { %>
    <p class="mensaje-error"><%= request.getAttribute("error") %></p>
<% } %>

<section class="bloque">
    <div class="titulo-bloque">
        <h2>Órdenes de lavado</h2>
        <span class="contador"><%= ordenes.size() %> órdenes</span>
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
            <th>Acción</th>
        </tr>
        </thead>
        <tbody>
        <% for (OrdenLavado orden : ordenes) { %>
        <tr>
            <td><%= orden.getIdOrden() %></td>
            <td><%= orden.getPlaca() %></td>
            <td><%= orden.getNombreServicio() %></td>
            <td><%= orden.getNombreOperario() %></td>
            <td><%= orden.getFechaIngreso() %></td>
            <td><span class="estado estado-<%= orden.getEstado().toLowerCase() %>">
                <%= orden.getEstado().replace('_', ' ') %></span></td>
            <td>$<%= String.format("%,.0f", orden.getValor()) %></td>
            <td>
                <% if (!OrdenLavado.ESTADO_ENTREGADO.equals(orden.getEstado())) { %>
                <a class="boton" href="<%= request.getContextPath() %>/OrdenServlet?accion=avanzar&id=<%= orden.getIdOrden() %>">
                    Avanzar
                </a>
                <% } else { %>
                <span class="texto-suave">Entregado</span>
                <% } %>
            </td>
        </tr>
        <% } %>
        </tbody>
    </table>
</section>

<section class="bloque">
    <h2>Registrar orden de lavado</h2>
    <form method="post" action="<%= request.getContextPath() %>/OrdenServlet" class="formulario">
        <div class="campo">
            <label for="vehiculo">Vehículo</label>
            <select id="vehiculo" name="vehiculo" required>
                <% for (Vehiculo vehiculo : vehiculos) { %>
                <option value="<%= vehiculo.getIdVehiculo() %>">
                    <%= vehiculo.getPlaca() %> - <%= vehiculo.getMarca() %> <%= vehiculo.getModelo() %>
                </option>
                <% } %>
            </select>
        </div>
        <div class="campo">
            <label for="servicio">Servicio</label>
            <select id="servicio" name="servicio" required>
                <% for (Servicio servicio : servicios) { %>
                <option value="<%= servicio.getIdServicio() %>">
                    <%= servicio.getNombre() %> - $<%= String.format("%,.0f", servicio.getPrecio()) %>
                </option>
                <% } %>
            </select>
        </div>
        <div class="campo">
            <label for="operario">Operario</label>
            <select id="operario" name="operario" required>
                <% for (Usuario operario : operarios) { %>
                <option value="<%= operario.getIdUsuario() %>"><%= operario.getNombre() %></option>
                <% } %>
            </select>
        </div>
        <div class="campo campo-amplio">
            <label for="observaciones">Observaciones</label>
            <input type="text" id="observaciones" name="observaciones" maxlength="200"
                   placeholder="Detalles del vehículo o del servicio">
        </div>
        <button type="submit" class="boton-principal">Registrar orden</button>
    </form>
</section>

<%@ include file="comun/pie.jsp" %>
