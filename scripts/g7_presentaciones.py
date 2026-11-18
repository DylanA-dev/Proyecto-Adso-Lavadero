# -*- coding: utf-8 -*-
"""Genera las presentaciones de AA1-EV05 y AA3-EV02 para exponer."""
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt
from lxml import etree
from pptx.oxml.ns import qn

CAPTURAS = Path(r"C:\Users\dylan\Documents\OpenCode\ADSO\proyectos\lavadero\interfaz\capturas")
SALIDA = Path(r"C:\Users\dylan\Documents\OpenCode\ADSO\ACTIVIDADES\G7")

AZUL = RGBColor(0x0E, 0x3A, 0x7D)
AZUL_OSCURO = RGBColor(0x0B, 0x2A, 0x5B)
CIAN = RGBColor(0x22, 0xD3, 0xEE)
FONDO = RGBColor(0xF4, 0xF7, 0xFB)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
TEXTO = RGBColor(0x1F, 0x29, 0x37)
GRIS = RGBColor(0x64, 0x74, 0x8B)
BORDE = RGBColor(0xDD, 0xE5, 0xEF)
VERDE = RGBColor(0x15, 0x80, 0x3D)

FUENTE = "Segoe UI"

def rgb_hex(color):
    return "%02X%02X%02X" % (color[0], color[1], color[2])

def sombra(forma):
    sp_pr = forma._element.spPr
    efecto = etree.SubElement(sp_pr, qn("a:effectLst"))
    sombra_el = etree.SubElement(efecto, qn("a:outerShdw"))
    sombra_el.set("blurRad", "80000")
    sombra_el.set("dist", "25000")
    sombra_el.set("dir", "5400000")
    sombra_el.set("algn", "ctr")
    sombra_el.set("rotWithShape", "0")
    color = etree.SubElement(sombra_el, qn("a:srgbClr"))
    color.set("val", "0B2A5B")
    alfa = etree.SubElement(color, qn("a:alpha"))
    alfa.set("val", "15000")

def caja_texto(slide, x, y, w, h):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    return tf

def escribir(tf, texto, size, color, bold=False, align=PP_ALIGN.LEFT,
            espacio=0, primera=True, italic=False):
    parrafo = tf.paragraphs[0] if primera else tf.add_paragraph()
    parrafo.alignment = align
    parrafo.space_after = Pt(espacio)
    partes = texto.split("**")
    for indice, parte in enumerate(partes):
        if not parte:
            continue
        run = parrafo.add_run()
        run.text = parte
        run.font.name = FUENTE
        run.font.size = Pt(size)
        run.font.color.rgb = color
        run.font.bold = bold or indice % 2 == 1
        run.font.italic = italic
    return parrafo

def fondo(slide, color=FONDO):
    relleno = slide.background.fill
    relleno.solid()
    relleno.fore_color.rgb = color

def banda(slide, codigo):
    barra = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0,
                                   Inches(13.333), Inches(0.72))
    barra.fill.solid()
    barra.fill.fore_color.rgb = AZUL_OSCURO
    barra.line.fill.background()

    tf = caja_texto(slide, 0.55, 0.18, 6.0, 0.4)
    escribir(tf, "AQUA LAVADO", 15, BLANCO, bold=True)

    tf2 = caja_texto(slide, 7.0, 0.22, 5.8, 0.3)
    escribir(tf2, codigo, 10.5, RGBColor(0xBF, 0xD4, 0xEE),
             align=PP_ALIGN.RIGHT)

    linea = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(0.72),
                                   Inches(13.333), Inches(0.045))
    linea.fill.solid()
    linea.fill.fore_color.rgb = CIAN
    linea.line.fill.background()

