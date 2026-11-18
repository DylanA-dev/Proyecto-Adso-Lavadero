package com.aqualavado.escritorio;

import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.dao.ServicioDAO;
import com.aqualavado.dao.UsuarioDAO;
import com.aqualavado.dao.VehiculoDAO;
import com.aqualavado.modelo.OrdenLavado;
import com.aqualavado.modelo.Servicio;
import com.aqualavado.modelo.Usuario;
import com.aqualavado.modelo.Vehiculo;

import javax.swing.BorderFactory;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableModel;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.time.LocalDateTime;
import java.util.List;

/**
 * Registro y control de órdenes de lavado desde la aplicación de escritorio.
 */
public class PanelOrdenes extends JPanel {

    private final OrdenLavadoDAO ordenDAO;
    private final VehiculoDAO vehiculoDAO;
    private final ServicioDAO servicioDAO;
    private final UsuarioDAO usuarioDAO;

    private final DefaultTableModel modelo;
    private final JTable tabla;
    private final JComboBox<Vehiculo> vehiculos = new JComboBox<>();
    private final JComboBox<Servicio> servicios = new JComboBox<>();
    private final JComboBox<Usuario> operarios = new JComboBox<>();
    private final JTextField observaciones = new JTextField();

    public PanelOrdenes(OrdenLavadoDAO ordenDAO, VehiculoDAO vehiculoDAO,
                        ServicioDAO servicioDAO) {
        this.ordenDAO = ordenDAO;
        this.vehiculoDAO = vehiculoDAO;
        this.servicioDAO = servicioDAO;
        this.usuarioDAO = new UsuarioDAO();

        setLayout(new BorderLayout(16, 16));
        setBackground(new Color(238, 242, 247));
        setBorder(BorderFactory.createEmptyBorder(18, 20, 18, 20));

        modelo = new DefaultTableModel(
                new Object[]{"Orden", "Placa", "Servicio", "Operario", "Estado", "Valor"}, 0) {
            @Override
            public boolean isCellEditable(int fila, int columna) {
                return false;
            }
        };
        tabla = new JTable(modelo);
        tabla.setRowHeight(28);
        tabla.setBackground(Color.WHITE);
        tabla.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
        tabla.setFillsViewportHeight(true);
        tabla.getTableHeader().setFont(new Font("Segoe UI", Font.BOLD, 12));
        int[] anchos = {70, 110, 140, 140, 110, 90};
        for (int i = 0; i < anchos.length; i++) {
            tabla.getColumnModel().getColumn(i).setPreferredWidth(anchos[i]);
        }
        add(new JScrollPane(tabla), BorderLayout.CENTER);
        add(construirPanelInferior(), BorderLayout.SOUTH);

        cargarCombos();
        configurarRenderizadores();
        cargar();
    }

    private void configurarRenderizadores() {
        vehiculos.setRenderer(new javax.swing.DefaultListCellRenderer() {
            @Override
            public java.awt.Component getListCellRendererComponent(
                    javax.swing.JList<?> lista, Object valor, int indice,
                    boolean seleccionado, boolean enfocado) {
                super.getListCellRendererComponent(lista, valor, indice, seleccionado, enfocado);
                if (valor instanceof Vehiculo vehiculo) {
                    setText(vehiculo.getPlaca() + " - " + vehiculo.getMarca()
                            + " " + vehiculo.getModelo());
                }
                return this;
            }
        });
        servicios.setRenderer(new javax.swing.DefaultListCellRenderer() {
            @Override
            public java.awt.Component getListCellRendererComponent(
                    javax.swing.JList<?> lista, Object valor, int indice,
                    boolean seleccionado, boolean enfocado) {
                super.getListCellRendererComponent(lista, valor, indice, seleccionado, enfocado);
                if (valor instanceof Servicio servicio) {
                    setText(servicio.getNombre() + " - $"
                            + String.format("%,.0f", servicio.getPrecio()));
                }
                return this;
            }
        });
        operarios.setRenderer(new javax.swing.DefaultListCellRenderer() {
            @Override
            public java.awt.Component getListCellRendererComponent(
                    javax.swing.JList<?> lista, Object valor, int indice,
                    boolean seleccionado, boolean enfocado) {
                super.getListCellRendererComponent(lista, valor, indice, seleccionado, enfocado);
                if (valor instanceof Usuario usuario) {
                    setText(usuario.getNombre());
                }
                return this;
            }
        });
    }

