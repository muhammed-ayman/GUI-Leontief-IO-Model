from tkinter import *

class AbstractFrame():
    def __init__(self, master, graphicsInfo):
        self.master = master
            
    def draw(self):
        pass

    def initFrame(self):
        self.frame = Frame(self.master, width=self.graphicsInfo['HEIGHT'], height=self.graphicsInfo['WIDTH'])
        self.frame.pack()
    
    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()