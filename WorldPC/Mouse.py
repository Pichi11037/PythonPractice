from InputDevice import InputDevice

class Mouse(InputDevice):

    mouse_counter = 0

    def __init__(self, inputType: str, brand: str) -> None:
        Mouse.mouse_counter += 1
        super().__init__(inputType, brand)
        self._id  = Mouse.mouse_counter

    def __str__(self) -> str:
        return f'Mouse[id:{self._id}] | ' + super().__str__()
    


if __name__ == '__main__':
    mouse = Mouse('mouse', 'logitech')
    print(mouse)