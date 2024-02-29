from Color import Color
from GeometricFigure import GeometricFigure

class Square(GeometricFigure, Color):
    def __init__(self, length, r, g, b) -> None:
        GeometricFigure.__init__(self, length, length)
        Color.__init__(self, r, g, b)

    def getArea(self):
        return self.length*self.height
    
    def __str__(self) -> str:
        return f'Square = [Length:{self.length}, Height:{self.height}, Area:{self.getArea()}]'
    