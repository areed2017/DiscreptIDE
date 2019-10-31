from tkinter.filedialog import *

from discreptide.control import FileTools
from discreptide.model.Settings import Settings
from discreptide.view.CommandBar import CommandBar
from discreptide.view.MenuBar import MenuBar
from discreptide.view.TextEditor import TextEditor
from discreptide.view.TreeView import TreeView
from discreptide.view.pdf_viewer import PDFViewer

WINDOW = None


def open_workspace():
    global WINDOW
    if WINDOW is not None:
        WINDOW.destroy()
    Tk().withdraw()
    directory = askdirectory()
    if directory == '':
        directory = Settings.MAIN.get('last_workspace')
    Tk().destroy()
    Settings.MAIN.set('last_workspace', directory)
    Settings.MAIN.save()
    WINDOW = Window(directory)


def open_last_workspace():
    global WINDOW
    if WINDOW is not None:
        WINDOW.destroy()
    Tk().withdraw()
    directory = Settings.MAIN.get('last_workspace')
    Tk().destroy()
    WINDOW = Window(directory)


class Window(Tk):

    def __init__(self, workspace_folder):
        super().__init__()
        self.workspace_folder = workspace_folder
        self.title("Discrept Editor")

        self.tree = None
        self.editor = None
        self.command_bar = None
        self.viewer = None

        self.build_view()
        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar, background='grey')

        self.key_binding()
        self.mainloop()

    def key_binding(self):
        top = self.winfo_toplevel()

        top.bind('<Control-s>', lambda: FileTools.save_file(self.editor))
        top.bind('<Command-s>', lambda: FileTools.save_file(self.editor))

        top.bind('<Control-Shift-s>', lambda: FileTools.save_file_as(self.editor))
        top.bind('<Command-Shift-s>', lambda: FileTools.save_file_as(self.editor))

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def build_view(self):
        exterior_frame = Frame(self, background='light grey')
        frame = Frame(exterior_frame, background='light grey')

        # Widgets
        self.editor = TextEditor(frame)
        self.viewer = PDFViewer(frame)
        self.command_bar = CommandBar(exterior_frame, self.editor, self.viewer)
        self.tree = TreeView(frame, self.editor)

        # Window Configuration
        frame.columnconfigure(3, weight=1)
        frame.rowconfigure(0, weight=1)

        # Widget Locations
        self.tree.grid(column=0, row=0, columnspan=1, sticky=('N', 'E', 'S', 'W'), pady=(5, 5))
        self.editor.grid(column=1, row=0, columnspan=3, sticky=('N', 'E', 'S', 'W'), padx=(5, 0), pady=(5, 5))
        self.viewer.grid(column=4, row=0, columnspan=1, sticky=('N', 'E', 'S', 'W'), padx=(5, 0), pady=(5, 5))

        self.command_bar.grid(column=0, row=0, rowspan=1, sticky=('N', 'E', 'S', 'W'))
        frame.grid(column=0, row=1, rowspan=3, sticky=('N', 'E', 'S', 'W'))

        exterior_frame.columnconfigure(0, weight=1)
        exterior_frame.rowconfigure(3, weight=1)
        exterior_frame.pack(expand=True, fill=BOTH, padx=(10,10))

    def on_closing(self):
        self.destroy()
        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #     self.destroy()
        quit(0)
