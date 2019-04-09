from tkinter.font import Font
from PIL import Image, ImageTk

from Config import config as cfg


def getRelW(text_str, font_size, x_window_size, button=False):
    mult = 0.9
    if button:
        mult *= 1.25
    return ((len(text_str) * font_size / x_window_size)) * mult


def getRelH(font_size, y_window_size, button=False):
    mult = 1.8
    if button:
        mult *= 1.25
    return (font_size / y_window_size) * mult


def removeChildren(root):
    for child in root.winfo_children():
        child.destroy()


def crFont(font_str):

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


def crHome():
    return ImageTk.PhotoImage(
        Image.open(cfg.home_icon).resize(
            (cfg.home_button_size, cfg.home_button_size), Image.ANTIALIAS
        )
    )
