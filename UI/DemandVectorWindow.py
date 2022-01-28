from UI.AbstractFrame import AbstractFrame
from tkinter import *
from Matrix.IOMatrix import *
from Matrix.Vector import *
import config

class DemandVectorWindow(AbstractFrame):
    def __init__(self, master, appInstance, matrixDimension=0):
        self.master = master
        self.matrixDimension = matrixDimension
        self.appInstance = appInstance
        self.industriesLabels = appInstance.getIndustriesLabels()
        self.DemandVectorEntries = []
        self.DemandVectorInputs = []
        self.invalidInputLabel = None
        self.pLevelVector = None
        self.nullSpaceBasis = None
        self.IOMatrixInstance = appInstance.getIOMatrixInstance()
    
    def draw(self):
        # Setting the layout configuration
        cellWidth = 0.75*config.graphicsInfo['WIDTH']/self.matrixDimension
        cellHeight = 0.60*config.graphicsInfo['HEIGHT']/self.matrixDimension
        labelWidth = 0.50*config.graphicsInfo['WIDTH']
        upMargin = 0.2*config.graphicsInfo['HEIGHT']

        # Setting the title of the frame
        FrameTitle = Label(self.frame,
                            text="Enter The Demand Vector",
                            font=('Calibri', 15))
        FrameTitle.place(relx=0.5, y=upMargin/4, anchor=CENTER)

        # Setting the Demand Vector Entries
        for i in range(self.matrixDimension):
            demandLabel = Label(self.frame,
                                text=self.industriesLabels[i],
                                font=('Arial', 10), anchor=CENTER)

            demand_cell = Entry(self.frame)
            demand_cell.insert(0,0)
            demand_cell.place(relx=0.5,
                            y=upMargin+i*cellHeight, width=cellWidth/2, height=cellHeight/2)
            self.DemandVectorEntries.append(demand_cell)

            demandLabel.place(x=0,
                            y=upMargin+i*cellHeight,
                            width=labelWidth,
                            height=cellHeight/2)
        
        # Setting the Submission Button
        submissionButton = Button(self.frame,
                                    text="Proceed",
                                    command=self.checkDemandInputs)
        submissionButton.place(relx=0.5,
                                    y=upMargin+10+self.matrixDimension*cellHeight,
                                    width=0.4*config.graphicsInfo['WIDTH'],
                                    height=50,
                                    anchor=CENTER)
        
    
    def checkDemandInputs(self):
        self.DemandVectorInputs = []
        if self.invalidInputLabel:
            self.invalidInputLabel.destroy()
        for i in range(self.matrixDimension):
            try:
                floatConversion = float(self.DemandVectorEntries[i].get())
            except:
                self.invalidInputLabel = Label(self.frame,
                                text="Invalid Vector",
                                font=('Arial', 10), anchor=W)
                self.invalidInputLabel.place(relx=0.5,
                                    y=0.9*config.graphicsInfo['HEIGHT'],
                                    anchor=CENTER)
                self.DemandVectorInputs = []
                return
            self.DemandVectorInputs.append(float(self.DemandVectorEntries[i].get()))
        try:
            dVector = Vector(self.DemandVectorInputs, 1, self.matrixDimension)
            self.pLevelVector = self.IOMatrixInstance.getPLevelVector(dVector)
            if self.pLevelVector:
                self.proceedToSolutionWindow()
                return
            self.nullSpaceBasis = self.IOMatrixInstance.null_space_basis.get_matrix()    
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
        
    def proceedToSolutionWindow(self):
        self.clearFrame()
        if self.pLevelVector:
            self.appInstance.savePLevelVector(self.pLevelVector)
        if self.nullSpaceBasis:
            self.appInstance.savePVectorNullSpace(self.nullSpaceBasis)
        self.appInstance.fireSolutionWindow()
    
    def __del__(self):
        print("DemandVector Window Destructor Called!")