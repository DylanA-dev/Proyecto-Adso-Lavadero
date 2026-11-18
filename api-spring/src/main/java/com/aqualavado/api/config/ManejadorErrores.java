package com.aqualavado.api.config;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.sql.SQLException;
import java.util.Map;

/**
 * Convierte los errores de la API en respuestas JSON con un mensaje claro.
 */
@RestControllerAdvice
public class ManejadorErrores {

    @ExceptionHandler(SQLException.class)
    public ResponseEntity<Map<String, String>> errorBaseDatos(SQLException error) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(Map.of("error", "Error de base de datos",
                        "detalle", error.getMessage()));
    }

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<Map<String, String>> solicitudInvalida(IllegalArgumentException error) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                .body(Map.of("error", "Solicitud inválida",
                        "detalle", error.getMessage()));
    }
}
