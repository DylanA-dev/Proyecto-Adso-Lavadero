package com.aqualavado.modelo;

import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * Orden de lavado generada cuando el vehículo ingresa al establecimiento.
 */
public class OrdenLavado {

    public static final String ESTADO_EN_COLA = "EN_COLA";
    public static final String ESTADO_EN_PROCESO = "EN_PROCESO";
    public static final String ESTADO_FINALIZADO = "FINALIZADO";
    public static final String ESTADO_ENTREGADO = "ENTREGADO";

    private int idOrden;
    private int idVehiculo;
    private String placa;
    private int idServicio;
    private String nombreServicio;
    private int idOperario;
    private String nombreOperario;
    private LocalDateTime fechaIngreso;
    private LocalDateTime fechaSalida;
    private String estado;
    private BigDecimal valor;
    private String observaciones;

    public OrdenLavado() {
    }

    public OrdenLavado(int idVehiculo, int idServicio, int idOperario,
                       String estado, BigDecimal valor, String observaciones) {
        this.idVehiculo = idVehiculo;
        this.idServicio = idServicio;
        this.idOperario = idOperario;
        this.estado = estado;
        this.valor = valor;
        this.observaciones = observaciones;
    }

    public int getIdOrden() {
        return idOrden;
    }

    public void setIdOrden(int idOrden) {
        this.idOrden = idOrden;
    }

    public int getIdVehiculo() {
        return idVehiculo;
    }

    public void setIdVehiculo(int idVehiculo) {
        this.idVehiculo = idVehiculo;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public int getIdServicio() {
        return idServicio;
    }

    public void setIdServicio(int idServicio) {
        this.idServicio = idServicio;
    }

    public String getNombreServicio() {
        return nombreServicio;
    }

    public void setNombreServicio(String nombreServicio) {
        this.nombreServicio = nombreServicio;
    }

    public int getIdOperario() {
        return idOperario;
    }

    public void setIdOperario(int idOperario) {
        this.idOperario = idOperario;
    }

    public String getNombreOperario() {
        return nombreOperario;
    }

    public void setNombreOperario(String nombreOperario) {
        this.nombreOperario = nombreOperario;
    }

    public LocalDateTime getFechaIngreso() {
        return fechaIngreso;
    }

    public void setFechaIngreso(LocalDateTime fechaIngreso) {
        this.fechaIngreso = fechaIngreso;
    }

    public LocalDateTime getFechaSalida() {
        return fechaSalida;
    }

    public void setFechaSalida(LocalDateTime fechaSalida) {
        this.fechaSalida = fechaSalida;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public BigDecimal getValor() {
        return valor;
    }

    public void setValor(BigDecimal valor) {
        this.valor = valor;
    }

    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }

    @Override
    public String toString() {
        return String.format("%-4d %-8s %-12s %-14s %-12s %-16s %-10s %s",
                idOrden, placa, nombreServicio, nombreOperario,
                fechaIngreso == null ? "" : fechaIngreso.toString().replace('T', ' '),
                estado, valor, observaciones == null ? "" : observaciones);
    }
}
