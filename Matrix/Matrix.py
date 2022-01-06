class Matrix:
    # n = number of rows, m = number of columns
    def __init__(self,matrix=[],n=0,m=0):
        self.matrix = matrix
        if not self.validate_matrix(matrix, n, m):
            print("Invalid Matrix!")
            self.__del__()
    
    def get_row(self, index):
        try:
            return self.matrix[index]
        except:
            return "Invalid Index!"
    
    def get_column(self, index):
        try:
            column = []
            for row in range(0, len(self.matrix)):
                column.append(row[index])
            return column
        except:
            return "Invalid Index!"

    def get_matrix(self):
        return self.matrix

    def validate_matrix(self, matrix, n, m):
        rows_num = len(self.matrix)
        if not (n > 0 and m > 0):
            return
        if rows_num != n:
            return 0
        for row in range(rows_num):
            if len(self.matrix[row]) != m:
                return 0
        return 1
    
    def get_rows_dimension(self):
        return len(self.matrix)
    
    def get_columns_dimension(self):
        return len(self.matrix[0])
    
    # Overloading the + operator to work for matrices
    def __add__(self, SecondMatrix):
        if not (self.get_rows_dimension() == SecondMatrix.get_rows_dimension() and self.get_columns_dimension() == SecondMatrix.get_columns_dimension()):
            print("Invalid Matrices Dimensions")
            return
        resultList = []
        for row in range(self.get_rows_dimension()):
            rowList = []
            for column in range(self.get_columns_dimension()):
                rowList.append(self.matrix[row][column] + SecondMatrix[row][column])
            resultList.append(rowList)
        resultMatrix = Matrix(resultList, len(resultList), len(resultList[0]))
        
        return resultMatrix

    def __getitem__(self, index):
        try:
            return self.matrix[index]
        except:
            print("Invalid Element Position!")

    def __del__(self):
        print("The Matrix Has Been Deleted!")