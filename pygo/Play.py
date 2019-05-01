from tkinter import *
import traceback
import colorsys
import datetime
import uuid,os

from Config import config as cfg
import Utils as tls

from Start import Start
from Game import Game, saveGame
from Result import Result


class BoardWidget(Frame):
    def __init__(self, parent, game):
        Frame.__init__(self, parent)

        self.parent = parent
        self.game = game
        self.stone_location = {}

        dim = self.game.dimension
        self.canvas = tls.ResizeableCanvas(self, width=2 * dim, height=2 * dim)
        self.canvas.configure(background=cfg.board_color)

        # Create lines
        for i in range(1, 2 * dim, 2):
            self.canvas.create_line(1, i, 2 * dim - 1, i)
            self.canvas.create_line(i, 1, i, 2 * dim - 1)

        # Create stones
        def enter_stone(stone):
            def f(_):
                row, col = self.stone_location[stone]
                color = self.game.players[self.game.current_player]["color"]
                if self.game.board[row][col] is None:
                    self.canvas.itemconfig(stone, fill=color)

            return f

        def leave_stone(stone):
            def f(_):
                row, col = self.stone_location[stone]
                if self.game.board[row][col] is None:
                    self.canvas.itemconfig(stone, fill="")

            return f

        def place_stone(stone):
            def f(_):
                row, col = self.stone_location[stone]
                try:
                    self.game.play_stone(row, col)
                    self.update()
                except Exception as e:
                    traceback.print_exc(e)

            return f

        for i in range(dim):
            for j in range(dim):
                stone = self.canvas.create_oval(
                    2 * i, 2 * j, 2 * (i + 1), 2 * (j + 1), fill="", outline=""
                )
                self.canvas.tag_bind(stone, "<Enter>", enter_stone(stone))
                self.canvas.tag_bind(stone, "<Leave>", leave_stone(stone))
                self.canvas.tag_bind(stone, "<Button>", place_stone(stone))
                self.stone_location[stone] = (i, j)

        self.canvas.pack(fill=BOTH, expand=True)
        self.update()

    def update(self):
        for stone, (row, col) in self.stone_location.items():
            if self.game.board[row][col] is None:
                self.canvas.itemconfig(stone, fill="")
            else:
                color = self.game.players[self.game.board[row][col]]["color"]
                self.canvas.itemconfig(stone, fill=color)
        self.event_generate("<<MoveMade>>")


class Play(Frame):
    def __init__(self, master, game):
        Frame.__init__(self, master)

        self.configure(background=cfg.bg_color)

        self.game = game

        self.t_start = datetime.datetime.now()

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

        self.name_labl = Label(
            self,
            text="-",
            font=tls.create_font("start"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
        )
        self.name_labl.place(
            anchor="w",
            relheight=relh_name_str,
            relwidth=relw_name_str,
            relx=0.3,
            rely=0.05,
        )

        end_str = "Save & exit"
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
            command=lambda: self.end_and_save(),
        )
        end_but.place(
            anchor="center",
            relheight=relh_end_str,
            relwidth=relw_end_str,
            relx=0.85,
            rely=0.90,
        )

        pass_str = "Pass"
        self.passed = 0
        relh_pass_str = tls.get_rel_h(
            cfg.start_font_size, cfg.y_window_size, button=True
        )
        relw_pass_str = tls.get_rel_w(
            pass_str, cfg.start_font_size, cfg.x_window_size, button=True
        )
        pass_but = Button(
            self,
            text=pass_str,
            font=tls.create_font("start"),
            activebackground="light salmon",
            bg=cfg.bg_color,
            fg=cfg.fg_color,
            relief=cfg.relief,
            highlightthickness=cfg.border_thick,
            highlightbackground=cfg.border_color,
            command=lambda: self.pass_move(),
        )
        pass_but.place(
            anchor="center",
            relheight=relh_end_str,
            relwidth=relw_end_str,
            relx=0.15,
            rely=0.90,
        )


        self.board = BoardWidget(self, self.game)
        self.board.bind("<<MoveMade>>", self.update_labels)
        self.board.place(
            anchor="center", relx=0.5, rely=0.5, relwidth=0.7, relheight=0.7
        )
        self.update_labels()

    def update_labels(self, event=None):
        if event is not None:
            passed = 0
        current_player_name = self.game.players[self.game.current_player]["name"]
        current_player_color = self.game.players[self.game.current_player]["color"]
        lightness = tls.hex_to_hls(current_player_color)[1]
        if lightness > 0.5:
            text_color = "black"
        else:
            text_color = "white"
        self.name_labl.config(
            text=current_player_name,
            background=current_player_color,
            foreground=text_color,
        )

    def end_and_save(self):
        t_end = datetime.datetime.now()
        delta_t = t_end - self.t_start
        self.game.t_total += delta_t
        self.game.t_end = t_end

        if self.game.file is None:
            self.game.file = uuid.uuid4().hex + ".pickle"
        saveGame(self.game, os.path.join(tls.get_data_dir("saves"), self.game.file))
        self.master.switch_to(Start)

    def pass_move(self):
        self.passed += 1
        if self.passed == len(self.game.players):
            self.master.switch_to(Result, args = [self.game.players, self.game.score()])
        else:
            self.game.current_player = (self.game.current_player + 1) % len(self.game.players)
            self.update_labels()
