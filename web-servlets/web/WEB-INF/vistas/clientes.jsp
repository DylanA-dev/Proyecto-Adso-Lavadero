<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.util.List" %>
<%@ page import="com.aqualavado.modelo.Cliente" %>
<%@ include file="comun/encabezado.jsp" %>

<%
    List<Cliente> clientes = (List<Cliente>) request.getAttribute("clientes");
%>

<section class="bloque">
    <div class="titulo-bloque">
        <h2>Clientes registrados</h2>
        <span class="contador"><%= clientes.size() %> clientes</span>
    </div>
    <table class="tabla">
        <thead>
        <tr>
            <th>Id</th>
            <th>Documento</th>
            <th>Nombre</th>
            <th>Teléfono</th>
            <th>Correo</th>
            <th>Dirección</th>
            <th>Acción</th>
        </tr>
        </thead>
        <tbody>
        <% for (Cliente cliente : clientes) { %>
        <tr>
            <td><%= cliente.getIdCliente() %></td>
            <td><%= cliente.getDocumento() %></td>
            <td><%= cliente.getNombre() %></td>
            <td><%= cliente.getTelefono() %></td>
            <td><%= cliente.getCorreo() %></td>
            <td><%= cliente.getDireccion() %></td>
            <td>
                <form method="post" action="<%= request.getContextPath() %>/ClienteServlet"
                      onsubmit="return confirm('¿Eliminar el cliente seleccionado?');">
                    <input type="hidden" name="accion" value="eliminar">
                    <input type="hidden" name="id" value="<%= cliente.getIdCliente() %>">
                    <button type="submit" class="boton-secundario">Eliminar</button>
                </form>
            </td>
        </tr>
        <% } %>
        </tbody>
    </table>
</section>

<section class="bloque">
    <h2>Registrar cliente</h2>
    <form method="post" action="<%= request.getContextPath() %>/ClienteServlet" class="formulario">
        <div class="campo">
            <label for="documento">Documento</label>
            <input type="text" id="documento" name="documento" required maxlength="15"
                   pattern="[0-9]{6,15}" title="Entre 6 y 15 dígitos">
        </div>
        <div class="campo">
            <label for="nombre">Nombre completo</label>
            <input type="text" id="nombre" name="nombre" required maxlength="80">
        </div>
        <div class="campo">
            <label for="telefono">Teléfono</label>
            <input type="tel" id="telefono" name="telefono" required maxlength="15"
                   pattern="[0-9]{7,15}" title="Entre 7 y 15 dígitos">
        </div>
        <div class="campo">
            <label for="correo">Correo</label>
            <input type="email" id="correo" name="correo" maxlength="100">
        </div>
        <div class="campo">
            <label for="direccion">Dirección</label>
            <input type="text" id="direccion" name="direccion" maxlength="120">
        </div>
        <button type="submit" class="boton-principal">Guardar cliente</button>
    </form>
</section>

<%@ include file="comun/pie.jsp" %>
