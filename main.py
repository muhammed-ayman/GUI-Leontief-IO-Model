from Matrix.Matrix import *
from tkinter import *
from UI.UI import *
import config

# Tkinter Initialization
root = Tk()
root.title("Leontif Input-Output Analysis")
root.geometry("{0}x{1}".format(config.graphicsInfo['WIDTH'], config.graphicsInfo['HEIGHT']))

if __name__ == '__main__':  
    app = App(root)
    app.execute()
    root.mainloop()