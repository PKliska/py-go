from tkinter import *

from Start import Start

class Controller(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.current_activity = Start(self)
        self.current_activity.pack(fill=BOTH, expand=True)

    def switch_to(self, activity, args=None):
        self.current_activity.pack_forget()
        self.current_activity.destroy()
        if args is None:
            self.current_activity = activity(self)
        else:
            self.current_activity = activity(self, *args)
        self.current_activity.pack(fill=BOTH, expand=True)
