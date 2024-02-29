from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse
from Computer import Computer
from Order import Order

keyboard1 = Keyboard('Keyboard', 'Logitech')
# print(keyboard)
monitor1 = Monitor('Logitech', 'Medium')
# print(monitor)
mouse1 = Mouse('Mouse', 'Samsung')
# print(mouse)
computer1 = Computer('test-cpu', monitor1, keyboard1, mouse1)

keyboard2 = Keyboard('Keyboard', 'Logitech')
# print(keyboard)
monitor2 = Monitor('Logitech', 'Medium')
# print(monitor)
mouse2 = Mouse('Mouse', 'Samsung')
# print(mouse)
computer2 = Computer('test-cpu', monitor1, keyboard1, mouse1)

computers = [computer1, computer2]

order = Order(computers)

print(order)

keyboard3 = Keyboard('Keyboard', 'Logitech')
# print(keyboard)
monitor3 = Monitor('Logitech', 'Medium')
# print(monitor)
mouse3 = Mouse('Mouse', 'Samsung')
# print(mouse)
computer3 = Computer('test-cpu', monitor1, keyboard1, mouse1)

order.addComputer(computer3)


# test