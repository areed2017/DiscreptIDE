from os import walk
from tkinter.ttk import Treeview

from discreptide import Settings
from discreptide.control import FileTools
from discreptide.view.TextEditor import TextEditor

ACCEPTED_FILE_EXT = ['.dis', '.png', '.jpg', '.gif', '.sub']


class TreeView(Treeview):

    def __init__(self, parent, editor: TextEditor):
        super().__init__(parent, show="tree")
        self.editor = editor
        self.__update__()

    def refresh(self):
        self.load_workspace(Settings.MAIN.get('last_workspace'))

    def load_workspace(self, dir, head=None):
        def print_(url: str):
            return url.split('/')[-1]

        if head is None:
            id_ = self.insert('', 0, text=print_(dir))
            self.tag_bind('ttk', '<Double-1>', self.item_clicked)
            head = id_
        else:
            id_ = self.insert(head, 'end', text=print_(dir))

        for (dir_path, sub_dirs, file_names) in walk(dir):
            for sub_dir in sub_dirs:
                self.load_workspace(dir_path + '/' + sub_dir, id_)
            for file in file_names:
                if file[-4:].lower() in ACCEPTED_FILE_EXT:
                    value=dir_path + '/' + file
                    self.insert(id_, 'end', value=value.replace(' ', '$$$$'), text=print_(file), tags=('ttk', 'simple'))
            break

    def __update__(self):
        for item in self.get_children():
            self.delete(item)
        self.load_workspace(Settings.MAIN.get('last_workspace'))

    def item_clicked(self, event):
        item = self.selection()[0]
        file = self.item(item, "value")[0]
        FileTools.open_file(file.replace('$$$$', ' '), self.editor)
