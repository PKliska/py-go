from tkinter import ttk
from tkinter import Tk
from tkinter.ttk import Label
from tkinter.font import Font

from Config import config as cfg

root = Tk()

root.geometry('{}x{}'.format(cfg.x_window_size, cfg.y_window_size))
root.resizable(cfg.resize_window_x, cfg.resize_window_y)
root.configure(background=cfg.bg_color)
root.title('Py-Go')

def getFontSize(font):
	return font.actual()['size']

def getRelW(text, font, window):
	return ((len(text) * getFontSize(font) / window))*0.9

def getRelH(font, window):
	return (getFontSize(font) /  window)*1.8

testing = False

style = ttk.Style()
style.configure('BW.TLabel', foreground='black', background=cfg.bg_color)
style.configure('GAME.TLabel', foreground='black', background='blue' if testing else cfg.bg_color)
style.configure('DESC.TLabel', foreground='black', background='red' if testing else cfg.bg_color)

game_name_font = Font(family=cfg.font_family, size=70)
desc_font = Font(family=cfg.font_family, size=12)

game_str = 'Py-Go'
desc_str = 'An N-player Go implementation in Python using TKinter'

relw_game_name = getRelW(game_str, game_name_font, cfg.x_window_size)
relw_desc = getRelW(desc_str, desc_font, cfg.x_window_size)

relh_game_name = getRelH(game_name_font, cfg.x_window_size)
relh_desc = getRelH(desc_font, cfg.x_window_size)

game_name = Label(root, text=game_str, font=game_name_font, style='GAME.TLabel', anchor='center')
game_name.place(anchor='center', relheight=relh_game_name, relwidth=relw_game_name, relx=0.5, rely=0.2)

desc = Label(root, text=desc_str, font=desc_font, style='DESC.TLabel', anchor='center')
desc.place(anchor='center', relheight=relh_desc, relwidth=relw_desc, relx=0.5, rely=0.35)

root.mainloop()