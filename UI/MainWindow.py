from UI.AbstractFrame import AbstractFrame
from tkinter import *
import config

class MainWindow(AbstractFrame):
    def __init__(self, master, appInstance):
        self.appInstance = appInstance
        self.master = master
        self.matrixDimension = 0
    
    def draw(self):
        self.matrix_dim_label1 = Label(self.frame, 
                                    text="Enter The IO Matrix Dimension",
                                    font=('Arial', 14))
        self.matrix_dim_label2 = Label(self.frame, 
                                    text="N =",
                                    font=('Arial', 14))
        self.matrix_dim_entry = Entry(self.frame)
        self.matrix_dim_entry.insert(0, 3)
        self.matrix_dim_btn = Button(self.frame,
                                    text="Proceed",
                                    command=self.proceedToIndustriesInputWindow)

        self.matrix_dim_entry.place(x=(config.graphicsInfo["HEIGHT"]/2)-50, 
                                    y = (config.graphicsInfo["WIDTH"]/2)-50,
                                    width=100,
                                    height=30)

        self.matrix_dim_label1.place(x=150,
                                    y=200)

        self.matrix_dim_label2.place(x=(config.graphicsInfo["HEIGHT"]/2)-100,
                                    y = (config.graphicsInfo["WIDTH"]/2)-50)

        self.matrix_dim_btn.place(x=(config.graphicsInfo["HEIGHT"]/2)-50,
                                y = (config.graphicsInfo["WIDTH"]/2),
                                height=30,
                                width=100)
    
    def get_matrix_dimension(self):
        return self.matrixDimension
    
    def proceedToIndustriesInputWindow(self):
        try:
            dim = int(self.matrix_dim_entry.get())
            self.matrixDimension = dim
            self.clearFrame()
            self.appInstance.saveMatrixDimension(self.matrixDimension)
            self.appInstance.fireIndustriesInputWindow()
        except Exception as e:
            print(e)
    
    def __del__(self):
        print("Main Window Destructor Called!")