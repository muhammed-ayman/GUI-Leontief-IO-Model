from AbstractFrame import AbstractFrame
from tkinter import *

class IndustriesInput(AbstractFrame):
    def __init__(self, master, graphicsInfo, matrixDimension=0):
        self.master = master
        self.graphicsInfo = graphicsInfo
        self.matrixDimension = matrixDimension
    
    def draw(self):
        FrameTitle = Label(self.frame, 
                            text="Enter The Industries/Goods Names",
                            font=('Calibri', 15))
        FrameTitle.place(x=150,
                        y = 20)

        self.industries = []
        industries_labels = []
        industries_entries = []
        
        for i in range(self.matrixDimension):
            industryLabel = Label(self.frame, 
                                text="Industry {0}".format(str(i+1)),
                                font=('Arial', 12))
            industries_labels.append(industryLabel)
        
        for i in range(self.matrixDimension):
            industryEntry = Entry(self.frame)
            industries_entries.append(industryEntry)
        
        industries_submission_btn = Button(self.frame,
                                    text="Proceed",
                                    command=self.proceedToAnalysisWindow)
        
        for i in range(self.matrixDimension):
            industries_labels[i].place(x=150, 
                                    y = 20+50*(i+1))
            industries_entries[i].place(x=250, 
                                    y = 20+50*(i+1),
                                    width=200,
                                    height=30)

        industries_submission_btn.place(x=150,
                                y = 20+50*(self.matrixDimension+1),
                                height=40,
                                width=300)
    
    def proceedToAnalysisWindow(self):
        print(self.frame.winfo_children())