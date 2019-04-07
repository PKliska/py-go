from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

from Config import config as cfg
import Start

if __name__ == '__main__':

	root = Tk()

	im = Image.open(cfg.home_icon)
	ph = ImageTk.PhotoImage(im.resize((40, 40), Image.ANTIALIAS))

	relh_home = relw_home = Start.getRelH(40, cfg.x_window_size, but=True)

	root.geometry('{}x{}'.format(cfg.x_window_size, cfg.y_window_size))
	root.resizable(cfg.resize_window_x, cfg.resize_window_y)
	root.configure(background=cfg.bg_color)
	root.title('Py-Go')

	home_button = Button(image=ph, activebackground='light salmon', bg=cfg.bg_color, fg='black', relief='flat', highlightthickness=5, highlightbackground='black')
	home_button.place(anchor='center', relheight=relh_home/1.5, relwidth=relw_home/1.5, relx=0.05, rely=0.05)

	game_query_str = 'Game name:'
	dimension_str = 'Dimension:'

	query_font = Font(family=cfg.font_family, size=20)

	relh_query = Start.getRelH(20, cfg.y_window_size)
	relw_query_str = Start.getRelW(game_query_str, 20, cfg.x_window_size)
	relw_dim_str = Start.getRelW(dimension_str, 20, cfg.x_window_size)

	game_query_lab = Label(root, text=game_query_str, font=query_font, anchor='center', foreground='black', background=cfg.bg_color)
	game_query_lab.place(anchor='center', relheight=relh_query, relwidth=relw_query_str, relx=0.3, rely=0.2)

	dimension_lab = Label(root, text=dimension_str, font=query_font, anchor='center', foreground='black', background=cfg.bg_color)
	dimension_lab.place(anchor='center', relheight=relh_query, relwidth=relw_dim_str, relx=0.3, rely=0.28)

	n_chars_name = 20
	relw_game_name = Start.getRelW('a'*n_chars_name, 20, cfg.x_window_size)

	game_name_entry = Entry(root, bg = cfg.bg_color, font=query_font, fg='black', relief='flat')
	game_name_entry.place(anchor='center', relheight=relh_query, relwidth=relw_game_name, relx=0.57, rely=0.2)

	dim_options = ['9x9', '13x13', '17x17', '19x19']
	dim_select = StringVar(root)
	dim_select.set(dim_options[-1])

	relw_opt = Start.getRelW(dim_options[-1], 20, cfg.x_window_size)

	option_menu = OptionMenu(root, dim_select, *dim_options)
	option_menu.configure(activebackground=cfg.bg_color, activeforeground='black')
	option_menu.configure(anchor='center')
	option_menu.configure(background=cfg.bg_color, foreground='black')
	option_menu.configure(font=query_font)
	option_menu.configure(disabledforeground=cfg.bg_color)
	option_menu.configure(highlightthickness=1)
	option_menu.configure(relief='flat')
	option_menu.place(anchor='center', relheight=relh_query, relwidth=relw_opt*1.5, relx=0.46, rely=0.28)

	start_game_str = 'Start game!'
	relh_start_str = Start.getRelH(20, cfg.y_window_size, but=True)
	relw_start_str = Start.getRelW(start_game_str, 20, cfg.x_window_size)

	start_game_but = Button(text=start_game_str, font=query_font, activebackground='pale green', bg=cfg.bg_color, fg='black', relief='flat', highlightthickness=5, highlightbackground='black')
	start_game_but.place(anchor='center', relheight=relh_start_str, relwidth=relw_start_str, relx=0.8, rely=0.9)

	root.mainloop()