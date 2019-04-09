from tkinter import *

from Config import config as cfg
import Utils as tls


if __name__ == "__main__":

    root = Tk()
    root.geometry("{}x{}".format(cfg.x_window_size, cfg.y_window_size))
    root.resizable(cfg.resize_window_x, cfg.resize_window_y)
    root.configure(background=cfg.bg_color)
    root.title("Py-Go")

    title_str = "Py-Go"
    desc_str = "An N-player Go implementation in Python using TKinter"
    new_game_str = "New game"
    saved_games_str = "Saved games"

    relw_title = tls.getRelW(title_str, cfg.title_font_size, cfg.x_window_size)
    relw_desc = tls.getRelW(desc_str, cfg.desc_font_size, cfg.x_window_size)
    relw_new = tls.getRelW(
        new_game_str, cfg.start_font_size, cfg.x_window_size, button=True
    )
    relw_saved = tls.getRelW(
        saved_games_str, cfg.start_font_size, cfg.x_window_size, button=True
    )

    relh_title = tls.getRelH(cfg.title_font_size, cfg.y_window_size)
    relh_desc = tls.getRelH(cfg.desc_font_size, cfg.y_window_size)
    relh_new = tls.getRelH(cfg.start_font_size, cfg.y_window_size, button=True)
    relh_saved = tls.getRelH(cfg.start_font_size, cfg.y_window_size, button=True)

    title_labl = Label(
        root,
        text=title_str,
        font=tls.crFont("title"),
        foreground=cfg.fg_color,
        background=cfg.bg_color,
    )
    title_labl.place(
        anchor="center", relheight=relh_title, relwidth=relw_title, relx=0.5, rely=0.2
    )

    desc_labl = Label(
        root,
        text=desc_str,
        font=tls.crFont("desc"),
        foreground=cfg.fg_color,
        background=cfg.bg_color,
    )
    desc_labl.place(
        anchor="center", relheight=relh_desc, relwidth=relw_desc, relx=0.5, rely=0.35
    )

    new_game_but = Button(
        text=new_game_str,
        activebackground="pale green",
        bg=cfg.bg_color,
        font=tls.crFont("start"),
        fg=cfg.fg_color,
        relief=cfg.relief,
        highlightthickness=cfg.border_thick,
        highlightbackground=cfg.border_color,
    )
    new_game_but.place(
        anchor="center", relheight=relh_new, relwidth=relw_new, relx=0.75, rely=0.8
    )

    saved_games_but = Button(
        text=saved_games_str,
        activebackground="khaki",
        bg=cfg.bg_color,
        font=tls.crFont("start"),
        fg=cfg.fg_color,
        relief=cfg.relief,
        highlightthickness=cfg.border_thick,
        highlightbackground=cfg.border_color,
    )
    saved_games_but.place(
        anchor="center", relheight=relh_saved, relwidth=relw_saved, relx=0.25, rely=0.8
    )

    root.mainloop()
