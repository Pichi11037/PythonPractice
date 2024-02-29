class Monitor():

    monitor_counter = 0

    def __init__(self, brand: str, size: str) -> None:
        Monitor.monitor_counter += 1
        self._id = Monitor.monitor_counter
        self._brand  = brand
        self._size = size

    def __str__(self) -> str:
        return f'Monitor[id:{self._id}, Brand:{self._brand}, Size:{self._size}]'

if __name__ == '__main__':
    monitor = Monitor('Logitech', 'Medium')
    print(monitor)