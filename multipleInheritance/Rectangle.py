from Color import Color
from GeometricFigure import GeometricFigure

class Rectangle(GeometricFigure, Color):
    
    def __init__(self, length: float, height: float, r:float, g:float, b:float) -> None:
        GeometricFigure.__init__(self, length, height)
        Color.__init__(self, r, g, b)

    def getArea(self):
        return self.length*self.height

    def __str__(self) -> str:
        return f'Rectangle = [Length:{self.length}, Height:{self.height}, Area:{self.getArea()}]'