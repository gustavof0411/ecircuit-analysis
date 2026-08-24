from util.current import Current
from util.node import Node
from util.voltage import Voltage

class Wire:
    def __init__(self, voltage: Voltage, current: Current) -> None:
        self.voltage = voltage
        self.current = current
        self.node1 = Node # leftmost or lowest node
        self.node2 = Node # rightmost or highest node