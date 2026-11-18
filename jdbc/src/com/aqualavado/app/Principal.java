package com.aqualavado.app;

import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.dao.ServicioDAO;
import com.aqualavado.dao.VehiculoDAO;
import com.aqualavado.modelo.Cliente;
import com.aqualavado.modelo.OrdenLavado;
import com.aqualavado.modelo.Servicio;
import com.aqualavado.modelo.Vehiculo;

import java.math.BigDecimal;
import java.sql.SQLException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Scanner;

/**
 * Aplicación de consola para la operación básica del lavadero.
 */
public class Principal {

    private static final Scanner TECLADO = new Scanner(System.in);
    private static final ClienteDAO CLIENTE_DAO = new ClienteDAO();
    private static final VehiculoDAO VEHICULO_DAO = new VehiculoDAO();
    private static final ServicioDAO SERVICIO_DAO = new ServicioDAO();
    private static final OrdenLavadoDAO ORDEN_DAO = new OrdenLavadoDAO();

    public static void main(String[] args) {
        int opcion;
        do {
            mostrarMenu();
            opcion = leerEntero("Seleccione una opción: ");
            try {
                ejecutar(opcion);
            } catch (SQLException error) {
                System.out.println("Error de base de datos: " + error.getMessage());
            }
        } while (opcion != 0);
        System.out.println("Fin de la aplicación.");
    }

    private static void mostrarMenu() {
        System.out.println("\n===== AQUALAVADO - GESTIÓN DE LAVADERO =====");
        System.out.println("1. Listar clientes");
        System.out.println("2. Registrar cliente");
        System.out.println("3. Actualizar teléfono de cliente");
        System.out.println("4. Eliminar cliente");
        System.out.println("5. Listar vehículos");
        System.out.println("6. Registrar vehículo");
        System.out.println("7. Listar servicios");
        System.out.println("8. Listar órdenes de lavado");
        System.out.println("9. Registrar orden de lavado");
        System.out.println("10. Avanzar estado de una orden");
        System.out.println("0. Salir");
    }

    private static void ejecutar(int opcion) throws SQLException {
        switch (opcion) {
            case 1 -> listarClientes();
            case 2 -> registrarCliente();
            case 3 -> actualizarCliente();
            case 4 -> eliminarCliente();
            case 5 -> listarVehiculos();
            case 6 -> registrarVehiculo();
            case 7 -> listarServicios();
            case 8 -> listarOrdenes();
            case 9 -> registrarOrden();
            case 10 -> avanzarOrden();
            case 0 -> {
            }
            default -> System.out.println("Opción no válida.");
        }
    }

    private static void listarClientes() throws SQLException {
        List<Cliente> clientes = CLIENTE_DAO.listar();
        System.out.println("\nID   DOCUMENTO    NOMBRE                   TELÉFONO     CORREO");
        clientes.forEach(System.out::println);
        System.out.println("Total: " + clientes.size());
    }

    private static void registrarCliente() throws SQLException {
        Cliente cliente = new Cliente();
        cliente.setDocumento(leerTexto("Documento: "));
        cliente.setNombre(leerTexto("Nombre: "));
        cliente.setTelefono(leerTexto("Teléfono: "));
        cliente.setCorreo(leerTexto("Correo: "));
        cliente.setDireccion(leerTexto("Dirección: "));
        int id = CLIENTE_DAO.insertar(cliente);
        System.out.println("Cliente registrado con id " + id);
    }

    private static void actualizarCliente() throws SQLException {
        int id = leerEntero("Id del cliente: ");
        Cliente cliente = CLIENTE_DAO.buscarPorId(id);
        if (cliente == null) {
            System.out.println("No existe el cliente.");
            return;
        }
        cliente.setTelefono(leerTexto("Nuevo teléfono: "));
        System.out.println(CLIENTE_DAO.actualizar(cliente)
                ? "Cliente actualizado." : "No fue posible actualizar.");
    }

