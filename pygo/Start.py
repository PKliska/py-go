from tkinter import *

from Config import config as cfg
import Utils as tls


class Start(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(background=cfg.bg_color)

        from NewGame import NewGame
        from SavedGames import SavedGames

        title_str = "Py-Go"
        desc_str = "An N-player Go implementation in Python using TKinter"
        new_game_str = "New game"
        saved_games_str = "Load game"

        relw_title = tls.get_rel_w(title_str, cfg.title_font_size, cfg.x_window_size)
        relw_desc = tls.get_rel_w(desc_str, cfg.desc_font_size, cfg.x_window_size)
        relw_new = tls.get_rel_w(
            new_game_str, cfg.start_font_size, cfg.x_window_size, button=True
        )
        relw_saved = tls.get_rel_w(
            saved_games_str, cfg.start_font_size, cfg.x_window_size, button=True
        )

        relh_title = tls.get_rel_h(cfg.title_font_size, cfg.y_window_size)
        relh_desc = tls.get_rel_h(cfg.desc_font_size, cfg.y_window_size)
        relh_new = tls.get_rel_h(cfg.start_font_size, cfg.y_window_size, button=True)
        relh_saved = tls.get_rel_h(cfg.start_font_size, cfg.y_window_size, button=True)
        title_labl = Label(
            self,
            text=title_str,
            font=tls.create_font("title"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
        )
        title_labl.place(
            anchor="center",
            relheight=relh_title,
            relwidth=relw_title,
            relx=0.5,
            rely=0.2,
        )

        desc_labl = Label(
            self,
            text=desc_str,
            font=tls.create_font("desc"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
        )
        desc_labl.place(
            anchor="center",
            relheight=relh_desc,
            relwidth=relw_desc,
            relx=0.5,
            rely=0.35,
        )

        new_game_but = Button(
            self,
            text=new_game_str,
            activebackground="pale green",
            bg=cfg.bg_color,
            font=tls.create_font("start"),
            fg=cfg.fg_color,
            relief=cfg.relief,
            highlightthickness=cfg.border_thick,
            highlightbackground=cfg.border_color,
            command=lambda: self.master.switch_to(NewGame),
        )
        new_game_but.place(
            anchor="center", relheight=relh_new, relwidth=relw_new, relx=0.75, rely=0.8
        )

        saved_games_but = Button(
            self,
            text=saved_games_str,
            activebackground="khaki",
            bg=cfg.bg_color,
            font=tls.create_font("start"),
            fg=cfg.fg_color,
            relief=cfg.relief,
            highlightthickness=cfg.border_thick,
            highlightbackground=cfg.border_color,
            command=lambda: self.master.switch_to(SavedGames),
        )
        saved_games_but.place(
            anchor="center",
            relheight=relh_saved,
            relwidth=relw_saved,
            relx=0.25,
            rely=0.8,
        )
