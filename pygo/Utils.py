import os
from tkinter import *
from tkinter.font import Font

from colorsys import rgb_to_hls
from Config import config as cfg


class ResizeableCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        kwargs["highlightthickness"] = 0
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        wscale = event.width / self.width
        hscale = event.height / self.height
        self.width = event.width
        self.height = event.height
        self.config(width=self.width, height=self.height)
        self.scale(ALL, 0, 0, wscale, hscale)


class VerticalScrolledFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(
            self,
            bd=0,
            highlightthickness=0,
            yscrollcommand=vscrollbar.set,
            background=cfg.bg_color,
        )
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview, background=cfg.bg_color)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        self.interior = interior = Frame(canvas, background=cfg.bg_color)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind("<Configure>", _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind("<Configure>", _configure_canvas)


def hex_to_hls(hex):
    r, g, b = map(lambda x: int(x, 16) / 255, (hex[1:3], hex[3:5], hex[5:7]))
    return rgb_to_hls(r, g, b)


def get_rel_w(text_str, font_size, x_window_size, button=False):
    mult = 0.9
    if button:
        mult *= 1.25
    return ((len(text_str) * font_size / x_window_size)) * mult


def get_rel_h(font_size, y_window_size, button=False):
    mult = 1.8
    if button:
        mult *= 1.25
    return (font_size / y_window_size) * mult


def get_dim(dim_str):
    return int(dim_str.split("x")[0])


def create_font(font_str):

    size = None

    if font_str == "desc":
        size = cfg.desc_font_size
    elif font_str == "query":
        size = cfg.query_font_size
    elif font_str == "start":
        size = cfg.start_font_size
    elif font_str == "title":
        size = cfg.title_font_size
    elif font_str == "saved":
        size = cfg.saved_font_size

    return Font(family=cfg.font_family, size=size)


def create_home(x_size=cfg.home_button_size, y_size=cfg.home_button_size):
    return PhotoImage(file=cfg.home_icon)


def get_data_dir(subdir=""):
    dir = os.path.expanduser(r"~/.pygo/")
    if not os.path.exists(dir):
        os.mkdir(dir)
    if subdir:
        dir = os.path.join(dir, subdir)
        if not os.path.exists(dir):
            os.mkdir(dir)
    return dir
