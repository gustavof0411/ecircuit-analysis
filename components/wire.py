from components.terminal import Terminal
from util.current import Current
from util.node import Node
from util.voltage import Voltage
import itertools

class Wire:
    id_iter = itertools.count()
    def __init__(self) -> None:
        # Sets the wire's ID
        self.id = next(self.id_iter)
        #self.voltage = voltage
        #self.current = current
        self.startTerminal = Terminal(self.id, True)
        self.endTerminal = Terminal(self.id, False)

    def connectStartTerminal(self, node: Node, position: str):
        if (position == "r"):
            node.elementR = self.startTerminal
        elif (position == "t"):
            node.elementT = self.startTerminal
        elif (position == "l"):
            node.elementL = self.startTerminal
        elif (position == "b"):
            node.elementB = self.startTerminal
        else:
            print('error while connecting start terminal')

    def connectEndTerminal(self, node: Node, position: str):
        if (position == "r"):
            node.elementR = self.endTerminal
        elif (position == "t"):
            node.elementT = self.endTerminal
        elif (position == "l"):
            node.elementL = self.endTerminal
        elif (position == "b"):
            node.elementB = self.endTerminal
        else:
            print('error while connecting end terminal')

