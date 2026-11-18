package com.aqualavado.escritorio;

import com.aqualavado.dao.ClienteDAO;
import com.aqualavado.dao.OrdenLavadoDAO;
import com.aqualavado.dao.ServicioDAO;
import com.aqualavado.dao.VehiculoDAO;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.SwingUtilities;
import javax.swing.Timer;
import javax.swing.UIManager;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

/**
 * Aplicación de escritorio para la operación del lavadero.
 */
public class AplicacionEscritorio extends JFrame {

    public AplicacionEscritorio(int tabInicial) {
        super("AquaLavado | Escritorio" + sufijo(tabInicial));
        ClienteDAO clienteDAO = new ClienteDAO();
        VehiculoDAO vehiculoDAO = new VehiculoDAO();
        ServicioDAO servicioDAO = new ServicioDAO();
        OrdenLavadoDAO ordenDAO = new OrdenLavadoDAO();

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setMinimumSize(new Dimension(1120, 760));
        setSize(1180, 820);
        setLayout(new BorderLayout());

        add(construirEncabezado(), BorderLayout.NORTH);

        JTabbedPane pestanas = new JTabbedPane();
        pestanas.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        pestanas.addTab("Panel", new PanelResumen(clienteDAO, ordenDAO));
        pestanas.addTab("Clientes", new PanelClientes(clienteDAO));
        pestanas.addTab("Órdenes de lavado",
                new PanelOrdenes(ordenDAO, vehiculoDAO, servicioDAO));
        pestanas.setSelectedIndex(Math.max(0, Math.min(tabInicial, 2)));
        add(pestanas, BorderLayout.CENTER);

        setLocationRelativeTo(null);
    }

    private static String sufijo(int tab) {
        return switch (tab) {
            case 1 -> " - Clientes";
            case 2 -> " - Órdenes";
            default -> " - Panel";
        };
    }

    private JPanel construirEncabezado() {
        JPanel encabezado = new JPanel(new BorderLayout());
        encabezado.setBackground(new Color(14, 58, 125));
        encabezado.setBorder(BorderFactory.createEmptyBorder(14, 22, 14, 22));

        JLabel marca = new JLabel("AQUA LAVADO");
        marca.setForeground(Color.WHITE);
        marca.setFont(new Font("Segoe UI", Font.BOLD, 22));

        JLabel descripcion = new JLabel(
                "Sistema de gestión de lavadero de vehículos · Servicio presencial");
        descripcion.setForeground(new Color(191, 212, 238));
        descripcion.setFont(new Font("Segoe UI", Font.PLAIN, 12));

        JPanel textos = new JPanel(new BorderLayout());
        textos.setOpaque(false);
        textos.add(marca, BorderLayout.NORTH);
        textos.add(descripcion, BorderLayout.SOUTH);
        encabezado.add(textos, BorderLayout.WEST);
        return encabezado;
    }

    /**
     * Genera una imagen de la ventana para las evidencias del proyecto.
     *
     * @param ruta archivo de salida en formato PNG
     */
    public void programarCaptura(String ruta) {
        Timer temporizador = new Timer(1800, evento -> {
            try {
                BufferedImage imagen = new BufferedImage(
                        getWidth(), getHeight(), BufferedImage.TYPE_INT_RGB);
                Graphics2D grafico = imagen.createGraphics();
                paintAll(grafico);
                grafico.dispose();
                ImageIO.write(imagen, "png", new File(ruta));
            } catch (Exception error) {
                error.printStackTrace();
            }
            dispose();
            System.exit(0);
        });
        temporizador.setRepeats(false);
        temporizador.start();
    }

    public static void main(String[] args) {        try {
            for (UIManager.LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (Exception error) {
            // Se conserva el estilo predeterminado del sistema.
        }
        SwingUtilities.invokeLater(() -> {
            int tab = 0;
            String captura = null;
            for (String arg : args) {
                if (arg.startsWith("--tab=")) {
                    try {
                        tab = Integer.parseInt(arg.substring(6));
                    } catch (NumberFormatException error) {
                        tab = 0;
                    }
                } else if (arg.startsWith("--captura=")) {
                    captura = arg.substring(10);
                }
            }
            AplicacionEscritorio ventana = new AplicacionEscritorio(tab);
            ventana.setVisible(true);
            if (captura != null) {
                ventana.programarCaptura(captura);
            }
        });
    }
}
