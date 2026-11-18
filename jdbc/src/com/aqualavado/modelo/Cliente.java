package com.aqualavado.modelo;

/**
 * Cliente registrado en el lavadero.
 */
public class Cliente {

    private int idCliente;
    private String documento;
    private String nombre;
    private String telefono;
    private String correo;
    private String direccion;

    public Cliente() {
    }

    public Cliente(String documento, String nombre, String telefono,
                   String correo, String direccion) {
        this.documento = documento;
        this.nombre = nombre;
        this.telefono = telefono;
        this.correo = correo;
        this.direccion = direccion;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getDocumento() {
        return documento;
    }

    public void setDocumento(String documento) {
        this.documento = documento;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    @Override
    public String toString() {
        return String.format("%-4d %-12s %-24s %-12s %-26s %s",
                idCliente, documento, nombre, telefono,
                correo == null ? "" : correo,
                direccion == null ? "" : direccion);
    }
}