def titulo_slide(prs, titulo, subtitulo=None, codigo="", numero=None,
                 total=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    fondo(slide)
    banda(slide, codigo)

    tf = caja_texto(slide, 0.6, 1.0, 12.1, 0.7)
    escribir(tf, titulo, 27, AZUL, bold=True)

    if subtitulo:
        tf2 = caja_texto(slide, 0.6, 1.68, 12.1, 0.45)
        escribir(tf2, subtitulo, 13, GRIS)

    pie = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6),
                                 Inches(7.03), Inches(12.13), Inches(0.012))
    pie.fill.solid()
    pie.fill.fore_color.rgb = BORDE
    pie.line.fill.background()

    tf3 = caja_texto(slide, 0.6, 7.1, 9.5, 0.28)
    escribir(tf3, "Dylan Arias · SENA ADSO · Ficha 3186703", 9, GRIS)

    if numero and total:
        tf4 = caja_texto(slide, 11.9, 7.1, 0.85, 0.28)
        escribir(tf4, f"{numero} / {total}", 9, GRIS, align=PP_ALIGN.RIGHT)
    return slide

def vinetas(slide, items, x, y, w, h, size=15, espacio=9):
    tf = caja_texto(slide, x, y, w, h)
    primera = True
    for item in items:
        texto = "■   " + item
        parrafo = tf.paragraphs[0] if primera else tf.add_paragraph()
        parrafo.space_after = Pt(espacio)
        parrafo.line_spacing = 1.05
        run = parrafo.add_run()
        run.text = "■   "
        run.font.name = FUENTE
        run.font.size = Pt(size - 2)
        run.font.color.rgb = CIAN
        partes = item.split("**")
        for indice, parte in enumerate(partes):
            if not parte:
                continue
            r = parrafo.add_run()
            r.text = parte
            r.font.name = FUENTE
            r.font.size = Pt(size)
            r.font.color.rgb = TEXTO
            r.font.bold = indice % 2 == 1
        primera = False
    return tf

def imagen(slide, ruta, x, y, w, h, caption=None):
    ruta = Path(ruta)
    with Image.open(ruta) as im:
        ratio = im.width / im.height

    caja_ratio = w / h
    if ratio >= caja_ratio:
        ancho = w
        alto = w / ratio
    else:
        alto = h
        ancho = h * ratio
    px = x + (w - ancho) / 2
    py = y + (h - alto) / 2

    tarjeta = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(px - 0.1), Inches(py - 0.1),
        Inches(ancho + 0.2), Inches(alto + 0.2))
    tarjeta.fill.solid()
    tarjeta.fill.fore_color.rgb = BLANCO
    tarjeta.line.color.rgb = BORDE
    tarjeta.line.width = Pt(0.75)
    tarjeta.adjustments[0] = 0.05
    sombra(tarjeta)

    slide.shapes.add_picture(str(ruta), Inches(px), Inches(py),
                             Inches(ancho), Inches(alto))

    if caption:
        tf = caja_texto(slide, x, y + h + 0.14, w, 0.3)
        escribir(tf, caption, 9.5, GRIS, italic=True, align=PP_ALIGN.CENTER)

def tabla(slide, encabezados, filas, x, y, w, h, anchos=None, size=11):
    forma = slide.shapes.add_table(len(filas) + 1, len(encabezados),
                                   Inches(x), Inches(y), Inches(w), Inches(h))
    t = forma.table
    if anchos:
        for i, ancho in enumerate(anchos):
            t.columns[i].width = Inches(ancho)

    for c, texto in enumerate(encabezados):
        celda = t.cell(0, c)
        celda.text = ""
        celda.fill.solid()
        celda.fill.fore_color.rgb = AZUL
        celda.margin_left = Inches(0.08)
        celda.margin_right = Inches(0.08)
        tf = celda.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = texto
        r.font.name = FUENTE
        r.font.size = Pt(size)
        r.font.bold = True
        r.font.color.rgb = BLANCO

    for f, fila in enumerate(filas, start=1):
        for c, texto in enumerate(fila):
            celda = t.cell(f, c)
            celda.text = ""
            celda.fill.solid()
            celda.fill.fore_color.rgb = BLANCO if f % 2 else RGBColor(0xF1, 0xF5, 0xFA)
            celda.margin_left = Inches(0.08)
            celda.margin_right = Inches(0.08)
            tf = celda.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            r = p.add_run()
            r.text = texto
            r.font.name = FUENTE
            r.font.size = Pt(size)
            r.font.color.rgb = TEXTO
    return t

