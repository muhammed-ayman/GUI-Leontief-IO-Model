from Matrix.Matrix import *
from tkinter import *
from UI.UI import *

# Graphics Info
graphicsInfo = {
    'HEIGHT' : 600,
    'WIDTH' : 600
}

# Tkinter Initialization
root = Tk()
root.title("Leontif Input-Output Analysis")
root.geometry("{0}x{1}".format(graphicsInfo['WIDTH'], graphicsInfo['HEIGHT']))

if __name__ == '__main__':  
    app = App(root, graphicsInfo)
    app.execute()
    root.mainloop()