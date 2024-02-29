from Monitor import Monitor
from Keyboard import Keyboard
from Mouse import Mouse

class Computer:
    computer_counter = 0
    def __init__(self, name:str, monitor:Monitor, keyboard:Keyboard, mouse:Mouse) -> None:
        
        Computer.computer_counter += 1

        self._id = Computer.computer_counter
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def monitor(self):
        return self.monitor
    
    @monitor.setter
    def monitor(self, monitor:Monitor):
        self.monitor = monitor
    
    @property
    def keyboard(self):
        return self.keyboard
    
    @keyboard.setter
    def keyboard(self, keyboard:Keyboard):
        self.keyboard = keyboard
    
    @property
    def mouse(self):
        return self.mouse
    
    @mouse.setter
    def mouse(self, mouse:Mouse):
        self.mouse = mouse

    def __str__(self) -> str:
        return f'Computer[id:{self._id}, name:{self._name}] |' + self._monitor.__str__() + ' | ' + self._keyboard.__str__() + ' | ' + self._mouse.__str__()

if __name__ == '__main__':
    keyboard = Keyboard('Keyboard', 'Logitech')
    # print(keyboard)
    monitor = Monitor('Logitech', 'Medium')
    # print(monitor)
    mouse = Mouse('Mouse', 'Samsung')
    # print(mouse)

    computer = Computer('test-cpu', monitor, keyboard, mouse)
    print(computer)