package com.aqualavado.modelo;

/**
 * Vehículo asociado a un cliente del lavadero.
 */
public class Vehiculo {

    private int idVehiculo;
    private String placa;
    private String marca;
    private String modelo;
    private String color;
    private int idCliente;
    private String nombreCliente;

    public Vehiculo() {
    }

    public Vehiculo(String placa, String marca, String modelo, String color, int idCliente) {
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
        this.color = color;
        this.idCliente = idCliente;
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

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getNombreCliente() {
        return nombreCliente;
    }

    public void setNombreCliente(String nombreCliente) {
        this.nombreCliente = nombreCliente;
    }

    @Override
    public String toString() {
        return String.format("%-4d %-8s %-14s %-14s %-10s %s",
                idVehiculo, placa, marca, modelo, color,
                nombreCliente == null ? String.valueOf(idCliente) : nombreCliente);
    }
}
