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

    def __del__(self):
        print("The Matrix Has Been Deleted!")