from tkinter.filedialog import *

from discreptide.view.CommandBar import CommandBar
from discreptide.view.Menu import MenuBar
from discreptide.view.TextEditor import TextEditor
from discreptide.view.TreeView import TreeView

def open_workspace():
    Tk().withdraw()
    directory = askdirectory()
    if directory == '':
        quit(1)
    Tk().destroy()
    Window(directory)


class Window(Tk):

    def __init__(self, workspace_folder):
        super().__init__()
        self.workspace_folder = workspace_folder
        self.title("Discrept Editor's Settings")

        self.tree = None
        self.frame = None

        self.build_view()

        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mainloop()

    def build_view(self):
        exterior_frame = Frame(self)
        frame = Frame(exterior_frame)

        # Widgets
        self.editor = TextEditor(frame)
        self.command_bar = CommandBar(exterior_frame, self.editor)
        self.tree = TreeView(frame, self.editor)

        # Window Configuration
        frame.columnconfigure(3, weight=1)
        frame.rowconfigure(0, weight=1)

        # Widget Locations
        self.tree.grid(column=0, row=0, columnspan=1, sticky=('N', 'E', 'S', 'W'))
        self.editor.grid(column=1, row=0, columnspan=3, sticky=('N', 'E', 'S', 'W'))

        self.command_bar.grid(column=0, row=0, rowspan=1, sticky=('N', 'E', 'S', 'W'))
        frame.grid(column=0, row=1, rowspan=3, sticky=('N', 'E', 'S', 'W'))

        exterior_frame.columnconfigure(0, weight=1)
        exterior_frame.rowconfigure(2, weight=1)
        exterior_frame.pack(expand=True, fill=BOTH, padx=(10,10))

    @staticmethod
    def on_closing():
        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #     self.destroy()
        quit(0)



