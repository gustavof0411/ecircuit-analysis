from components.terminal import Terminal
from util.current import Current
from util.node import Node
from util.voltage import Voltage

class Wire:
    wireList = {}
    currentID = 0
    def __init__(self) -> None:
        # Sets the wire's ID
        self.id = Wire.currentID
        Wire.wireList[Wire.currentID] = self
        Wire.currentID += 1
        self.hasPolarity = True

        #self.voltage = voltage
        #self.current = current
        self.terminals:  dict[int, Terminal | None] = {
            0: None,
            1: None
        }

    @staticmethod
    def getWireList():
        return Wire.wireList