    private JPanel construirPanelInferior() {
        JPanel panel = new JPanel(new BorderLayout(8, 8));
        panel.setBorder(BorderFactory.createTitledBorder("Registrar orden de lavado"));
        panel.setBackground(new Color(238, 242, 247));

        JPanel campos = new JPanel(new java.awt.GridLayout(2, 4, 10, 4));
        campos.setOpaque(false);

        String[] etiquetas = {"Vehículo", "Servicio", "Operario", "Observaciones"};
        for (String etiqueta : etiquetas) {
            JLabel label = new JLabel(etiqueta);
            label.setFont(new Font("Segoe UI", Font.PLAIN, 12));
            campos.add(label);
        }
        campos.add(vehiculos);
        campos.add(servicios);
        campos.add(operarios);
        campos.add(observaciones);

        JPanel botones = new JPanel(new java.awt.FlowLayout(java.awt.FlowLayout.LEFT, 8, 0));
        botones.setOpaque(false);

        JButton registrar = new JButton("Registrar orden");
        registrar.setBackground(new Color(14, 58, 125));
        registrar.setForeground(Color.WHITE);
        registrar.setFont(new Font("Segoe UI", Font.BOLD, 12));

        JButton avanzar = new JButton("Avanzar estado");
        JButton actualizar = new JButton("Actualizar listado");

        registrar.addActionListener(evento -> registrar());
        avanzar.addActionListener(evento -> avanzar());
        actualizar.addActionListener(evento -> cargar());

        botones.add(registrar);
        botones.add(avanzar);
        botones.add(actualizar);

        panel.add(campos, BorderLayout.CENTER);
        panel.add(botones, BorderLayout.SOUTH);
        return panel;
    }

    private void cargarCombos() {
        try {
            List<Vehiculo> listaVehiculos = vehiculoDAO.listar();
            vehiculos.setModel(new DefaultComboBoxModel<>(listaVehiculos.toArray(new Vehiculo[0])));
            servicios.setModel(new DefaultComboBoxModel<>(
                    servicioDAO.listar().toArray(new Servicio[0])));
            operarios.setModel(new DefaultComboBoxModel<>(
                    usuarioDAO.listarActivos().toArray(new Usuario[0])));
        } catch (Exception error) {
            JOptionPane.showMessageDialog(this,
                    "No fue posible cargar los catálogos: " + error.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void cargar() {
        try {
            modelo.setRowCount(0);
            for (OrdenLavado orden : ordenDAO.listar()) {
                modelo.addRow(new Object[]{
                        orden.getIdOrden(),
                        orden.getPlaca(),
                        orden.getNombreServicio(),
                        orden.getNombreOperario(),
                        orden.getEstado().replace('_', ' '),
                        "$" + String.format("%,.0f", orden.getValor())});
            }
        } catch (Exception error) {
            JOptionPane.showMessageDialog(this,
                    "No fue posible cargar las órdenes: " + error.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void registrar() {
        Vehiculo vehiculo = (Vehiculo) vehiculos.getSelectedItem();
        Servicio servicio = (Servicio) servicios.getSelectedItem();
        Usuario operario = (Usuario) operarios.getSelectedItem();
        if (vehiculo == null || servicio == null || operario == null) {
            JOptionPane.showMessageDialog(this, "Seleccione vehículo, servicio y operario.");
            return;
        }
        try {
            OrdenLavado orden = new OrdenLavado(
                    vehiculo.getIdVehiculo(),
                    servicio.getIdServicio(),
                    operario.getIdUsuario(),
                    OrdenLavado.ESTADO_EN_COLA,
                    servicio.getPrecio(),
                    observaciones.getText().trim());
            ordenDAO.insertar(orden);
            observaciones.setText("");
            cargar();
            JOptionPane.showMessageDialog(this,
                    "Orden registrada por valor de " + servicio.getPrecio());
        } catch (Exception error) {
            JOptionPane.showMessageDialog(this,
                    "No fue posible registrar la orden: " + error.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void avanzar() {
        int fila = tabla.getSelectedRow();
        if (fila < 0) {
            JOptionPane.showMessageDialog(this, "Seleccione una orden de la tabla.");
            return;
        }
        int id = Integer.parseInt(modelo.getValueAt(fila, 0).toString());
        try {
            OrdenLavado orden = ordenDAO.buscarPorId(id);
            String siguiente = switch (orden.getEstado()) {
                case OrdenLavado.ESTADO_EN_COLA -> OrdenLavado.ESTADO_EN_PROCESO;
                case OrdenLavado.ESTADO_EN_PROCESO -> OrdenLavado.ESTADO_FINALIZADO;
                case OrdenLavado.ESTADO_FINALIZADO -> OrdenLavado.ESTADO_ENTREGADO;
                default -> null;
            };
            if (siguiente == null) {
                JOptionPane.showMessageDialog(this, "La orden ya fue entregada.");
                return;
            }
            LocalDateTime salida = OrdenLavado.ESTADO_ENTREGADO.equals(siguiente)
                    ? LocalDateTime.now() : null;
            ordenDAO.cambiarEstado(id, siguiente, salida);
            cargar();
        } catch (Exception error) {
            JOptionPane.showMessageDialog(this,
                    "No fue posible actualizar la orden: " + error.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
}
