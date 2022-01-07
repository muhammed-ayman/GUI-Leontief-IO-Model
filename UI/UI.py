from tkinter import *
from AbstractFrame import AbstractFrame
from MainWindow import MainWindow
from IndustriesInput import IndustriesInput

# Graphics Info
graphicsInfo = {
    'HEIGHT' : 600,
    'WIDTH' : 600
}

# Tkinter Initialization
root = Tk()
root.title("Leontif Input-Output Analysis")
root.geometry("{0}x{1}".format(graphicsInfo['WIDTH'], graphicsInfo['HEIGHT']))

class App:
    def __init__(self, master, graphicsInfo):
        self.MainWindowObj = MainWindow(master, graphicsInfo)
    
    def execute(self):
        self.MainWindowObj.initFrame()
        self.MainWindowObj.draw()

app = App(root, graphicsInfo)
app.execute()

root.mainloop()