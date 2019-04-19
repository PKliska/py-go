import pygame as pyg
from tkinter.font import Font
from PIL import Image, ImageTk

from Config import config as cfg


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


def remove_children(root):
    for child in root.winfo_children():
        child.destroy()


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
        Image.open(cfg.home_icon).resize(
            (x_size, y_size), Image.ANTIALIAS
        )
    )


def surf_tkimage(surface, width, height):
    image_str = pyg.image.tostring(surface, "RGB")
    w, h = surface.get_rect()[2:]
    image = Image.frombytes("RGB", (w, h), image_str).resize((width, height))
    return ImageTk.PhotoImage(image)
