class Color:

    def __init__(self, red:float, green:float, blue:float) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, red:float):
        self._red = red

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, blue:float):
        self._blue = blue    

    @property
    def green(self):
        return self._green    

    @green.setter
    def red(self, green:float):
        self._green = green