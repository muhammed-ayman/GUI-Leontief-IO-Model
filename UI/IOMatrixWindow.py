from UI.AbstractFrame import AbstractFrame
from tkinter import *
from Matrix.IOMatrix import *
import config

class IOMatrixWindow(AbstractFrame):
    def __init__(self, master, appInstance, matrixDimension=0):
        self.master = master
        self.matrixDimension = matrixDimension
        self.appInstance = appInstance
        self.industriesLabels = appInstance.getIndustriesLabels()
        self.IOEntries = []
        self.IOInputs = []
        self.invalidInputLabel = None
        self.demandVectorState = IntVar()
        self.IOMatrixInstance = None
    
    def draw(self):
        # Setting the layout configuration
        cellWidth = 0.75*config.graphicsInfo['WIDTH']/self.matrixDimension
        cellHeight = 0.60*config.graphicsInfo['HEIGHT']/self.matrixDimension
        leftMargin = 0.20*config.graphicsInfo['WIDTH']
        upMargin = 0.2*config.graphicsInfo['HEIGHT']

        # Setting the title of the frame
        FrameTitle = Label(self.frame,
                            text="Enter The Input Output Matrix",
                            font=('Calibri', 15))
        FrameTitle.place(relx=0.5, y=upMargin/4, anchor=CENTER)

        # Setting the IO Matrix Entries
        for i in range(self.matrixDimension):
            industryLabelUp = Label(self.frame,
                                text=self.industriesLabels[i],
                                font=('Arial', 10), anchor=W)
            industryLabelBottom = Label(self.frame,
                                text=self.industriesLabels[i],
                                font=('Arial', 10))

            for j in range(self.matrixDimension):
                io_cell = Entry(self.frame)
                io_cell.insert(0,0)
                io_cell.place(x=leftMargin+j*(cellWidth),
                            y=upMargin+i*cellHeight, width=cellWidth/2, height=cellHeight/2)
                self.IOEntries.append(io_cell)

            industryLabelUp.place(x=leftMargin+i*(cellWidth),
                            y=0.6*upMargin,
                            width=cellWidth)
            industryLabelBottom.place(x=0,
                            y=upMargin+i*cellHeight,
                            width=leftMargin,
                            height=cellHeight/2)
        
        # Setting the Submission Button
        submissionButton = Button(self.frame,
                                    text="Proceed",
                                    command=self.checkIOInputs)
        submissionButton.place(relx=0.5,
                                    y=upMargin+10+self.matrixDimension*cellHeight,
                                    width=0.4*config.graphicsInfo['WIDTH'],
                                    height=50,
                                    anchor=CENTER)
        
        # Demand Vector Checkbutton
        self.demandCheckBox = Checkbutton(self.frame,
                                text="Demand Vector",
                                variable=self.demandVectorState)
        self.demandCheckBox.place(relx=0.5,
                                    y=upMargin+80+self.matrixDimension*cellHeight,
                                    anchor=CENTER)
    
    def checkIOInputs(self):
        self.IOInputs = []
        if self.invalidInputLabel:
            self.invalidInputLabel.destroy()
        localInputList = []
        counter = 1
        for i in range(self.matrixDimension*self.matrixDimension):
            try:
                floatConversion = float(self.IOEntries[i].get())
            except:
                self.invalidInputLabel = Label(self.frame,
                                text="Invalid IO Matrix",
                                font=('Arial', 10), anchor=W)
                self.invalidInputLabel.place(relx=0.5,
                                    y=0.9*config.graphicsInfo['HEIGHT'],
                                    anchor=CENTER)
                self.IOInputs = []
                return
            localInputList.append(float(self.IOEntries[i].get()))
            if i+1 == counter*self.matrixDimension:
                self.IOInputs.append(localInputList)
                localInputList = []
                counter += 1
        try:
            self.IOMatrixInstance = IOMatrix(self.IOInputs, self.matrixDimension, self.matrixDimension)
            if self.demandVectorState:
                self.proceedToDemandVectorInputWindow()
                return
            self.proceedToSolutionWindow()
        
        except Exception as e:
            if self.invalidInputLabel:
                self.invalidInputLabel.destroy()
            self.invalidInputLabel = Label(self.frame,
                                text=e,
                                font=('Arial', 10), anchor=W)
            self.invalidInputLabel.place(relx=0.5,
                                    y=0.9*config.graphicsInfo['HEIGHT'],
                                    anchor=CENTER)
        
    def proceedToDemandVectorInputWindow(self):
        self.clearFrame()
        self.appInstance.saveIOMatrix(self.IOMatrixInstance)
        self.appInstance.fireDemandVectorInputWindow()
    
    def proceedToSolutionWindow(self):
        self.clearFrame()
        self.appInstance.saveIOMatrix(self.IOMatrixInstance)
        self.appInstance.fireSolutionWindow()
    
    def __del__(self):
        print("IOMatrix Window Destructor Called!")