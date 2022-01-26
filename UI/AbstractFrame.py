from tkinter import *
import config

class AbstractFrame():
    def __init__(self, master):
        self.master = master
            
    def draw(self):
        pass

    def initFrame(self):
        self.frame = Frame(self.master, width=config.graphicsInfo['HEIGHT'], height=config.graphicsInfo['WIDTH'])
        self.frame.pack()
    
    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()