from tkinter import *
from tkinter.filedialog import askdirectory

from discreptide.control import ClipBoard, Discrept, FileTools


class MenuBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.build_file_menu()
        self.build_edit_menu()
        self.build_run_menu()

    def build_file_menu(self):
        from discreptide.view.Window import open_workspace
        file_menu = Menu(self)

        file_menu.add_command(
            label="New",
            command=lambda:  FileTools.new_file(self.master.editor, self.master.tree)
        )

        file_menu.add_command(
            label="Open",
            command=lambda: FileTools.open_file(askdirectory(), self.master.editor)
        )

        file_menu.add_command(
            label="Work Space",
            command=lambda: open_workspace()
        )

        file_menu.add_command(
            label="Save",
            command=lambda: FileTools.save_file(self.master.editor)
        )

        file_menu.add_command(
            label="Save as",
            command=lambda: FileTools.save_file_as(self.master.editor)
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Settings",
            command=lambda: print("Settings")
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Print",
            command=lambda: print("Print")
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Exit",
            command=lambda: quit()
        )

        self.add_cascade(label='File', menu=file_menu)

    def build_edit_menu(self):
        edit_menu = Menu(self)

        edit_menu.add_command(
            label="Undo",
            accelerator="Ctrl+Z",
            command=lambda: self.master.editor.edit_undo()
        )

        edit_menu.add_command(
            label="Redo",
            accelerator="Ctrl+Shift+Z",
            command=lambda: self.master.editor.edit_redo()
        )

        edit_menu.add_separator()

        edit_menu.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            command=lambda: ClipBoard.cut_to_clipboard(self.master.editor)
        )

        edit_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=lambda: ClipBoard.copy_to_clipboard(self.master.editor)
        )

        edit_menu.add_command(
            label="Paste",
            accelerator="Ctrl+P",
            command=lambda: ClipBoard.paste_from_clip_board(self.master.editor)
        )

        self.add_cascade(label='Edit', menu=edit_menu)

    def build_run_menu(self):
        run_menu = Menu(self)

        run_menu.add_command(
            label="Run as Discrept File",
            command=lambda: Discrept.discrept(self.master.editor, self.master.viewer)
        )

        run_menu.add_command(
            label="Run as Subscrept File",
            command=lambda: print("Run as Subscrept File")
        )

        self.add_cascade(label='Run', menu=run_menu)
