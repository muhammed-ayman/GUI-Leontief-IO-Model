from UI.AbstractFrame import AbstractFrame
from tkinter import *

class IndustriesInput(AbstractFrame):
    def __init__(self, master, appInstance, matrixDimension=0):
        self.master = master
        self.matrixDimension = matrixDimension
        self.appInstance = appInstance
    
    def draw(self):
        FrameTitle = Label(self.frame, 
                            text="Enter The Industries/Goods Names",
                            font=('Calibri', 15))
        FrameTitle.place(x=150,
                        y = 20)

        self.industries = []
        self.industries_labels = []
        self.industries_entries = []
        
        for i in range(self.matrixDimension):
            industryLabel = Label(self.frame, 
                                text="Industry/Good {0}".format(str(i+1)),
                                font=('Arial', 12))
            self.industries_labels.append(industryLabel)

            industryEntry = Entry(self.frame)
            self.industries_entries.append(industryEntry)

            self.industries_labels[i].place(x=150, 
                                    y = 20+50*(i+1))
            self.industries_entries[i].place(x=280, 
                                    y = 20+50*(i+1),
                                    width=170,
                                    height=30)

        industries_submission_btn = Button(self.frame,
                                    text="Proceed",
                                    command=self.proceedToDemandVectorInputWindow)

        industries_submission_btn.place(x=150,
                                y = 20+50*(self.matrixDimension+1),
                                height=40,
                                width=300)
    
    def proceedToDemandVectorInputWindow(self):
        try:
            self.industries = []
            for i in range(self.matrixDimension):
                self.industries.append(self.industries_entries[i].get())

            self.clearFrame()
            self.appInstance.saveIndustries(self.industries)
            self.appInstance.fireIOMatrixInputWindow()
        
        except Exception as e:
            self.industries = []
            print(e)
    
    def __del__(self):
        print("IndustriesInput Window Destructor Called!")