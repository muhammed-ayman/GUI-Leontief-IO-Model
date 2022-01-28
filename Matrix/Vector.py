from Matrix import *

# Exceptions
class InvalidVectorError(Error):
    """Raised When The Vector Is Invalid"""
    def __init__(self, message="Invalid Vector"):
        self.message = message
        super().__init__(self.message)

class IncompatibleVector(Error):
    """Raised When The Vector Dimensions Is Invalid"""
    def __init__(self, message="Incompatible Vector Dimensions"):
        self.message = message
        super().__init__(self.message)

class Vector(Matrix):
    def __init__(self,vectorList, rows=1,cols=0):
        self.__vector = vectorList
        self.__rows = rows
        self.__cols = cols
        try:
            self.validateVector()
        except Exception as e:
            self.__del__()
            raise e
        super(Vector, self).__init__([vectorList],rows,cols)
    
    def validateVector(self):
        # Checks Whether The Matrix is Valid
        if not isinstance(self.__vector, list):
            raise InvalidVectorError
        if not isinstance(self.__vector[0], (float,int)):
            raise InvalidVectorError
        
        # Checks Dimensions Compatibility
        if self.__rows != 1 or len(self.__vector) != self.__cols:
            raise IncompatibleVector
    
    def __del__(self):
        print("The Vector Has Been Deleted!")

v = Vector([1,2,3],1,3)