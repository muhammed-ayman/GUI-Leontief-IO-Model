from UI.MainWindow import MainWindow
from UI.IndustriesInput import IndustriesInput

class App:
    def __init__(self, master, graphicsInfo):
        self.industries = []
        self.InputOutputMatrix = 0
        self.DemandVector = 0
        self.ProductionLevelVector = 0
        self.MatrixDimension = 0
        self.MainWindowObj = MainWindow(master, graphicsInfo, self)
        self.master = master
        self.graphicsInfo = graphicsInfo
    
    def execute(self):
        self.MainWindowObj.initFrame()
        self.MainWindowObj.draw()
    
    def saveIndustries(self, industriesList):
        if len(industriesList) != self.MatrixDimension:
            return
        self.industries = [industriesList[i] for i in range(len(industriesList))]
    
    def saveMatrixDimension(self, matrix_dimension):
        self.MatrixDimension = matrix_dimension
    

    def fireIndustriesInputWindow(self):
        del self.MainWindowObj
        self.MainWindowObj = None
        self.IndustriesInputObj = IndustriesInput(self.master, self.graphicsInfo, self, matrixDimension=self.MatrixDimension)
        self.IndustriesInputObj.initFrame()
        self.IndustriesInputObj.draw()
    
    def fireIOMatrixInputWindow(self):
        del self.IndustriesInputObj
        self.IndustriesInputObj = None

    def __del__(self):
        print("App Destructor Called!")