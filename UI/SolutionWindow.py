from UI.AbstractFrame import AbstractFrame
from tkinter import *
from Matrix.IOMatrix import *
import config

class SolutionWindow(AbstractFrame):
    def __init__(self, master, appInstance):
        self.master = master
        self.appInstance = appInstance
        self.pLevelVector = self.appInstance.getPLevelVector()
        self.pVectorSpace = self.appInstance.getPVectorSpace()
    
    def draw(self):
        # Setting the layout configuration
        upMargin = 0.2*config.graphicsInfo['HEIGHT']

        title = "The Solution Vector"
        if self.pVectorSpace:
            title = "The Solution Space"

        # Setting the title of the frame
        FrameTitle = Label(self.frame,
                            text=title,
                            font=('Calibri', 15))
        FrameTitle.place(relx=0.5, y=upMargin/4, anchor=CENTER)

        if self.pLevelVector:
            solutionDim = self.pLevelVector.get_rows_dimension()
            solutionCellHeight = 0.7*config.graphicsInfo['HEIGHT']/solutionDim
            canvas = Canvas(self.frame,
                            width=0.2*config.graphicsInfo['WIDTH'],
                            height=solutionCellHeight*solutionDim)
            canvas.place(relx=0.5,
                        rely=0.5,
                        anchor=CENTER)
            # Left Matrix Boundary
            canvas.create_line(20,5,
                            20,solutionCellHeight*solutionDim-solutionCellHeight/2,
                            fill="#000")
            canvas.create_line(20,5,25,5,fill="#000")
            canvas.create_line(20,solutionCellHeight*solutionDim-solutionCellHeight/2,
                            25,solutionCellHeight*solutionDim-solutionCellHeight/2,
                            fill="#000")
            # Right Matrix Boundary
            canvas.create_line(0.2*config.graphicsInfo['WIDTH']-20,5,
                            0.2*config.graphicsInfo['WIDTH']-20,solutionCellHeight*solutionDim-solutionCellHeight/2,
                            fill="#000")
            canvas.create_line(0.2*config.graphicsInfo['WIDTH']-20,5,
                            0.2*config.graphicsInfo['WIDTH']-25,5,
                            fill="#000")
            canvas.create_line(0.2*config.graphicsInfo['WIDTH']-20,solutionCellHeight*solutionDim-solutionCellHeight/2,
                            0.2*config.graphicsInfo['WIDTH']-25,solutionCellHeight*solutionDim-solutionCellHeight/2,
                            fill="#000")

            for i in range(solutionDim):
                solutionLabel = Label(self.frame,
                            text=round(self.pLevelVector[i][0],3),
                            font=('Calibri', 11),
                            anchor=CENTER)
                solutionLabel.place(relx=0.5,
                            y = upMargin + i*solutionCellHeight,
                            height=solutionCellHeight/2,
                            anchor=CENTER)


    
    def __del__(self):
        print("Solution Window Destructor Called!")