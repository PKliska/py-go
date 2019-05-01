import pygame as pyg
from tkinter import Canvas, ALL
from tkinter.font import Font
from PIL import Image, ImageTk

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

    return Font(family=cfg.font_family, size=size)


def create_home(x_size=cfg.home_button_size, y_size=cfg.home_button_size):
    return ImageTk.PhotoImage(
        Image.open(cfg.home_icon).resize((x_size, y_size), Image.ANTIALIAS)
    )
