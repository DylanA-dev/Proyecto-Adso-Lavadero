# -*- coding: utf-8 -*-
"""Generador de evidencias SENA para el proyecto AquaLavado (GA7).

Copia la plantilla institucional, inserta el contenido con los estilos de la
guía, actualiza la tabla de contenido y exporta el PDF con Word.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.text.paragraph import Paragraph

PLANTILLA = Path(r"C:\Users\dylan\Documents\OpenCode\ADSO\ACTIVIDADES\1GUIA_PARA_SENA .docx")
SALIDA = Path(r"C:\Users\dylan\Documents\OpenCode\ADSO\ACTIVIDADES\G7")
AUTOR = "Dylan Arias"


def _norm(texto: str) -> str:
    import unicodedata

    return (
        unicodedata.normalize("NFKD", texto)
        .encode("ascii", "ignore")
        .decode()
        .upper()
    )


class SenaDoc:
    def __init__(self, codigo: str, titulo: str, fecha: str = "Noviembre 2026"):
        SALIDA.mkdir(parents=True, exist_ok=True)
        self.codigo_evidencia = codigo
        self.titulo = titulo
        self.fecha = fecha
        self.docx_path = SALIDA / f"{codigo}.docx"
        self.pdf_path = SALIDA / f"{codigo}.pdf"
        self.tabla_num = 0
        self.figura_num = 0

        shutil.copy2(PLANTILLA, self.docx_path)
        self.doc = Document(self.docx_path)

        self._portada()
        self._toc()
        self._numeracion()
        self._propiedades()
        self._secciones()

        self.intro_h = self._buscar("INTRODUCCIÓN")
        self.desarrollo_h = self._buscar("DESARROLLO DE LA ACTIVIDAD")
        self.conclusion_h = self._buscar("CONCLUSIÓN")
        self.anchor = self.intro_h._p

    # ------------------------------------------------------------------ base
    def _buscar(self, objetivo: str):
        t = _norm(objetivo)
        for p in self.doc.paragraphs:
            if t in _norm(p.text):
                return p
        raise ValueError(f"No se encontró el título: {objetivo}")

    def _portada(self):
        p = self._buscar("Evidencia de conocimiento")
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
        p.add_run(self.codigo_evidencia)

        sub = OxmlElement("w:p")
        p._p.addnext(sub)
        par = Paragraph(sub, p._parent)
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = par.add_run(self.titulo)
        run.bold = True
        run.font.size = Pt(12)

        fecha = self._buscar("MES")
        for r in list(fecha.runs):
            r._r.getparent().remove(r._r)
        fecha.add_run(self.fecha)

    def _toc(self):
        titulo = self._buscar("Tabla de Contenidos")
        anterior = titulo._p.getprevious()
        if anterior is not None and anterior.tag == qn("w:p"):
            texto = "".join(anterior.itertext()).strip()
            tiene_salto = any(
                br.get(qn("w:type")) == "page" for br in anterior.iter(qn("w:br"))
            )
            if not texto and tiene_salto:
                anterior.getparent().remove(anterior)
        titulo.paragraph_format.page_break_before = True

        # La plantilla trae un control de contenido con una tabla desactualizada.
        siguiente = titulo._p.getnext()
        if siguiente is not None and siguiente.tag == qn("w:sdt"):
            siguiente.getparent().remove(siguiente)

        p = OxmlElement("w:p")
        titulo._p.addnext(p)

        def run_fld(tipo, texto=None, dirty=False):
            r = OxmlElement("w:r")
            if tipo == "instr":
                el = OxmlElement("w:instrText")
                el.set(qn("xml:space"), "preserve")
                el.text = texto
            elif tipo == "text":
                el = OxmlElement("w:t")
                el.text = texto
            else:
                el = OxmlElement("w:fldChar")
                el.set(qn("w:fldCharType"), tipo)
                if dirty:
                    el.set(qn("w:dirty"), "true")
            r.append(el)
            return r

        p.append(run_fld("begin", dirty=True))
        p.append(run_fld("instr", ' TOC \\o "1-3" \\h \\z \\u '))
        p.append(run_fld("separate"))
        p.append(run_fld("text", "Actualice el campo para ver la tabla de contenido."))
        p.append(run_fld("end"))

        # Quita los párrafos vacíos que separaban la tabla del contenido.
        actual = p.getnext()
        while actual is not None:
            if actual.tag == qn("w:p"):
                texto = "".join(actual.itertext()).strip()
                tiene_salto = any(
                    br.get(qn("w:type")) == "page" for br in actual.iter(qn("w:br"))
                )
                if texto or tiene_salto:
                    break
                siguiente = actual.getnext()
                actual.getparent().remove(actual)
                actual = siguiente
            else:
                break

    def _secciones(self):
        """Deja cada sección mayor en una página nueva y sin saltos duplicados."""
        for objetivo in ("INTRODUCCIÓN", "DESARROLLO DE LA ACTIVIDAD", "CONCLUSIÓN"):
            par = self._buscar(objetivo)
            anterior = par._p.getprevious()
            if anterior is not None and anterior.tag == qn("w:p"):
                texto = "".join(anterior.itertext()).strip()
                tiene_salto = any(
                    br.get(qn("w:type")) == "page" for br in anterior.iter(qn("w:br"))
                )
                if not texto and tiene_salto:
                    anterior.getparent().remove(anterior)
            par.paragraph_format.page_break_before = True

    def _numeracion(self):
        section = self.doc.sections[0]
        footer = section.footer
        par = footer.paragraphs[0]
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = par.add_run()
        begin = OxmlElement("w:fldChar")
        begin.set(qn("w:fldCharType"), "begin")
        instr = OxmlElement("w:instrText")
        instr.set(qn("xml:space"), "preserve")
        instr.text = " PAGE "
        end = OxmlElement("w:fldChar")
        end.set(qn("w:fldCharType"), "end")
        run._r.append(begin)
        run._r.append(instr)
        run._r.append(end)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)

    def _propiedades(self):
        cp = self.doc.core_properties
        cp.author = AUTOR
        cp.last_modified_by = AUTOR
        cp.title = f"{self.codigo_evidencia} - {self.titulo}"
        cp.subject = "SENA ADSO - Ficha 3186703"
        cp.keywords = "AquaLavado, SENA, ADSO, GA7-220501096"
        cp.comments = ""

        settings = self.doc.settings.element
        el = OxmlElement("w:updateFields")
        el.set(qn("w:val"), "true")
        settings.append(el)

    # ------------------------------------------------------------- inserción
    def _despues(self, elemento, estilo="Normal"):
        p = OxmlElement("w:p")
        elemento.addnext(p)
        return Paragraph(p, self.doc._body)

    def _texto_con_negrita(self, par, texto):
        partes = re.split(r"(\*\*.+?\*\*)", texto)
        for parte in partes:
            if not parte:
                continue
            if parte.startswith("**") and parte.endswith("**"):
                r = par.add_run(parte[2:-2])
                r.bold = True
            else:
                par.add_run(parte)

    def salto(self):
        p = self._despues(self.anchor)
        run = p.add_run()
        run.add_break(6)  # WD_BREAK.PAGE
        self.anchor = p._p
        return self

    def h2(self, texto):
        p = self._despues(self.anchor, "Heading 2")
        p.style = self.doc.styles["Heading 2"]
        r = p.add_run(texto)
        r.bold = True
        r.font.size = Pt(12)
        r.font.name = "Times New Roman"
        r.font.color.rgb = RGBColor(0, 0, 0)
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        self.anchor = p._p
        return self

    def h3(self, texto):
        p = self._despues(self.anchor, "Heading 3")
        p.style = self.doc.styles["Heading 3"]
        r = p.add_run(texto)
        r.bold = True
        r.font.size = Pt(11)
        r.font.name = "Times New Roman"
        r.font.color.rgb = RGBColor(0, 0, 0)
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        self.anchor = p._p
        return self

    def p(self, texto, align=WD_ALIGN_PARAGRAPH.JUSTIFY, size=12, italic=False,
          space_after=6, bold=False):
        par = self._despues(self.anchor)
        par.alignment = align
        par.paragraph_format.space_after = Pt(space_after)
        par.paragraph_format.line_spacing = 1.15
        self._texto_con_negrita(par, texto)
        for r in par.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(size)
            if italic:
                r.italic = True
            if bold:
                r.bold = True
        self.anchor = par._p
        return self

    def bullets(self, items, size=12):
        for item in items:
            par = self._despues(self.anchor)
            par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            par.paragraph_format.left_indent = Cm(0.75)
            par.paragraph_format.first_line_indent = Cm(-0.35)
            par.paragraph_format.space_after = Pt(3)
            par.paragraph_format.line_spacing = 1.15
            self._texto_con_negrita(par, "• " + item)
            for r in par.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(size)
            self.anchor = par._p
        return self

    def numeros(self, items, size=12):
        for i, item in enumerate(items, start=1):
            par = self._despues(self.anchor)
            par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            par.paragraph_format.left_indent = Cm(0.9)
            par.paragraph_format.first_line_indent = Cm(-0.5)
            par.paragraph_format.space_after = Pt(3)
            par.paragraph_format.line_spacing = 1.15
            self._texto_con_negrita(par, f"{i}. {item}")
            for r in par.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(size)
            self.anchor = par._p
        return self

    def codigo(self, texto, size=8.5):
        lineas = texto.split("\n")
        for i, linea in enumerate(lineas):
            par = self._despues(self.anchor)
            par.alignment = WD_ALIGN_PARAGRAPH.LEFT
            par.paragraph_format.left_indent = Cm(0.5)
            par.paragraph_format.space_after = Pt(0)
            par.paragraph_format.space_before = Pt(0)
            par.paragraph_format.line_spacing = 1.0
            par.paragraph_format.keep_with_next = i < len(lineas) - 1
            run = par.add_run(linea if linea else " ")
            run.font.name = "Consolas"
            run.font.size = Pt(size)
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:color"), "auto")
            shd.set(qn("w:fill"), "F4F4F4")
            par._p.get_or_add_pPr().append(shd)
            self.anchor = par._p
        self.p(" ", size=4, space_after=2)
        return self

    def tabla(self, encabezados, filas, anchos=None, caption=None, size=8):
        self.tabla_num += 1
        if caption:
            self.p(f"Tabla {self.tabla_num}. {caption}", size=8, italic=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)

        tabla = self.doc.add_table(rows=1 + len(filas), cols=len(encabezados))
        tabla.autofit = False

        tbl_pr = tabla._tbl.tblPr
        borders = OxmlElement("w:tblBorders")
        for borde in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement("w:" + borde)
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "4")
            el.set(qn("w:color"), "BFBFBF")
            borders.append(el)
        tbl_pr.append(borders)

        margenes = OxmlElement("w:tblCellMar")
        for lado, valor in (("top", 40), ("left", 70), ("bottom", 40), ("right", 70)):
            el = OxmlElement("w:" + lado)
            el.set(qn("w:w"), str(valor))
            el.set(qn("w:type"), "dxa")
            margenes.append(el)
        tbl_pr.append(margenes)

        datos = [encabezados] + [[str(c) for c in fila] for fila in filas]
        for r, fila in enumerate(datos):
            for c, valor in enumerate(fila):
                celda = tabla.rows[r].cells[c]
                celda.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                celda.text = ""
                par = celda.paragraphs[0]
                par.paragraph_format.space_after = Pt(0)
                par.paragraph_format.space_before = Pt(0)
                par.paragraph_format.line_spacing = 1.0
                run = par.add_run(valor)
                run.font.name = "Calibri"
                run.font.size = Pt(size)
                if r == 0:
                    run.bold = True
                    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    shd = OxmlElement("w:shd")
                    shd.set(qn("w:val"), "clear")
                    shd.set(qn("w:color"), "auto")
                    shd.set(qn("w:fill"), "F2F2F2")
                    celda._tc.get_or_add_tcPr().append(shd)
                if anchos:
                    celda.width = Cm(anchos[c])

        if anchos:
            for col, ancho in zip(tabla.columns, anchos):
                col.width = Cm(ancho)

        # Repite el encabezado si la tabla pasa de página.
        tr_pr = tabla.rows[0]._tr.get_or_add_trPr()
        cabecera = OxmlElement("w:tblHeader")
        cabecera.set(qn("w:val"), "true")
        tr_pr.append(cabecera)

        self.anchor.addnext(tabla._tbl)
        self.anchor = tabla._tbl
        self.p(" ", size=4, space_after=2)
        return self

    def imagen(self, ruta, caption=None, ancho_cm=15.0):
        ruta = Path(ruta)
        if not ruta.exists():
            raise FileNotFoundError(f"No existe la imagen: {ruta}")
        par = self._despues(self.anchor)
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        par.paragraph_format.space_before = Pt(6)
        par.paragraph_format.space_after = Pt(2)
        par.add_run().add_picture(str(ruta), width=Cm(ancho_cm))
        self.anchor = par._p
        if caption:
            self.figura_num += 1
            self.p(f"Figura {self.figura_num}. {caption}", size=8.5, italic=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
        return self

    def intro(self, parrafos):
        for texto in parrafos:
            self.p(texto)
        return self

    def desarrollo(self):
        self.anchor = self.desarrollo_h._p
        return self

    def conclusion(self, parrafos):
        # Elimina los párrafos espaciadores que queden al final de la página
        # anterior para evitar una página en blanco antes de la conclusión.
        anterior = self.conclusion_h._p.getprevious()
        while anterior is not None and anterior.tag == qn("w:p"):
            texto = "".join(anterior.itertext()).strip()
            tiene_salto = any(
                br.get(qn("w:type")) == "page" for br in anterior.iter(qn("w:br"))
            )
            if not texto and not tiene_salto:
                previo = anterior.getprevious()
                anterior.getparent().remove(anterior)
                anterior = previo
            else:
                break

        self.anchor = self.conclusion_h._p
        for texto in parrafos:
            self.p(texto)
        return self

    def bibliografia(self, referencias):
        h = self._despues(self.anchor, "Heading 1")
        h.style = self.doc.styles["Heading 1"]
        h.paragraph_format.page_break_before = True
        r = h.add_run("BIBLIOGRAFÍA")
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(14)
        r.font.color.rgb = RGBColor(0, 0, 0)
        h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self.anchor = h._p

        self.p("Referencias — Norma APA 7ª edición", size=9, italic=True,
               align=WD_ALIGN_PARAGRAPH.LEFT, space_after=8)
        for ref in referencias:
            par = self._despues(self.anchor)
            par.alignment = WD_ALIGN_PARAGRAPH.LEFT
            par.paragraph_format.left_indent = Cm(1.0)
            par.paragraph_format.first_line_indent = Cm(-1.0)
            par.paragraph_format.space_after = Pt(5)
            par.paragraph_format.line_spacing = 1.0
            run = par.add_run(ref)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9.5)
            self.anchor = par._p
        return self

    # ---------------------------------------------------------------- salida
    def guardar(self):
        self.doc.save(self.docx_path)
        self._exportar()
        return self.docx_path, self.pdf_path

    def _exportar(self):
        import win32com.client

        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        try:
            documento = word.Documents.Open(str(self.docx_path))
            documento.Fields.Update()
            if documento.TablesOfContents.Count:
                documento.TablesOfContents(1).Update()
            documento.Save()
            documento.ExportAsFixedFormat(
                OutputFileName=str(self.pdf_path),
                ExportFormat=17,
                OpenAfterExport=False,
                OptimizeFor=0,
                CreateBookmarks=1,
            )
            documento.Close(False)
        finally:
            word.Quit()
