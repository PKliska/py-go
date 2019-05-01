from tkinter import *
import os

from Config import config as cfg
import Utils as tls

from Start import Start
from Play import Play
from Game import Game, loadGame


class SavedGames(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(background=cfg.bg_color)

        size_home = tls.get_rel_h(cfg.home_button_size, cfg.x_window_size, button=True)
        self.home = tls.create_home()

        home_button = Button(
            self,
            image=self.home,
            activebackground="light salmon",
            bg=cfg.bg_color,
            fg=cfg.fg_color,
            relief=cfg.relief,
            highlightthickness=cfg.border_thick,
            highlightbackground=cfg.border_color,
            command=lambda: self.master.switch_to(Start),
        )
        home_button.place(
            anchor="center",
            relheight=size_home / 1.5,
            relwidth=size_home / 1.5,
            relx=0.05,
            rely=0.05,
        )

        saved_games_str = "Saved games"

        relw_saved = tls.get_rel_w(
            saved_games_str, cfg.saved_font_size, cfg.x_window_size, button=False
        )
        relh_saved = tls.get_rel_h(cfg.saved_font_size, cfg.y_window_size, button=False)

        saved_labl = Label(
            self,
            text=saved_games_str,
            font=tls.create_font("saved"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
        )
        saved_labl.place(
            anchor="center",
            relheight=relh_saved,
            relwidth=relw_saved,
            relx=0.5,
            rely=0.1,
        )
        games = []
        for i in os.listdir(tls.get_data_dir("saves")):
            games.append(loadGame(os.path.join(tls.get_data_dir("saves"), i)))
        games.sort(key = lambda x: x.t_end, reverse=True)

        saved_games = tls.VerticalScrolledFrame(self)
        for game in games:
            switch = lambda e: self.master.switch_to(Play, args=[game])
            f = Frame(saved_games.interior)
            for s in game.game_strs():
                l = Label(f, text=s)
                l.pack()
                l.bind("<Button-1>", switch)
            f.pack()
            f.bind("<Button-1>", switch)
        saved_games.place(relx=0.5, rely=0.5, relwidth=0.3)
