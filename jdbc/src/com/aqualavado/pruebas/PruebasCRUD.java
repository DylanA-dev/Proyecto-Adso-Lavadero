package com.aqualavado.pruebas;

import com.aqualavado.conexion.ConexionBD;
import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.dao.ServicioDAO;
import com.aqualavado.dao.VehiculoDAO;
import com.aqualavado.modelo.Cliente;
import com.aqualavado.modelo.OrdenLavado;
import com.aqualavado.modelo.Servicio;
import com.aqualavado.modelo.Vehiculo;

import java.math.BigDecimal;
import java.sql.Connection;
import java.time.LocalDateTime;

/**
 * Ejecuta un ciclo completo de inserción, consulta, actualización y
 * eliminación sobre la base de datos, con el fin de verificar el CRUD.
 */
public class PruebasCRUD {

    private static int aprobadas;
    private static int fallidas;

    public static void main(String[] args) {
        try (Connection conexion = ConexionBD.obtener()) {
            verificar("Conexión a la base de datos aqualavado",
                    conexion != null && !conexion.isClosed());
        } catch (Exception error) {
            verificar("Conexión a la base de datos aqualavado", false);
            System.out.println("Detalle: " + error.getMessage());
            return;
        }

        ClienteDAO clienteDAO = new ClienteDAO();
        VehiculoDAO vehiculoDAO = new VehiculoDAO();
        ServicioDAO servicioDAO = new ServicioDAO();
        OrdenLavadoDAO ordenDAO = new OrdenLavadoDAO();

        try {
            System.out.println("\n--- CLIENTES ---");
            Cliente cliente = new Cliente("999999999", "Cliente de prueba",
                    "3000000000", "prueba@aqualavado.com", "Calle 1 # 2-3");
            int idCliente = clienteDAO.insertar(cliente);
            verificar("Insertar cliente", idCliente > 0);

            Cliente consultado = clienteDAO.buscarPorId(idCliente);
            verificar("Consultar cliente por id",
                    consultado != null && "999999999".equals(consultado.getDocumento()));

            consultado.setTelefono("3011111111");
            verificar("Actualizar teléfono del cliente", clienteDAO.actualizar(consultado));
            verificar("Verificar actualización",
                    "3011111111".equals(clienteDAO.buscarPorId(idCliente).getTelefono()));

            System.out.println("\n--- VEHÍCULOS ---");
            Vehiculo vehiculo = new Vehiculo("TST999", "Renault", "Sandero",
                    "Negro", idCliente);
            int idVehiculo = vehiculoDAO.insertar(vehiculo);
            verificar("Insertar vehículo", idVehiculo > 0);
            verificar("Consultar vehículo con su cliente",
                    vehiculoDAO.buscarPorId(idVehiculo) != null);

            System.out.println("\n--- SERVICIOS ---");
            Servicio servicio = new Servicio("Prueba", "Servicio temporal",
                    new BigDecimal("15000.00"), 20, true);
            int idServicio = servicioDAO.insertar(servicio);
            verificar("Insertar servicio", idServicio > 0);
            servicio.setPrecio(new BigDecimal("17000.00"));
            verificar("Actualizar servicio", servicioDAO.actualizar(servicio));

            System.out.println("\n--- ÓRDENES DE LAVADO ---");
            OrdenLavado orden = new OrdenLavado(idVehiculo, idServicio, 2,
                    OrdenLavado.ESTADO_EN_COLA, new BigDecimal("17000.00"),
                    "Orden generada por la prueba");
            int idOrden = ordenDAO.insertar(orden);
            verificar("Insertar orden de lavado", idOrden > 0);

            verificar("Cambiar estado a EN_PROCESO",
                    ordenDAO.cambiarEstado(idOrden, OrdenLavado.ESTADO_EN_PROCESO, null));
            verificar("Cambiar estado a ENTREGADO",
                    ordenDAO.cambiarEstado(idOrden, OrdenLavado.ESTADO_ENTREGADO,
                            LocalDateTime.now()));
            verificar("Consultar orden actualizada",
                    OrdenLavado.ESTADO_ENTREGADO.equals(
                            ordenDAO.buscarPorId(idOrden).getEstado()));

            System.out.println("\n--- ELIMINACIÓN ---");
            verificar("Eliminar orden", ordenDAO.eliminar(idOrden));
            verificar("Eliminar servicio", servicioDAO.eliminar(idServicio));
            verificar("Eliminar vehículo", vehiculoDAO.eliminar(idVehiculo));
            verificar("Eliminar cliente", clienteDAO.eliminar(idCliente));
            verificar("Confirmar eliminación del cliente",
                    clienteDAO.buscarPorId(idCliente) == null);

        } catch (Exception error) {
            System.out.println("Error durante las pruebas: " + error.getMessage());
            fallidas++;
        }

        System.out.println("\n========================================");
        System.out.println("Pruebas aprobadas: " + aprobadas);
        System.out.println("Pruebas fallidas:  " + fallidas);
        System.out.println("Resultado: " + (fallidas == 0 ? "APROBADO" : "REVISAR"));
        System.out.println("========================================");
    }

    private static void verificar(String nombre, boolean condicion) {
        if (condicion) {
            aprobadas++;
            System.out.println("[OK]    " + nombre);
        } else {
            fallidas++;
            System.out.println("[FALLO] " + nombre);
        }
    }
}
