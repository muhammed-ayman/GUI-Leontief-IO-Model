from Matrix import *

# Exceptions
class Error(Exception):
    """Base Class For All Exceptions"""
    pass

class NotSquareIOMatrix(Error):
    """Raised When The IO Matrix Is Not Square"""
    def __init__(self, message="IO Matrix Should Be Square."):
        self.message = message
        super().__init__(self.message)

class NonRealisticIOMatrix(Error):
    """Raised When The IO Matrix Is Not Realistic"""
    def __init__(self, message="IO Matrix Should Neither Include Values >= 1 Nor Values < 0."):
        self.message = message
        super().__init__(self.message)

# IO Matrix Class
class IOMatrix(Matrix):
    def __init__(self, matrix=[], n=0,m=0):
        super(IOMatrix, self).__init__(matrix,n,m)
        self.validateIOMatrix()
    
    def validateIOMatrix(self):
        # Checks Whether the IO Matrix is Square
        if not self.is_square():
            raise NotSquareIOMatrix
        # Checks whether the IO Matrix is Realistic
        for row in range(self._rows_dim):
            for col in range(self._cols_dim):
                if self.matrix[row][col] >= 1:
                    raise NonRealisticIOMatrix
try:
    m = IOMatrix([1,2,3], 1, 1)
except Exception as e:
    print(e)