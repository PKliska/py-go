from tkinter import *

from Config import config as cfg
import Utils as tls

from Game import Game


class Board(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

    def _angle(self, i, j):
        n = parent.dimension - 1
        angle = 0

        if i != 0 and j == 0:
            angle = 90
        elif i == n and 0 < j < n:
            angle = 180
        elif j == n:
            angle = 270

        return angle


class Play(Frame):
    def __init__(self, master, new_game, game_name, dimension, players):
        Frame.__init__(self, master)

        self.configure(background=cfg.bg_color)

        self.game_name = game_name
        self.dimension = dimension
        self.players = players
        self.n_players = len(self.players)

        self.game = Game(self.dimension, self.n_players)

        # from Start import Start

        playing_str = "Playing:"
        relw_playing_str = tls.get_rel_w(
            playing_str, cfg.start_font_size, cfg.x_window_size
        )
        relh_playing_str = tls.get_rel_h(cfg.start_font_size, cfg.y_window_size)
        playing_labl = Label(
            self,
            text=playing_str,
            font=tls.create_font("start"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
        )
        playing_labl.place(
            anchor="center",
            relheight=relh_playing_str,
            relwidth=relw_playing_str,
            relx=0.2,
            rely=0.05,
        )

        sample_name_str = "-" * 20
        relh_name_str = relh_playing_str
        relw_name_str = tls.get_rel_w(
            sample_name_str, cfg.start_font_size, cfg.x_window_size
        )
        self.name_str = "-"
        self.name_labl = Label(
            self,
            text=self.name_str,
            font=tls.create_font("start"),
            foreground=cfg.fg_color,
            background="red",
        )
        self.name_labl.place(
            anchor="w",
            relheight=relh_name_str,
            relwidth=relw_name_str,
            relx=0.3,
            rely=0.05,
        )

        end_str = "End game"
        relh_end_str = tls.get_rel_h(
            cfg.start_font_size, cfg.y_window_size, button=True
        )
        relw_end_str = tls.get_rel_w(
            end_str, cfg.start_font_size, cfg.x_window_size, button=True
        )
        end_but = Button(
            self,
            text=end_str,
            font=tls.create_font("start"),
            activebackground="light salmon",
            bg=cfg.bg_color,
            fg=cfg.fg_color,
            relief=cfg.relief,
            highlightthickness=cfg.border_thick,
            highlightbackground=cfg.border_color,
        )
        end_but.place(
            anchor="center",
            relheight=relh_end_str,
            relwidth=relw_end_str,
            relx=0.85,
            rely=0.90,
        )

        self.board = Board(self)
