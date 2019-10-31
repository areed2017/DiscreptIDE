from tkinter import *

from discreptide.view.TextEditor import TextEditor


def copy_to_clipboard(text_editor: TextEditor):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text_editor.selection_get())
    r.update()
    r.destroy()


def cut_to_clipboard(text_editor: TextEditor):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text_editor.selection_get())
    r.update()
    r.destroy()
    text_editor.delete(SEL_FIRST, SEL_LAST)


def paste_from_clip_board(text_editor: TextEditor):
    r = Tk()
    r.withdraw()
    text_editor.insert(INSERT, r.clipboard_get())

