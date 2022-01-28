from UI.MainWindow import MainWindow
from UI.IndustriesInput import IndustriesInput
from UI.IOMatrixWindow import IOMatrixWindow
from Matrix.IOMatrix import IOMatrix
import config

class App:
    def __init__(self, master):
        self.industries = []
        self.InputOutputMatrix = 0
        self.DemandVector = 0
        self.ProductionLevelVector = 0
        self.MatrixDimension = 0
        self.IOMatrixObj = 0
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
    
    def saveIOMatrix(self, IOMatrixObj: IOMatrix):
        self.IOMatrixObj = IOMatrixObj
        print(self.IOMatrixObj.get_matrix())
        pass
    
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
        self.IOMatrixWindowObj = IOMatrixWindow(self.master, self, matrixDimension=self.MatrixDimension)
        self.IOMatrixWindowObj.initFrame()
        self.IOMatrixWindowObj.draw()
    
    def fireDemandVectorInputWindow(self):
        del self.IOMatrixObj
        self.IOMatrixObj = None
        pass

    def fireSolutionWindow(self):
        if self.IOMatrixObj:
            del self.IOMatrixObj
        pass

    def __del__(self):
        print("App Destructor Called!")