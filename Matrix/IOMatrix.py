from Matrix.Matrix import *
from Matrix.Vector import Vector

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

class NonHSMatrix(Error):
    """Raised When The IO Matrix Doesn't Satisfy The HS Conditions"""
    def __init__(self, message="Matrix Doesn't Satisfy The HS Conditions."):
        self.message = message
        super().__init__(self.message)

# IO Matrix Class
class IOMatrix(Matrix):
    def __init__(self, matrix=[], n=0,m=0):
        super(IOMatrix, self).__init__(matrix,n,m)
        self.LeontifMatrix = None
        self.invertedLeontifMatrix = None
        self.validateIOMatrix()
        # self.validateHSConditions()
    
    def validateIOMatrix(self):
        # Checks Whether the IO Matrix is Square
        if not self.is_square():
            raise NotSquareIOMatrix
        # Checks Whether the IO Matrix is Realistic
        for row in range(self._rows_dim):
            for col in range(self._cols_dim):
                if self._matrix[row][col] >= 1 or self._matrix[row][col] < 0:
                    raise NonRealisticIOMatrix
        # Checks Whether the IO Matrix contains a Column of Zeros
        for col in range(self._cols_dim):
            valid_col = 0
            for row in range(self._rows_dim):
                if self._matrix[row][col] != 0:
                    valid_col = 1
                    break
            if not valid_col:
                raise NonRealisticIOMatrix("IO Matrix Can't Contain a Column of Zeros.")
    
    # Checks Whether The Matrix Satisfies The HS Conditions
    def validateHSConditions(self):
        identityMatrix = generateIdentityMatrix(self._rows_dim)
        self.LeontifMatrix = identityMatrix - self
        for i in range(self._rows_dim):
            if self.LeontifMatrix[i][i] <= 0:
                raise NonHSMatrix
        for i in range(1, self._rows_dim+1):
            if self.getPrincipalMinor(i, self.LeontifMatrix) <= 0:
                raise NonHSMatrix
        self.invertedLeontifMatrix = getInverse(self.LeontifMatrix)
    
    # Returns The Principal Minor at pMinorIndex Index
    def getPrincipalMinor(self, pMinorIndex, matrix):
        pMinorMatrix = [[matrix[i][j] for i in range(self._rows_dim) if (i+1 != pMinorIndex)] for j in range(self._rows_dim) if (j+1 != pMinorIndex)]
        pMatrix = Matrix(pMinorMatrix, self._rows_dim-1, self._rows_dim-1)
        pDet = getDeterminant(pMatrix)
        return pDet
    
    # Solve The System
    def getPLevelVector(self, demandVector: Vector) -> Vector:
        if self.validateDemandVector(demandVector):
            isDemandZero = (not any(demandVector))
            # Apply The HS Conditions in case Demand is Not The Zero Vector.
            if not isDemandZero:
                self.validateHSConditions()
                return self.invertedLeontifMatrix * demandVector
            # Solve The Homogenous System (I-A)x=0 otherwise.
            demandMatrix = np.array(demandVector.get_matrix())
            print(demandMatrix)

    # Checks Demand Vector Validity
    def validateDemandVector(self, demandVector: Vector) -> bool:
        for i in range(demandVector.get_rows_dimension()):
            if demandVector[i] < 0:
                return 0
        return 1