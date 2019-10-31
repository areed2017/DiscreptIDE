import re
from math import floor
from tkinter import Text, END, INSERT, GROOVE

from discreptide.model.Settings import Settings


class TextEditor(Text):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, undo=True, relief=GROOVE, borderwidth=2, *args, **kwargs)
        self.text_len = 0
        self.bind('<KeyRelease>', self.__update__)

        self.tag_configure('blue', foreground='blue')
        self.tag_configure('green', foreground='green')
        self.bind("<Tab>", self.tab)
        self.bind("<Return>", self.enter)

        Settings.MAIN.add_observer(self)
        self.refresh()

    def refresh(self):
        font = Settings.MAIN.get('font') + ' ' + str(Settings.MAIN.get('font_size'))
        self.configure(font=font)

    def tab(self, arg):
        self.insert(INSERT, " " * 4)
        return 'break'

    def enter(self, event):
        index = float(floor(float(self.index(INSERT))))
        last_line = self.get(index, END).splitlines()[0]
        tab_count = len(last_line.split(" " * 4)) - 1
        if '<' in last_line and '>' in last_line and '<new document>' not in last_line.lower():
            tab_count += 1
        self.insert(INSERT, "\n" + ((" " * 4) * tab_count))
        return 'break'

    def __applytag__(self, line, text):
        indexes = [(m.start(), m.end()) for m in re.finditer(r"<(.*?)>", text.lower())]
        for x in indexes:
            self.tag_add('blue', f'{line+1}.{x[0]}', f'{line+1}.{x[1]}')

        indexes = [(m.start(), m.end()) for m in re.finditer(r"\[(.*?)\]", text)]
        for x in indexes:
            self.tag_add('green', f'{line+1}.{x[0]}', f'{line+1}.{x[1]}')

    def __update__(self, event):
        if self.text_len == len(self.get_data()):
            return
        self.text_len = len(self.get_data())

        for tag in self.tag_names():
            self.tag_remove(tag, 1.0, END)

        lines = self.get('1.0', 'end-1c').split('\n')
        for i, line in enumerate(lines):
            self.__applytag__(i, line)

    def print_data(self, data):
        self.delete(0.0, END)
        self.insert(0.0, data)

    def get_data(self):
        return self.get(0.0, END)


