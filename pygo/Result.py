from tkinter import *

from Config import config as cfg
import Utils as tls

class Result(Frame):

    def __init__(self, master, players, scores):
        Frame.__init__(self, master)

        self.configure(background=cfg.bg_color)

        for i in range(len(players)):
            players[i]["score"] = scores[i]

        players.sort(key=lambda x: x["score"], reverse=True)

        for i in players:
            f = Frame(self, bg=i["color"])
            lightness = tls.hex_to_hls(i["color"])[1]
            if lightness<0.5:
                fg = "white"
            else:
                fg = "black"
            l = Label(f, text = i["name"] + " " + str(i["score"]), bg=i["color"], foreground=fg)
            l.pack(fill=BOTH, expand=True)
            f.pack(fill=BOTH, expand=True)
