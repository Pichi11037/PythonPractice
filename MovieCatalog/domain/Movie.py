class Movie():
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def __str__(self) -> str:
        return f'Movie[Name:{self._name}]'