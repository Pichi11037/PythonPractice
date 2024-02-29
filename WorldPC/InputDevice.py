class InputDevice:

    def __init__(self, inputType:str, brand:str) -> None:
        self.__inputType = inputType
        self.__brand = brand
    
    @property
    def inputType(self):
        return self.inputType
    
    @inputType.setter
    def inputType(self, inputType):
        self.__inputType = inputType

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    def __str__(self) -> str:
        return f'Input Device[Input Type:{self.__inputType}, Brand: {self.__brand}]'