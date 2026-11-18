package com.aqualavado.api.controlador;

import com.aqualavado.dao.UsuarioDAO;
import com.aqualavado.modelo.Usuario;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.sql.SQLException;
import java.util.Map;

/**
 * Servicio REST de autenticación de usuarios.
 */
@RestController
@RequestMapping("/api/auth")
public class AuthController {

    private final UsuarioDAO usuarioDAO = new UsuarioDAO();

    public record Credenciales(String correo, String clave) {
    }

    @PostMapping("/login")
    public ResponseEntity<Map<String, Object>> login(@RequestBody Credenciales credenciales)
            throws SQLException {
        Usuario usuario = usuarioDAO.autenticar(
                credenciales.correo(), credenciales.clave());
        if (usuario == null) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("mensaje", "Autenticación fallida"));
        }
        return ResponseEntity.ok(Map.of(
                "mensaje", "Autenticación satisfactoria",
                "usuario", usuario));
    }
}
