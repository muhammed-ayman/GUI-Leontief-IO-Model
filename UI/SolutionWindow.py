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

        # # Setting the IO Matrix Entries
        # for i in range(self.matrixDimension):
        #     industryLabelUp = Label(self.frame,
        #                         text=self.industriesLabels[i],
        #                         font=('Arial', 10), anchor=W)
        #     industryLabelBottom = Label(self.frame,
        #                         text=self.industriesLabels[i],
        #                         font=('Arial', 10))

        #     for j in range(self.matrixDimension):
        #         io_cell = Entry(self.frame)
        #         io_cell.insert(0,0)
        #         io_cell.place(x=leftMargin+j*(cellWidth),
        #                     y=upMargin+i*cellHeight, width=cellWidth/2, height=cellHeight/2)
        #         self.IOEntries.append(io_cell)

        #     industryLabelUp.place(x=leftMargin+i*(cellWidth),
        #                     y=0.6*upMargin,
        #                     width=cellWidth)
        #     industryLabelBottom.place(x=0,
        #                     y=upMargin+i*cellHeight,
        #                     width=leftMargin,
        #                     height=cellHeight/2)
        
        # # Setting the Submission Button
        # submissionButton = Button(self.frame,
        #                             text="Proceed",
        #                             command=self.checkIOInputs)
        # submissionButton.place(relx=0.5,
        #                             y=upMargin+10+self.matrixDimension*cellHeight,
        #                             width=0.4*config.graphicsInfo['WIDTH'],
        #                             height=50,
        #                             anchor=CENTER)
        
        # # Demand Vector Checkbutton
        # self.demandCheckBox = Checkbutton(self.frame,
        #                         text="Demand Vector",
        #                         variable=self.demandVectorState)
        # self.demandCheckBox.place(relx=0.5,
        #                             y=upMargin+80+self.matrixDimension*cellHeight,
        #                             anchor=CENTER)
    
    def __del__(self):
        print("Solution Window Destructor Called!")