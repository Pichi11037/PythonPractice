from Computer import Computer

class Order:

    order_counter = 0

    def __init__(self, computers:list): 
        Order.order_counter =+ 1
        self._id = Order.order_counter
        self._computerList = computers

    @property
    def id(self):
        return id
    
    @property
    def computerList(self):
        computer_str = ''
        for computer in self._computerList:
            computer_str += computer.__str__() + ' | '
        return computer_str
    
    @computerList.setter
    def computerList(self, computers:list): # type: ignore
        self._computerList = computers

    def __str__(self) -> str:
        return f'Order[id:{self._id}, Computers"{self.computerList}]'

    def addComputer(self, computer):
        self._computerList.append(computer)