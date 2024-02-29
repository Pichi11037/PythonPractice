from InputDevice import InputDevice

class Keyboard(InputDevice):

    keyboard_counter = 0

    def __init__(self, inputType: str, brand: str) -> None:
        Keyboard.keyboard_counter += 1
        super().__init__(inputType, brand)
        self._id  = Keyboard.keyboard_counter

    def __str__(self) -> str:
        return f'Keyboard[id:{self._id}] | ' + super().__str__()
    


if __name__ == '__main__':
    keyboard = Keyboard('Keyboard', 'Logitech')
    print(keyboard)