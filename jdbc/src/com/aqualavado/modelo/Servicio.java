package com.aqualavado.modelo;

import java.math.BigDecimal;

/**
 * Servicio de lavado ofrecido por el establecimiento.
 */
public class Servicio {

    private int idServicio;
    private String nombre;
    private String descripcion;
    private BigDecimal precio;
    private int duracionMin;
    private boolean activo;

    public Servicio() {
    }

    public Servicio(String nombre, String descripcion, BigDecimal precio,
                    int duracionMin, boolean activo) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.precio = precio;
        this.duracionMin = duracionMin;
        this.activo = activo;
    }

    public int getIdServicio() {
        return idServicio;
    }

    public void setIdServicio(int idServicio) {
        this.idServicio = idServicio;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public BigDecimal getPrecio() {
        return precio;
    }

    public void setPrecio(BigDecimal precio) {
        this.precio = precio;
    }

    public int getDuracionMin() {
        return duracionMin;
    }

    public void setDuracionMin(int duracionMin) {
        this.duracionMin = duracionMin;
    }

    public boolean isActivo() {
        return activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }

    @Override
    public String toString() {
        return String.format("%-4d %-12s %-10s %-4d %-8s %s",
                idServicio, nombre, precio, duracionMin,
                activo ? "ACTIVO" : "INACTIVO",
                descripcion == null ? "" : descripcion);
    }
}
