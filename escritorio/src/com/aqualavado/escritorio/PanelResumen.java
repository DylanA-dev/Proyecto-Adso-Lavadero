package com.aqualavado.escritorio;

import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.modelo.OrdenLavado;

import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.math.BigDecimal;
import java.util.List;

/**
 * Panel de indicadores de la aplicación de escritorio.
 */
public class PanelResumen extends JPanel {

    private final ClienteDAO clienteDAO;
    private final OrdenLavadoDAO ordenDAO;
    private final JLabel clientes = new JLabel();
    private final JLabel activas = new JLabel();
    private final JLabel ingresos = new JLabel();
    private final DefaultTableModel modelo;

    public PanelResumen(ClienteDAO clienteDAO, OrdenLavadoDAO ordenDAO) {
        this.clienteDAO = clienteDAO;
        this.ordenDAO = ordenDAO;
        setLayout(new BorderLayout(16, 16));
        setBackground(new Color(238, 242, 247));
        setBorder(BorderFactory.createEmptyBorder(18, 20, 18, 20));

        JPanel tarjetas = new JPanel();
        tarjetas.setLayout(new BoxLayout(tarjetas, BoxLayout.X_AXIS));
        tarjetas.add(tarjeta("Clientes", clientes));
        tarjetas.add(tarjeta("Órdenes activas", activas));
        tarjetas.add(tarjeta("Ingresos entregados", ingresos));
        add(tarjetas, BorderLayout.NORTH);

        modelo = new DefaultTableModel(
                new Object[]{"Orden", "Placa", "Servicio", "Estado", "Valor"}, 0) {
            @Override
            public boolean isCellEditable(int fila, int columna) {
                return false;
            }
        };
        JTable tabla = new JTable(modelo);
        tabla.setRowHeight(26);
        tabla.setBackground(Color.WHITE);
        tabla.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
        tabla.setFillsViewportHeight(true);
        int[] anchos = {80, 130, 180, 140, 130};
        for (int i = 0; i < anchos.length; i++) {
            tabla.getColumnModel().getColumn(i).setPreferredWidth(anchos[i]);
        }
        add(new JScrollPane(tabla), BorderLayout.CENTER);
        cargar();
    }

    private JPanel tarjeta(String titulo, JLabel valor) {
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBackground(Color.WHITE);
        panel.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(219, 227, 238)),
                BorderFactory.createEmptyBorder(14, 18, 14, 18)));
        JLabel etiqueta = new JLabel(titulo.toUpperCase());
        etiqueta.setForeground(new Color(107, 114, 128));
        etiqueta.setFont(new Font("Segoe UI", Font.PLAIN, 11));
        valor.setForeground(new Color(14, 58, 125));
        valor.setFont(new Font("Segoe UI", Font.BOLD, 22));
        panel.add(etiqueta, BorderLayout.NORTH);
        panel.add(valor, BorderLayout.CENTER);
        return panel;
    }

    private void cargar() {
        try {
            List<OrdenLavado> ordenes = ordenDAO.listar();
            long enCola = ordenes.stream()
                    .filter(o -> OrdenLavado.ESTADO_EN_COLA.equals(o.getEstado())).count();
            long enProceso = ordenes.stream()
                    .filter(o -> OrdenLavado.ESTADO_EN_PROCESO.equals(o.getEstado())).count();
            BigDecimal total = ordenes.stream()
                    .filter(o -> OrdenLavado.ESTADO_ENTREGADO.equals(o.getEstado()))
                    .map(OrdenLavado::getValor)
                    .reduce(BigDecimal.ZERO, BigDecimal::add);

            clientes.setText(String.valueOf(clienteDAO.listar().size()));
            activas.setText(enCola + " / " + enProceso);
            ingresos.setText("$" + String.format("%,.0f", total));

            modelo.setRowCount(0);
            for (OrdenLavado orden : ordenes) {
                modelo.addRow(new Object[]{
                        orden.getIdOrden(),
                        orden.getPlaca(),
                        orden.getNombreServicio(),
                        orden.getEstado(),
                        "$" + String.format("%,.0f", orden.getValor())});
            }
        } catch (Exception error) {
            clientes.setText("0");
            activas.setText("0 / 0");
            ingresos.setText("$0");
        }
    }
}
