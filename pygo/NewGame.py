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

	query_font = Font(family=cfg.font_family, size=15)

	relh_query = Start.getRelH(15, cfg.y_window_size)
	relw_query_str = Start.getRelW(game_query_str, 15, cfg.x_window_size)
	relw_dim_str = Start.getRelW(dimension_str, 15, cfg.x_window_size)

	game_query_lab = Label(root, text=game_query_str, font=query_font, anchor='center', foreground='black', background=cfg.bg_color)
	game_query_lab.place(anchor='center', relheight=relh_query, relwidth=relw_query_str, relx=0.2, rely=0.2)

	dimension_lab = Label(root, text=dimension_str, font=query_font, anchor='center', foreground='black', background=cfg.bg_color)
	dimension_lab.place(anchor='center', relheight=relh_query, relwidth=relw_dim_str, relx=0.2, rely=0.3)


	root.mainloop()