def portada(prs, kicker, titulo, subtitulo, codigo, comando=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    fondo(slide, AZUL_OSCURO)

    # Adorno lateral
    barra = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0,
                                   Inches(0.18), Inches(7.5))
    barra.fill.solid()
    barra.fill.fore_color.rgb = CIAN
    barra.line.fill.background()

    circulo = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.9), Inches(-1.6),
                                     Inches(4.2), Inches(4.2))
    circulo.fill.solid()
    circulo.fill.fore_color.rgb = RGBColor(0x10, 0x3F, 0x7F)
    circulo.line.fill.background()

    tf = caja_texto(slide, 0.9, 1.25, 10.6, 0.4)
    escribir(tf, kicker, 11.5, CIAN, bold=True)

    tf2 = caja_texto(slide, 0.9, 1.75, 10.8, 1.9)
    escribir(tf2, titulo, 38, BLANCO, bold=True)

    tf3 = caja_texto(slide, 0.9, 3.35, 9.8, 0.8)
    escribir(tf3, subtitulo, 17, RGBColor(0xBF, 0xD4, 0xEE))

    linea = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9),
                                   Inches(4.35), Inches(1.6), Inches(0.05))
    linea.fill.solid()
    linea.fill.fore_color.rgb = CIAN
    linea.line.fill.background()

    tf4 = caja_texto(slide, 0.9, 4.65, 7.0, 1.2)
    escribir(tf4, "Dylan David Arias Rojas", 16, BLANCO, bold=True, espacio=2)
    escribir(tf4, "Análisis y Desarrollo de Software · Ficha 3186703",
             11.5, RGBColor(0xBF, 0xD4, 0xEE), primera=False, espacio=2)
    escribir(tf4, "SENA Cartago · Noviembre 2026", 11.5,
             RGBColor(0xBF, 0xD4, 0xEE), primera=False)

    tf5 = caja_texto(slide, 0.9, 6.65, 8.0, 0.3)
    escribir(tf5, codigo, 10.5, RGBColor(0x8F, 0xB0, 0xD8))

    if comando:
        panel = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.15), Inches(4.6),
            Inches(4.55), Inches(2.05))
        panel.fill.solid()
        panel.fill.fore_color.rgb = RGBColor(0x07, 0x1B, 0x36)
        panel.line.color.rgb = RGBColor(0x1E, 0x4C, 0x8A)
        panel.adjustments[0] = 0.06
        sombra(panel)

        tf6 = caja_texto(slide, 8.38, 4.78, 4.1, 1.7)
        for i, linea_cmd in enumerate(comando):
            p = tf6.paragraphs[0] if i == 0 else tf6.add_paragraph()
            p.space_after = Pt(4)
            r = p.add_run()
            r.text = linea_cmd
            r.font.name = "Consolas"
            r.font.size = Pt(11)
            r.font.color.rgb = CIAN if linea_cmd.startswith("$") else RGBColor(0xCB, 0xD5, 0xE1)

    return slide

