from tkinter import Tk

from discreptide.view.pdf_viewer.pdfviewer import PDFViewer


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.title("Discrept Viewer")
        self.viewer = PDFViewer()
        self.viewer._open_file()
        self.mainloop()


if __name__ == '__main__':
    Window()