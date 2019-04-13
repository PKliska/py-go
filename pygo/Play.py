from tkinter import *

from Config import config as cfg
from PIL import ImageTk
import Utils as tls
import Draw as draw

from Game import Game


class Board(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.but_mat = [[None] * self.parent.dimension for i in range(self.parent.dimension)]
        self.but_size = self._get_button_size()

        for i in range(self.parent.dimension):
            self.parent.grid_rowconfigure(i, minsize=self.but_size)
            self.parent.grid_columnconfigure(i, minsize=self.but_size)


        for i in range(self.parent.dimension):
            for j in range(self.parent.dimension):
                surf = draw.empty_middle()
                but_image = tls.surf_tkimage(surf, self.but_size, self.but_size)
                but_image = ImageTk.PhotoImage(but_image)
                but = Button(self, image=but_image, height=self.but_size, width=self.but_size)
                but.grid(row=i, column=j)
                self.but_mat[i][j] = but


    def _get_button_size(self):
        return int(round((cfg.x_window_size*0.7)/self.parent.dimension))

    def _angle(self, i, j):
        n = self.parent.dimension - 1
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
        self.board.place(anchor='center', relx=0.5, rely=0.5, relwidth=0.7, relheight=0.7)