# ---------------------------------------------------------------- Git
def presentacion_git():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    codigo = "GA7-220501096-AA1-EV05"

    portada(
        prs,
        "EVIDENCIA DE DESEMPEÑO · AA1-EV05",
        "Versionamiento con Git",
        "Ejercicio práctico sobre el repositorio Programa-Git",
        codigo,
        ["$ git init -b master",
         "$ git add .",
         '$ git commit -m "Añadido datos."',
         "$ git push github master"],
    )

    s = titulo_slide(prs, "¿Qué se va a demostrar?",
                     "Ciclo completo de Git local y remoto", codigo, 2, 8)
    vinetas(s, [
        "Crear el repositorio local del programa.",
        "Registrar el nombre y el correo en **kotlin.txt**.",
        'Confirmar los cambios con el mensaje **"Añadido datos."**',
        "Enlazar el repositorio público **Programa-Git**.",
        "Publicar y verificar el historial en GitHub.",
    ], 0.6, 2.35, 6.3, 3.6)
    imagen(s, CAPTURAS / "git_version_crop.png", 7.2, 2.55, 5.6, 2.1,
           "Git instalado y verificado en el equipo")

    s = titulo_slide(prs, "Paso 1 · Repositorio local y enlace remoto",
                     "Programa-Git: creación e integración con GitHub", codigo, 3, 8)
    vinetas(s, [
        "Crear la carpeta **Programa-Git** e ingresar a ella.",
        "Inicializar el repositorio en la rama **master**.",
        "Enlazar el remoto con **git remote add github**.",
        "Comprobar las URL con **git remote -v**.",
    ], 0.6, 2.15, 5.9, 1.3, size=13.5)
    vinetas(s, [
        "El repositorio queda en la carpeta **.git**.",
        "El remoto **github** apunta a la URL de GitHub.",
    ], 6.8, 2.15, 5.9, 1.3, size=13.5)
    imagen(s, CAPTURAS / "git_paso1.png", 0.75, 3.75, 11.8, 2.75,
           "Creación del repositorio y enlace con el remoto")

    s = titulo_slide(prs, "Paso 2 · Archivo y confirmación",
                     "Preparar los cambios y registrar el commit", codigo, 4, 8)
    vinetas(s, [
        "Crear **kotlin.txt** con el nombre y el correo.",
        "Agregar los cambios con **git add .**",
        "Revisar el estado con **git status**.",
        'Confirmar con **git commit -m "Añadido datos."**',
    ], 0.6, 2.15, 5.9, 1.3, size=13.5)
    vinetas(s, [
        "El archivo pasa al área de preparación.",
        "El commit registra autor, fecha y mensaje.",
    ], 6.8, 2.15, 5.9, 1.3, size=13.5)
    imagen(s, CAPTURAS / "git_paso2.png", 0.75, 3.6, 11.8, 2.55,
           "Área de preparación y confirmación de los cambios")

    s = titulo_slide(prs, "Paso 3 · Publicación en GitHub",
                     "Enviar la rama master al repositorio remoto", codigo, 5, 8)
    vinetas(s, [
        "Publicar con **git push github master**.",
        "Verificar el archivo **kotlin.txt** en GitHub.",
        "Comprobar el mensaje **Añadido datos.** en el historial.",
        "Confirmar que local y remoto quedan sincronizados.",
    ], 0.6, 2.15, 5.9, 1.3, size=13.5)
    vinetas(s, [
        "El commit local y **origin/master** coinciden.",
        "El historial conserva el registro del ejercicio.",
    ], 6.8, 2.15, 5.9, 1.3, size=13.5)
    imagen(s, CAPTURAS / "git_paso3.png", 0.75, 3.6, 11.8, 2.4,
           "Enlace del remoto e historial de confirmaciones")

    s = titulo_slide(prs, "Configuración del entorno",
                     "Identidad, rama inicial y manejo de finales de línea", codigo, 6, 8)
    imagen(s, CAPTURAS / "git_config_crop.png", 1.85, 2.0, 9.6, 4.35)
    tf = caja_texto(s, 0.9, 6.55, 11.5, 0.4)
    escribir(tf, "Usuario **DylanA-dev** · correo **dylandavidariasrojas@gmail.com** · "
                 "rama inicial **main** · autocrlf **true**", 11, GRIS,
             align=PP_ALIGN.CENTER)

    s = titulo_slide(prs, "Comandos utilizados",
                     "Git local y Git remoto en el ejercicio", codigo, 7, 8)
    tabla(s, ["Comando", "Tipo", "Función"], [
        ["git init -b master", "Local", "Crear el repositorio en la rama master."],
        ["git status", "Local", "Consultar el estado de los archivos."],
        ["git add .", "Local", "Agregar los cambios al área de preparación."],
        ["git commit -m", "Local", "Registrar los cambios con un mensaje."],
        ["git log --oneline", "Local", "Consultar el historial resumido."],
        ["git remote add", "Remoto", "Enlazar el repositorio local con el remoto."],
        ["git remote -v", "Remoto", "Listar los repositorios remotos."],
        ["git push", "Remoto", "Publicar los commits en GitHub."],
    ], 0.75, 2.05, 11.8, 4.4, anchos=[3.5, 2.0, 6.3], size=12)

    s = titulo_slide(prs, "Verificación y cierre",
                     "Repositorio sincronizado y evidencia publicada", codigo, 8, 8)
    vinetas(s, [
        "Remoto **origin** configurado con la URL de GitHub.",
        "Rama **main** sincronizada con **origin/main**.",
        "Historial con los commits del proyecto.",
        "Árbol de trabajo limpio, sin cambios pendientes.",
    ], 0.6, 2.3, 5.4, 3.3, size=14)
    imagen(s, CAPTURAS / "git_repositorio_crop.png", 6.2, 2.15, 6.55, 3.6,
           "Repositorio local, ramas e historial")
    tf = caja_texto(s, 0.6, 5.95, 12.1, 0.6)
    escribir(tf, "Repositorio: https://github.com/DylanA-dev/Proyecto-Adso-Lavadero",
             11.5, AZUL)

    destino = SALIDA / "GA7-220501096-AA1-EV05-Presentacion.pptx"
    prs.save(destino)
    return destino

