import tkinter
from tkinter.filedialog import asksaveasfilename

from discreptide.model import set_file, get_file
from discreptide.view.TextEditor import TextEditor
from discreptide.view.TreeView import TreeView


def open_file(file_name:str, text_editor: TextEditor):
    set_file(file_name)
    with open(file_name) as file:
        text_editor.print_data(file.read().replace('\t', '    '))
    text_editor.__update__(None)


def new_file(text_editor: TextEditor, file_tree: TreeView):
    file_name = asksaveasfilename()
    if file_name == '':
        return
    text_editor.delete(0.0, tkinter.END)
    set_file(file_name)
    save_file(text_editor)
    file_tree.__update__()


def save_file(text_editor: TextEditor):
    text = text_editor.get_data()
    file_name = get_file()
    with open(file_name, 'w') as file:
        file.write(text)
    return True


def save_file_as(text_editor: TextEditor):
    file_name = asksaveasfilename(defaultextension=".dis")
    set_file(file_name)
    save_file(text_editor)


def auto_save(text_editor: TextEditor):
    pass