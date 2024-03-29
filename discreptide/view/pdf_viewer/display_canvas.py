from tkinter import *

from PIL import ImageTk


class DisplayCanvas(Frame):

    def __init__(self, master, page_height, page_width, **kw):
        Frame.__init__(self, master, **kw)
        self.x = self.y = 0

        self.canvas = Canvas(self, height=page_height, width=page_width, bg='#404040', highlightbackground='#353535')
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

        top = self.winfo_toplevel()
        self.bind('<Left>', self.on_left)
        self.bind('<Right>', self.on_right)
        self.bind('<Up>', self.on_up)
        self.bind('<Down>', self.on_down)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)

        self.rect = None
        self.image = None
        self.image_obj = None
        self.pil_image = None
        self.draw = False

        self.start_x = None
        self.start_y = None

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        if event.state == 'Shift':
            if event.delta < 0:
                self.on_left()
            else:
                self.on_right()
        else:
            if event.delta < 0:
                self.on_down()
            else:
                self.on_up()

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if not self.rect and self.draw:
            self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

    def on_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if event.x > 0.9*w:
            self.on_right()
        elif event.x < 0.1*w:
            self.on_left()
        if event.y > 0.9*h:
            self.on_down()
        elif event.y < 0.1*h:
            self.on_up()

        if self.draw:
            self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_left(self, event=None):
        self.canvas.xview_scroll(-1, 'units')

    def on_right(self, event=None):
        self.canvas.xview_scroll(1, 'units')

    def on_up(self, event=None):
        self.canvas.yview_scroll(-1, 'units')

    def on_down(self, event=None):
        self.canvas.yview_scroll(1, 'units')

    def on_button_release(self, event):
        pass

    def update_image(self, image):
        self.pil_image = image
        self.image = ImageTk.PhotoImage(image, master=self.canvas)
        if self.image_obj is None:
            self.image_obj = self.canvas.create_image(0, 0, image=self.image, anchor=CENTER)
        else:
            self.canvas.itemconfig(self.image_obj, image=self.image)

        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.canvas.xview_moveto(0.0)
        self.canvas.yview_moveto(0.0)

    def reset(self):
        self.canvas.delete("all")
        self.image_obj = self.canvas.create_image(0, 1, image=self.image)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.rect = None

    def clear(self):
        self.canvas.delete("all")
        self.image_obj = None

    def get_rect(self):
        w, h = self.pil_image.size
        x0, y0 = self.canvas.coords(self.image_obj)
        minx = x0 - w/2.0
        miny = y0 - h/2.0
        if self.rect:
            rect = self.canvas.coords(self.rect)
            rect = [rect[0] + abs(minx), rect[1] + abs(miny), rect[2] + abs(minx), rect[3] + abs(miny)]
            return rect
        else:
            return None
