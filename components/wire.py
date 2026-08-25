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

        #self.voltage = voltage
        #self.current = current
        self.startTerminal = Terminal(self, True)
        self.endTerminal = Terminal(self, False)

    def connectStartTerminal(self, node, position: str):
        if (position == "r"):
            node.getElements()[0] = self.startTerminal
        elif (position == "t"):
            node.getElements()[1] = self.startTerminal
        elif (position == "l"):
            node.getElements()[2] = self.startTerminal
        elif (position == "b"):
            node.getElements()[3] = self.startTerminal
        else:
            print('error while connecting start terminal')

    def connectEndTerminal(self, node, position: str):
        if (position == "r"):
            node.getElements()[0] = self.endTerminal
        elif (position == "t"):
            node.getElements()[1] = self.endTerminal
        elif (position == "l"):
            node.getElements()[2] = self.endTerminal
        elif (position == "b"):
            node.getElements()[3] = self.endTerminal
        else:
            print('error while connecting end terminal')

    @staticmethod
    def getWireList():
        return Wire.wireList