    private static void eliminarCliente() throws SQLException {
        int id = leerEntero("Id del cliente: ");
        System.out.println(CLIENTE_DAO.eliminar(id)
                ? "Cliente eliminado." : "No existe el cliente.");
    }

    private static void listarVehiculos() throws SQLException {
        List<Vehiculo> vehiculos = VEHICULO_DAO.listar();
        System.out.println("\nID   PLACA    MARCA          MODELO         COLOR      CLIENTE");
        vehiculos.forEach(System.out::println);
        System.out.println("Total: " + vehiculos.size());
    }

    private static void registrarVehiculo() throws SQLException {
        Vehiculo vehiculo = new Vehiculo();
        vehiculo.setPlaca(leerTexto("Placa: ").toUpperCase());
        vehiculo.setMarca(leerTexto("Marca: "));
        vehiculo.setModelo(leerTexto("Modelo: "));
        vehiculo.setColor(leerTexto("Color: "));
        vehiculo.setIdCliente(leerEntero("Id del cliente: "));
        int id = VEHICULO_DAO.insertar(vehiculo);
        System.out.println("Vehículo registrado con id " + id);
    }

    private static void listarServicios() throws SQLException {
        List<Servicio> servicios = SERVICIO_DAO.listar();
        System.out.println("\nID   SERVICIO     PRECIO     MIN  ESTADO   DESCRIPCIÓN");
        servicios.forEach(System.out::println);
    }

    private static void listarOrdenes() throws SQLException {
        List<OrdenLavado> ordenes = ORDEN_DAO.listar();
        System.out.println("\nID   PLACA    SERVICIO     OPERARIO       INGRESO          ESTADO           VALOR      OBSERVACIONES");
        ordenes.forEach(System.out::println);
        System.out.println("Total: " + ordenes.size());
    }

    private static void registrarOrden() throws SQLException {
        int idVehiculo = leerEntero("Id del vehículo: ");
        int idServicio = leerEntero("Id del servicio: ");
        int idOperario = leerEntero("Id del operario: ");
        Servicio servicio = SERVICIO_DAO.buscarPorId(idServicio);
        if (servicio == null) {
            System.out.println("El servicio no existe.");
            return;
        }
        OrdenLavado orden = new OrdenLavado(idVehiculo, idServicio, idOperario,
                OrdenLavado.ESTADO_EN_COLA, servicio.getPrecio(),
                leerTexto("Observaciones: "));
        int id = ORDEN_DAO.insertar(orden);
        System.out.println("Orden registrada con id " + id
                + " por valor de " + servicio.getPrecio());
    }

    private static void avanzarOrden() throws SQLException {
        int id = leerEntero("Id de la orden: ");
        OrdenLavado orden = ORDEN_DAO.buscarPorId(id);
        if (orden == null) {
            System.out.println("La orden no existe.");
            return;
        }
        String siguiente = switch (orden.getEstado()) {
            case OrdenLavado.ESTADO_EN_COLA -> OrdenLavado.ESTADO_EN_PROCESO;
            case OrdenLavado.ESTADO_EN_PROCESO -> OrdenLavado.ESTADO_FINALIZADO;
            case OrdenLavado.ESTADO_FINALIZADO -> OrdenLavado.ESTADO_ENTREGADO;
            default -> null;
        };
        if (siguiente == null) {
            System.out.println("La orden ya fue entregada.");
            return;
        }
        LocalDateTime salida = OrdenLavado.ESTADO_ENTREGADO.equals(siguiente)
                ? LocalDateTime.now() : null;
        ORDEN_DAO.cambiarEstado(id, siguiente, salida);
        System.out.println("Nuevo estado: " + siguiente);
    }

    private static String leerTexto(String mensaje) {
        System.out.print(mensaje);
        return TECLADO.nextLine().trim();
    }

    private static int leerEntero(String mensaje) {
        while (true) {
            try {
                System.out.print(mensaje);
                return Integer.parseInt(TECLADO.nextLine().trim());
            } catch (NumberFormatException error) {
                System.out.println("Ingrese un número válido.");
            }
        }
    }
}
