from tkinter import Tk, BOTH
from Controller import Controller
from Config import config as cfg


if __name__ == "__main__":
    root = Tk()
    root.geometry("{}x{}".format(cfg.x_window_size, cfg.y_window_size))
    root.resizable(cfg.resize_window_x, cfg.resize_window_y)
    root.title("Py-Go")
    Controller(root).pack(fill=BOTH, expand=True)
    root.mainloop()
