from tkinter import *
from tkinter.font import Font

from Config import config as cfg


def getRelW(text, pts, window, but=False):
	mult = 0.9
	if but:
		mult *= 1.25
	return ((len(text) * pts / window))*mult

def getRelH(pts, window, but=False):
	mult = 1.8
	if but:
		mult *= 1.25
	return (pts /  window)*mult

def removeChildren(root):
	for child in root.winfo_children():
		child.destroy()

if __name__ == '__main__':

	root = Tk()

	root.geometry('{}x{}'.format(cfg.x_window_size, cfg.y_window_size))
	root.resizable(cfg.resize_window_x, cfg.resize_window_y)
	root.configure(background=cfg.bg_color)
	root.title('Py-Go')

	testing = False

	game_name_font = Font(family=cfg.font_family, size=70)
	desc_font = Font(family=cfg.font_family, size=12)
	but_font = Font(family=cfg.font_family, size=20)

	game_str = 'Py-Go'
	desc_str = 'An N-player Go implementation in Python using TKinter'
	new_game_str = 'New game'
	saved_games_str = 'Saved games'

	relw_game_name = getRelW(game_str, 70, cfg.x_window_size)
	relw_desc = getRelW(desc_str, 12, cfg.x_window_size)
	relw_new = getRelW(new_game_str, 20, cfg.x_window_size, but=True)
	relw_saved = getRelW(saved_games_str, 20, cfg.x_window_size, but=True)

	relh_game_name = getRelH(70, cfg.y_window_size)
	relh_desc = getRelH(12, cfg.y_window_size)
	relh_new = getRelH(20, cfg.y_window_size, but=True)
	relh_saved = getRelH(20, cfg.y_window_size, but=True)

	game_name = Label(root, text=game_str, font=game_name_font, anchor='center', foreground='black', background=cfg.bg_color)
	game_name.place(anchor='center', relheight=relh_game_name, relwidth=relw_game_name, relx=0.5, rely=0.2)

	desc = Label(root, text=desc_str, font=desc_font, anchor='center', foreground='black', background=cfg.bg_color)
	desc.place(anchor='center', relheight=relh_desc, relwidth=relw_desc, relx=0.5, rely=0.35)

	new_game_but = Button(text=new_game_str, activebackground='pale green', bg=cfg.bg_color, font=but_font, fg='black', relief='flat', highlightthickness=5, highlightbackground='black')
	new_game_but.place(anchor='center', relheight=relh_new, relwidth=relw_new, relx=0.75, rely=0.8)

	saved_games_but = Button(text=saved_games_str, activebackground='khaki', bg=cfg.bg_color, font=but_font, fg='black', relief='flat', highlightthickness=5, highlightbackground='black', command=lambda: removeChildren(root))
	saved_games_but.place(anchor='center', relheight=relh_saved, relwidth=relw_saved, relx=0.25, rely=0.8)

	root.mainloop()