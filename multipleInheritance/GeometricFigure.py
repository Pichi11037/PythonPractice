from abc import ABC, abstractclassmethod

class GeometricFigure(ABC):

    staticvar = 'this is a static variable'

    def __init__(self, length:float, height:float) -> None:
        self._length = length
        self._height = height

    @property
    def length(self):
        return self._length
    
    @property
    def height(self):
        return self._height
        
    @length.setter
    def length(self, length:float):
        self._length = length
    
    @height.setter
    def height(self, height:float):
        self._height = height

    def __str__(self) -> str:
        return f'Geometric Figure=[Length: {self.length}, Height:{self.height}]'
    
    @abstractclassmethod
    def getArea(self):
        pass

    @staticmethod
    def staticMethod():
        return GeometricFigure.staticvar
    
    @classmethod
    def classMethod(cls):
        return cls.staticvar