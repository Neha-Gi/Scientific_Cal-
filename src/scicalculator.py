import math

class SciCalculator:


    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)
    
    def square(self,x):
        return math.pow(x,2)

    