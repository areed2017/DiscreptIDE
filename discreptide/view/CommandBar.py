from tkinter import *
from tkinter.font import Font

from pdfviewer import PDFViewer

from discreptide.control import Discrept
from discreptide.model.Settings import Settings
from discreptide.view.TextEditor import TextEditor


class CommandBar(Frame):

    def __init__(self, parent, editor: TextEditor, pdf_viewer: PDFViewer):
        super().__init__(parent, background='light grey')

        self.open = Button(self, text="+", background='light grey',
                           command=lambda: pdf_viewer._zoom_in())
        self.open.pack(side=RIGHT, pady=(5, 10), padx=(3, 10))

        self.open = Button(self, text="-", background='light grey',
                           command=lambda: pdf_viewer._zoom_out())
        self.open.pack(side=RIGHT, pady=(5, 10), padx=(3, 10))

        self.open = Button(self, text=">", background='light grey',
                           command=lambda: pdf_viewer._next_page())
        self.open.pack(side=RIGHT, pady=(5, 10), padx=(3, 10))

        self.open = Button(self, text="Open", background='light grey',
                           command=lambda: Discrept.view_discrept(pdf_viewer))
        self.open.pack(side=RIGHT, pady=(5, 10), padx=(3, 3))

        self.open = Button(self, text="<", background='light grey',
                           command=lambda: pdf_viewer._prev_page())
        self.open.pack(side=RIGHT, pady=(5, 10), padx=(3, 3))

        self.run = Button(self, text="Run", background='light grey',
                          command=lambda: Discrept.discrept(editor, pdf_viewer))
        self.run.pack(side=RIGHT, pady=(5, 10), padx=(3, 3))

        text = "Workspace: " + Settings.MAIN.get('last_workspace')
        self.label1 = Label(self, background='light grey', text=text, font= "Verdana 16 underline bold")
        self.label1.pack(side=LEFT, pady=(5, 10))