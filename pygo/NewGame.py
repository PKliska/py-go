from tkinter import *
from tkinter.colorchooser import askcolor

from Config import config as cfg
import Utils as tls

from Start import Start
from Play import Play


class PlayerSetupWidget(Frame):

    DEFAULT_COLORS = cfg.DEFAULT_COLORS

    class PlayerSettings(Frame):
        def __init__(self, parent, color):
            Frame.__init__(self, parent)
            self.parent = parent
            self.color = color
            self.name_entry = Entry(
                self,
                bg=cfg.bg_color,
                font=tls.crFont("query"),
                fg=cfg.fg_color,
                relief=cfg.relief,
            )
            self.name_entry.pack(fill=BOTH, expand=True, side=LEFT)
            self.color_button = Button(
                self,
                text=" ",
                font=tls.crFont("query"),
                bg=color,
                relief=cfg.relief,
                command=self.change_color,
            )
            self.color_button.pack(fill=Y, expand=False, side=LEFT)
            self.remove_button = Button(
                self,
                text="-",
                font=tls.crFont("query"),
                bg=cfg.bg_color,
                relief=cfg.relief,
                command=self.remove_player,
                state=DISABLED,
            )
            self.remove_button.pack(fill=Y, expand=False, side=LEFT)

        def remove_player(self):
            self.parent.remove_entry(self)

        def change_color(self):
            self.color = askcolor(self.color)[1]
            self.color_button.config(bg=self.color)

        def get_data(self):
            return (self.name_entry.get(), self.color)

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.entries = []
        self.add_player_button = Button(
            self,
            text="Add player",
            font=tls.crFont("query"),
            bg=cfg.bg_color,
            fg=cfg.fg_color,
            relief=cfg.relief,
            highlightthickness=cfg.border_thick,
            highlightbackground=cfg.border_color,
            command=self.add_entry,
        )
        self.add_player_button.pack(fill=X, side=TOP)
        self.add_entry()
        self.add_entry()

    def remove_entry(self, e):
        e.pack_forget()
        self.entries.remove(e)

        if (
            len(self.entries) < len(self.DEFAULT_COLORS)
            and not self.add_player_button.winfo_ismapped()
        ):
            self.add_player_button.pack(fill=X, side=TOP)

        if len(self.entries) == 2:
            for i in self.entries:
                i.remove_button.config(state=DISABLED)

    def add_entry(self):
        self.add_player_button.pack_forget()
        e = self.PlayerSettings(self, self.DEFAULT_COLORS[len(self.entries)])
        e.pack(fill=X, side=TOP)
        self.entries.append(e)
        if len(self.entries) < len(self.DEFAULT_COLORS):
            self.add_player_button.pack(fill=X, side=TOP)

        if len(self.entries) > 2:
            for i in self.entries:
                i.remove_button.config(state=NORMAL)

    def get_data(self):
        return [i.get_data() for i in self.entries]


class NewGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(background=cfg.bg_color)

        size_home = tls.getRelH(cfg.home_button_size, cfg.x_window_size, button=True)
        self.home = tls.crHome()

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

        name_entry_str = "Game name:"
        dimension_str = "Dimension:"

        relh_name_entry = tls.getRelH(cfg.start_font_size, cfg.y_window_size)
        relh_dimension = relh_name_entry
        relw_name_entry = tls.getRelW(
            name_entry_str, cfg.start_font_size, cfg.x_window_size
        )
        relw_dimension = tls.getRelW(
            dimension_str, cfg.start_font_size, cfg.x_window_size
        )

        game_query_labl = Label(
            self,
            text=name_entry_str,
            font=tls.crFont("start"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
        )
        game_query_labl.place(
            anchor="center",
            relheight=relh_name_entry,
            relwidth=relw_name_entry,
            relx=0.3,
            rely=0.2,
        )

        dimension_labl = Label(
            self,
            text=dimension_str,
            font=tls.crFont("start"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
            borderwidth=5,
        )
        dimension_labl.place(
            anchor="center",
            relheight=relh_dimension,
            relwidth=relw_dimension,
            relx=0.3,
            rely=0.28,
        )

        game_name_chars = 20
        relw_game_name = tls.getRelW(
            "-" * game_name_chars, cfg.start_font_size, cfg.x_window_size
        )

        self.game_name_entry = Entry(
            self,
            bg=cfg.bg_color,
            font=tls.crFont("start"),
            fg=cfg.fg_color,
            relief=cfg.relief,
        )
        self.game_name_entry.place(
            anchor="center",
            relheight=relh_name_entry,
            relwidth=relw_game_name,
            relx=0.57,
            rely=0.2,
        )

        dim_options = cfg.dim_options
        self.dim_select = StringVar(self)
        self.dim_select.set(dim_options[-1])

        relw_opt = tls.getRelW(dim_options[-1], cfg.start_font_size, cfg.x_window_size)
        relh_opt = relh_name_entry

        option_menu = OptionMenu(self, self.dim_select, *dim_options)
        option_menu.configure(
            activebackground=cfg.bg_color,
            activeforeground="black",
            background=cfg.bg_color,
            foreground=cfg.fg_color,
            font=tls.crFont("start"),
            disabledforeground=cfg.bg_color,
            highlightthickness=cfg.border_thin,
            relief=cfg.relief,
        )
        option_menu.place(
            anchor="center",
            relheight=relh_opt,
            relwidth=relw_opt * 1.5,
            relx=0.46,
            rely=0.28,
        )

        play_str = "Players:"
        relh_play_str = tls.getRelH(cfg.start_font_size, cfg.y_window_size)
        relw_play_str = tls.getRelW(play_str, cfg.start_font_size, cfg.x_window_size)

        play_title = Label(
            self,
            text=play_str,
            font=tls.crFont("start"),
            foreground=cfg.fg_color,
            background=cfg.bg_color,
        )
        play_title.place(
            anchor="s",
            relheight=relh_play_str,
            relwidth=relw_play_str,
            relx=0.5,
            rely=0.4,
        )

        self.players = PlayerSetupWidget(self)
        self.players.place(anchor="n", relx=0.5, rely=0.4)

        start_game_str = "Start game!"
        relh_start_str = tls.getRelH(
            cfg.start_font_size, cfg.y_window_size, button=True
        )
        relw_start_str = tls.getRelW(
            start_game_str, cfg.start_font_size, cfg.x_window_size
        )

        start_game_but = Button(
            self,
            text=start_game_str,
            font=tls.crFont("start"),
            activebackground="pale green",
            bg=cfg.bg_color,
            fg=cfg.fg_color,
            relief=cfg.relief,
            highlightthickness=cfg.border_thick,
            highlightbackground=cfg.border_color,
            command=lambda: self.switchToPlay(),
        )
        start_game_but.place(
            anchor="center",
            relheight=relh_start_str,
            relwidth=relw_start_str,
            relx=0.8,
            rely=0.9,
        )

    def switchToPlay(self):

        game_name = self.game_name_entry.get().strip()
        dimension = tls.getDim(self.dim_select.get())
        players = self.players.get_data()

        self.master.switch_to(Play, args=[self, game_name, dimension, players])
