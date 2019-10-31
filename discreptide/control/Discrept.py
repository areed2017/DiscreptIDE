import os
import subprocess
import sys
from tkinter import END, Text

from discrept_pac.parsetree import Compiler
from discrept_pac.printpdf import print_pdf
from discrept_pac.tokenizer import parse

from discreptide.control import FileTools
from discreptide.model import get_file
from discreptide.view.TextEditor import TextEditor
from discreptide.view.pdf_viewer import PDFViewer


def discrept(text_field: TextEditor, pdf_viewer: PDFViewer):
    if not FileTools.save_file(text_field):
        return

    data = text_field.get(0.0, END)
    token_stream = parse(data)

    styles_path = ""
    for path in sys.path:
        if 'python3.6' in path:
            styles_path = os.path.dirname(os.path.abspath(path)) + "/../styles/"
            break
        if 'Python36' in path:
            styles_path = os.path.dirname(os.path.abspath(path)) + "\\styles\\"
            break
    compiler = Compiler(token_stream, {'styles': styles_path})
    with open(get_file().replace(".dis", '.html'), 'w') as file_:
        file_.write(compiler.build())

    print_pdf(get_file().replace(".dis", ""))
    pdf_viewer._update_page()


def view_discrept(pdf_viewer: PDFViewer):
    pdf_viewer._open_file(get_file().replace('.dis', '.pdf'))
