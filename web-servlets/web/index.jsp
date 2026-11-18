<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AquaLavado | Inicio de sesión</title>
    <link rel="stylesheet" href="css/estilo.css">
</head>
<body class="pantalla-login">
<main class="tarjeta-login">
    <div class="marca">
        <span class="logo">AQUA</span><span class="logo-acento">LAVADO</span>
        <p>Sistema de gestión de lavadero de vehículos</p>
    </div>

    <form method="post" action="LoginServlet" autocomplete="off">
        <label for="correo">Correo electrónico</label>
        <input type="email" id="correo" name="correo" required
               placeholder="admin@aqualavado.com">

        <label for="clave">Contraseña</label>
        <input type="password" id="clave" name="clave" required
               minlength="6" placeholder="Ingrese su contraseña">

        <button type="submit" class="boton-principal">Ingresar</button>
    </form>

    <% if (request.getAttribute("error") != null) { %>
        <p class="mensaje-error"><%= request.getAttribute("error") %></p>
    <% } %>

    <p class="pie-login">El servicio se presta en las instalaciones del lavadero.</p>
</main>
</body>
</html>
