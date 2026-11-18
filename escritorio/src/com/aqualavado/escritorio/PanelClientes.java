package com.aqualavado.escritorio;

import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.modelo.Cliente;

import javax.swing.BorderFactory;
import javax.swing.JButton;
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
import java.util.List;

/**
 * Gestión de clientes desde la aplicación de escritorio.
 */
public class PanelClientes extends JPanel {

    private final ClienteDAO clienteDAO;
    private final DefaultTableModel modelo;
    private final JTable tabla;
    private final JTextField documento = new JTextField();
    private final JTextField nombre = new JTextField();
    private final JTextField telefono = new JTextField();
    private final JTextField correo = new JTextField();
    private final JTextField direccion = new JTextField();

    public PanelClientes(ClienteDAO clienteDAO) {
        this.clienteDAO = clienteDAO;
        setLayout(new BorderLayout(16, 16));
        setBackground(new Color(238, 242, 247));
        setBorder(BorderFactory.createEmptyBorder(18, 20, 18, 20));

        modelo = new DefaultTableModel(
                new Object[]{"Id", "Documento", "Nombre", "Teléfono", "Correo"}, 0) {
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
        int[] anchos = {60, 110, 150, 130, 170};
        for (int i = 0; i < anchos.length; i++) {
            tabla.getColumnModel().getColumn(i).setPreferredWidth(anchos[i]);
        }
        add(new JScrollPane(tabla), BorderLayout.CENTER);
        add(construirFormulario(), BorderLayout.SOUTH);

        cargar();
    }

    private JPanel construirFormulario() {
        JPanel formulario = new JPanel(new BorderLayout(8, 8));
        formulario.setBorder(BorderFactory.createTitledBorder("Registrar cliente"));
        formulario.setBackground(new Color(238, 242, 247));

        JPanel campos = new JPanel(new java.awt.GridLayout(2, 5, 10, 4));
        campos.setOpaque(false);
        JTextField[] entradas = {documento, nombre, telefono, correo, direccion};
        String[] etiquetas = {"Documento", "Nombre", "Teléfono", "Correo", "Dirección"};

        for (String etiqueta : etiquetas) {
            JLabel label = new JLabel(etiqueta);
            label.setFont(new Font("Segoe UI", Font.PLAIN, 12));
            campos.add(label);
        }
        for (JTextField entrada : entradas) {
            campos.add(entrada);
        }

        JPanel botones = new JPanel(new java.awt.FlowLayout(java.awt.FlowLayout.LEFT, 8, 0));
        botones.setOpaque(false);

        JButton guardar = new JButton("Guardar cliente");
        guardar.setBackground(new Color(14, 58, 125));
        guardar.setForeground(Color.WHITE);
        guardar.setFont(new Font("Segoe UI", Font.BOLD, 12));

        JButton eliminar = new JButton("Eliminar seleccionado");

        guardar.addActionListener(evento -> guardar());
        eliminar.addActionListener(evento -> eliminar());

        botones.add(guardar);
        botones.add(eliminar);

        formulario.add(campos, BorderLayout.CENTER);
        formulario.add(botones, BorderLayout.SOUTH);
        return formulario;
    }

    private void cargar() {
        try {
            modelo.setRowCount(0);
            List<Cliente> clientes = clienteDAO.listar();
            for (Cliente cliente : clientes) {
                modelo.addRow(new Object[]{
                        cliente.getIdCliente(),
                        cliente.getDocumento(),
                        cliente.getNombre(),
                        cliente.getTelefono(),
                        cliente.getCorreo()});
            }
        } catch (Exception error) {
            JOptionPane.showMessageDialog(this,
                    "No fue posible cargar los clientes: " + error.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void guardar() {
        if (documento.getText().isBlank() || nombre.getText().isBlank()
                || telefono.getText().isBlank()) {
            JOptionPane.showMessageDialog(this,
                    "Documento, nombre y teléfono son obligatorios.",
                    "Validación", JOptionPane.WARNING_MESSAGE);
            return;
        }
        try {
            Cliente cliente = new Cliente(
                    documento.getText().trim(),
                    nombre.getText().trim(),
                    telefono.getText().trim(),
                    correo.getText().trim(),
                    direccion.getText().trim());
            clienteDAO.insertar(cliente);
            limpiar();
            cargar();
            JOptionPane.showMessageDialog(this, "Cliente registrado correctamente.");
        } catch (Exception error) {
            JOptionPane.showMessageDialog(this,
                    "No fue posible guardar el cliente: " + error.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void eliminar() {
        int fila = tabla.getSelectedRow();
        if (fila < 0) {
            JOptionPane.showMessageDialog(this, "Seleccione un cliente de la tabla.");
            return;
        }
        int id = Integer.parseInt(modelo.getValueAt(fila, 0).toString());
        int respuesta = JOptionPane.showConfirmDialog(this,
                "¿Eliminar el cliente seleccionado?", "Confirmación",
                JOptionPane.YES_NO_OPTION);
        if (respuesta != JOptionPane.YES_OPTION) {
            return;
        }
        try {
            clienteDAO.eliminar(id);
            cargar();
        } catch (Exception error) {
            JOptionPane.showMessageDialog(this,
                    "No fue posible eliminar el cliente: " + error.getMessage(),
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void limpiar() {
        documento.setText("");
        nombre.setText("");
        telefono.setText("");
        correo.setText("");
        direccion.setText("");
    }
}