# ---------------------------------------------------------------- Pruebas
def presentacion_pruebas():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    codigo = "GA7-220501096-AA3-EV02"

    portada(
        prs,
        "EVIDENCIA DE PRODUCTO · AA3-EV02",
        "AquaLavado: módulos probados",
        "Funcionamiento y validaciones del sistema de lavadero",
        codigo,
    )

    # Tres versiones
    s = titulo_slide(prs, "AquaLavado en tres versiones",
                     "Misma base de datos, mismas reglas de negocio", codigo, 2, 12)
    columnas = [
        ("Stand-alone", "Java Swing", "Operación local en el computador del lavadero.",
         ["Panel de indicadores", "Clientes", "Órdenes y estados"]),
        ("Web", "Spring Boot + React", "API REST y front-end para el navegador.",
         ["Servicios REST", "Clientes y órdenes", "Reportes"]),
        ("Móvil", "React + PWA", "Aplicación instalable para el teléfono del operario.",
         ["Diseño responsivo", "Barra inferior", "Instalación en pantalla de inicio"]),
    ]
    x = 0.6
    for nombre, tecnologia, descripcion, items in columnas:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x),
                                  Inches(2.2), Inches(3.95), Inches(4.3))
        card.fill.solid()
        card.fill.fore_color.rgb = BLANCO
        card.line.color.rgb = BORDE
        card.adjustments[0] = 0.05
        sombra(card)

        tf = caja_texto(s, x + 0.25, 2.45, 3.45, 0.45)
        escribir(tf, nombre, 20, AZUL, bold=True)
        tf2 = caja_texto(s, x + 0.25, 2.95, 3.45, 0.35)
        escribir(tf2, tecnologia, 11.5, CIAN, bold=True)
        tf3 = caja_texto(s, x + 0.25, 3.4, 3.45, 0.9)
        escribir(tf3, descripcion, 12, GRIS)
        tf4 = caja_texto(s, x + 0.25, 4.35, 3.45, 1.9)
        primera = True
        for item in items:
            p = tf4.paragraphs[0] if primera else tf4.add_paragraph()
            p.space_after = Pt(7)
            r = p.add_run()
            r.text = "•  " + item
            r.font.name = FUENTE
            r.font.size = Pt(12.5)
            r.font.color.rgb = TEXTO
            primera = False
        x += 4.15

    tf = caja_texto(s, 0.6, 6.65, 12.1, 0.35)
    escribir(tf, "Servicio presencial en el establecimiento · No contempla lavados a domicilio",
             11, GRIS, italic=True)

    historias = [
        ("HU-01", "Inicio de sesión", "Acceso con credenciales válidas", "react_login_crop.png",
         ["Valida correo y contraseña contra el hash SHA-256.",
          "Abre la sesión y carga el panel principal.",
          "Muestra un mensaje si las credenciales fallan."],
         "Acceso con credenciales válidas y mensaje de error si fallan."),
        ("HU-02", "Panel de indicadores", "Resumen de la operación del lavadero", "react_panel.png",
         ["Órdenes activas en cola y en proceso.",
          "Lavados entregados e ingresos.",
          "Últimas órdenes con su estado."],
         "El panel reúne los indicadores principales y las últimas órdenes registradas."),
        ("HU-03", "Registro de clientes", "Datos personales y de contacto", "react_clientes.png",
         ["Documento de 6 a 15 dígitos.",
          "Teléfono de 7 a 15 dígitos.",
          "Correo con formato válido y longitudes máximas."],
         "El formulario valida documento, teléfono y correo, y muestra el cliente en la tabla."),
        ("HU-04", "Registro de órdenes", "Entrada del vehículo al lavadero", "react_ordenes.png",
         ["Selección de vehículo, servicio y operario.",
          "El valor se toma del precio del servicio.",
          "La orden se crea en estado EN_COLA."],
         "Al registrar la orden, el sistema toma el precio del servicio y crea la orden en cola."),
        ("HU-06", "Reportes", "Ingresos y lavados por servicio", "react_reportes.png",
         ["Lavados entregados e ingresos totales.",
          "Ticket promedio por vehículo.",
          "Cantidad y valor acumulado por servicio."],
         "El reporte consolida los ingresos y los lavados por tipo de servicio."),
    ]

    numero = 3
    for hu, titulo, subtitulo, archivo, items, nota in historias:
        s = titulo_slide(prs, f"{hu} · {titulo}", subtitulo, codigo, numero, 12)
        vinetas(s, items, 0.6, 2.3, 4.9, 3.8, size=13.5)
        imagen(s, CAPTURAS / archivo, 5.9, 2.0, 6.85, 4.3, nota)
        numero += 1

    # HU-05 estados (escritorio)
    s = titulo_slide(prs, "HU-05 · Control de estados",
                     "Seguimiento del lavado hasta la entrega", codigo, numero, 12)
    vinetas(s, [
        "Secuencia: **EN_COLA → EN_PROCESO → FINALIZADO → ENTREGADO**.",
        "El botón Avanzar actualiza el estado de la orden.",
        "Al entregar se registra la fecha de salida.",
        "La operación se verificó también en la versión de escritorio.",
    ], 0.6, 2.3, 4.9, 3.8, size=13)
    imagen(s, CAPTURAS / "escritorio_ordenes.png", 5.9, 2.0, 6.85, 4.1,
           "Órdenes y estados en la aplicación de escritorio")
    numero += 1

    # HU-07 escritorio
    s = titulo_slide(prs, "HU-07 · Operación desde el escritorio",
                     "Aplicación stand-alone para el computador del lavadero", codigo, numero, 12)
    vinetas(s, [
        "Interfaz con pestañas para panel, clientes y órdenes.",
        "Acceso directo a la base de datos MySQL.",
        "Registro de clientes y control de órdenes.",
        "Validaciones y mensajes de confirmación.",
    ], 0.6, 2.3, 4.9, 3.8, size=13)
    imagen(s, CAPTURAS / "escritorio_clientes.png", 5.9, 2.0, 6.85, 4.1,
           "Gestión de clientes en la aplicación de escritorio")
    numero += 1

    # HU-08 móvil
    s = titulo_slide(prs, "HU-08 · Operación desde el móvil",
                     "Versión instalable y adaptada al teléfono", codigo, numero, 12)
    vinetas(s, [
        "Barra de navegación inferior.",
        "Tarjetas en una columna y tablas adaptadas.",
        "Consulta y registro de órdenes desde el teléfono.",
        "Instalación como aplicación en la pantalla de inicio.",
    ], 0.6, 2.3, 6.0, 3.8, size=13)
    imagen(s, CAPTURAS / "react_movil.png", 6.9, 1.9, 5.7, 4.7,
           "Panel principal en la versión móvil")
    numero += 1

    # Validaciones
    s = titulo_slide(prs, "Validaciones aplicadas",
                     "Protección de los datos antes de llegar a la base de datos", codigo,
                     numero, 12)
    tabla(s, ["Tipo", "Dato ingresado", "Resultado"], [
        ["Número", "Documento con letras", "Rechazado por el patrón numérico"],
        ["Longitud", "Documento de 5 dígitos", "Rechazado (mínimo 6)"],
        ["Longitud", "Documento de 16 dígitos", "Rechazado (máximo 15)"],
        ["Número", "Teléfono de 6 dígitos", "Rechazado (mínimo 7)"],
        ["Texto", "Nombre vacío", "Rechazado por campo obligatorio"],
        ["Correo", "Correo sin arroba", "Rechazado por el tipo email"],
        ["Especiales", "María Gómez / Camilo Ríos", "Aceptado y conserva las tildes"],
        ["Número", "Valor modificado en el formulario", "Se toma del precio del servicio"],
        ["Longitud", "Observación de 201 caracteres", "Limitada a 200"],
    ], 0.75, 2.05, 11.8, 4.4, anchos=[2.2, 5.4, 4.2], size=11.5)
    numero += 1

    # Resultados
    s = titulo_slide(prs, "Resultados de las pruebas",
                     "Trazabilidad entre historias de usuario e implementación", codigo,
                     numero, 12)

    datos = [("20", "pruebas aprobadas"), ("0", "pruebas fallidas"),
             ("8", "historias de usuario"), ("3", "versiones probadas")]
    x = 0.7
    for valor, etiqueta in datos:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x),
                                  Inches(2.2), Inches(2.85), Inches(1.75))
        card.fill.solid()
        card.fill.fore_color.rgb = BLANCO
        card.line.color.rgb = BORDE
        card.adjustments[0] = 0.08
        sombra(card)
        tf = caja_texto(s, x + 0.2, 2.45, 2.45, 0.7)
        escribir(tf, valor, 34, AZUL, bold=True)
        tf2 = caja_texto(s, x + 0.2, 3.2, 2.45, 0.5)
        escribir(tf2, etiqueta, 11.5, GRIS)
        x += 3.0

    vinetas(s, [
        "Validaciones en navegador y servidor.",
        "Consultas parametrizadas con PreparedStatement.",
        "Pruebas ejecutadas sobre datos reales en MySQL.",
        "Documentación con captura por cada historia de usuario.",
    ], 0.75, 4.35, 11.6, 2.2, size=13)

    tf = caja_texto(s, 0.75, 6.35, 11.8, 0.4)
    escribir(tf, "Sistema probado y disponible para la sustentación del proyecto.",
             12.5, VERDE, bold=True)

    destino = SALIDA / "GA7-220501096-AA3-EV02-Presentacion.pptx"
    prs.save(destino)
    return destino

if __name__ == "__main__":
    # Recortes de las capturas para mejorar la lectura en pantalla
    origen = Image.open(CAPTURAS / "git_ejercicio.png")
    origen.crop((0, 40, origen.width, 255)).save(CAPTURAS / "git_paso1.png")
    origen.crop((0, 240, origen.width, 405)).save(CAPTURAS / "git_paso2.png")
    origen.crop((0, 385, origen.width, origen.height)).save(CAPTURAS / "git_paso3.png")

    version = Image.open(CAPTURAS / "git_version.png")
    version.crop((0, 0, version.width, 250)).save(CAPTURAS / "git_version_crop.png")

    config = Image.open(CAPTURAS / "git_config.png")
    config.crop((0, 0, config.width, 415)).save(CAPTURAS / "git_config_crop.png")

    repo = Image.open(CAPTURAS / "git_repositorio.png")
    repo.crop((0, 0, repo.width, 400)).save(CAPTURAS / "git_repositorio_crop.png")

    login = Image.open(CAPTURAS / "react_login.png")
    login.crop((280, 145, 860, 700)).save(CAPTURAS / "react_login_crop.png")

    print(presentacion_git())
    print(presentacion_pruebas())
