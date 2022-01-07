from AbstractFrame import AbstractFrame
from tkinter import *
from IndustriesInput import IndustriesInput

class MainWindow(AbstractFrame):
    def __init__(self, master, graphicsInfo):
        self.master = master
        self.graphicsInfo = graphicsInfo
        self.matrixDimension = 0
    
    def draw(self):
        self.matrix_dim_label1 = Label(self.frame, 
                                    text="Enter The IO Matrix Dimension",
                                    font=('Arial', 14))
        self.matrix_dim_label2 = Label(self.frame, 
                                    text="N =",
                                    font=('Arial', 14))
        self.matrix_dim_entry = Entry(self.frame)
        self.matrix_dim_btn = Button(self.frame,
                                    text="Proceed",
                                    command=self.proceedToAnalysisWindow)

        self.matrix_dim_entry.place(x=(self.graphicsInfo["HEIGHT"]/2)-50, 
                                    y = (self.graphicsInfo["WIDTH"]/2)-50,
                                    width=100,
                                    height=30)

        self.matrix_dim_label1.place(x=150,
                                    y=200)

        self.matrix_dim_label2.place(x=(self.graphicsInfo["HEIGHT"]/2)-100,
                                    y = (self.graphicsInfo["WIDTH"]/2)-50)

        self.matrix_dim_btn.place(x=(self.graphicsInfo["HEIGHT"]/2)-50,
                                y = (self.graphicsInfo["WIDTH"]/2),
                                height=30,
                                width=100)
    
    def get_matrix_dimension(self):
        return self.matrixDimension
    
    def proceedToAnalysisWindow(self):
        try:
            dim = int(self.matrix_dim_entry.get())
            self.matrixDimension = dim
            self.clearFrame()
            self.IndustriesInputObj = IndustriesInput(self.master, self.graphicsInfo, self.matrixDimension)
            self.IndustriesInputObj.initFrame()
            self.IndustriesInputObj.draw()
        except Exception as e:
            print(e)