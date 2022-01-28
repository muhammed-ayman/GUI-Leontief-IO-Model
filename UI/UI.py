from UI.MainWindow import MainWindow
from UI.IndustriesInput import IndustriesInput
from UI.IOMatrixWindow import IOMatrixWindow
import config

class App:
    def __init__(self, master):
        self.industries = []
        self.InputOutputMatrix = 0
        self.DemandVector = 0
        self.ProductionLevelVector = 0
        self.MatrixDimension = 0
        self.MainWindowObj = MainWindow(master, self)
        self.master = master
    
    def execute(self):
        self.fireMainWindow()
    
    def saveIndustries(self, industriesList):
        if len(industriesList) != self.MatrixDimension:
            return
        self.industries = [industriesList[i] for i in range(len(industriesList))]
    
    def getIndustriesLabels(self):
        return self.industries
    
    def saveMatrixDimension(self, matrix_dimension):
        self.MatrixDimension = matrix_dimension
    
    def fireMainWindow(self):
        self.MainWindowObj.initFrame()
        self.MainWindowObj.draw()

    def fireIndustriesInputWindow(self):
        del self.MainWindowObj
        self.MainWindowObj = None
        self.IndustriesInputObj = IndustriesInput(self.master, self, matrixDimension=self.MatrixDimension)
        self.IndustriesInputObj.initFrame()
        self.IndustriesInputObj.draw()
    
    def fireIOMatrixInputWindow(self):
        del self.IndustriesInputObj
        self.IndustriesInputObj = None
        self.IOMatrixObj = IOMatrixWindow(self.master, self, matrixDimension=self.MatrixDimension)
        self.IOMatrixObj.initFrame()
        self.IOMatrixObj.draw()

    def __del__(self):
        print("App Destructor Called!")