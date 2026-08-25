from components.terminal import Terminal
from util.node import Node


class Resistor:
    resList = {}
    currentID = 0
    def __init__(self, resistance: float) -> None:
        self.id = Resistor.currentID
        Resistor.resList[Resistor.currentID] = self
        Resistor.currentID += 1

        self.resistance = resistance
        self.posTerminal = Terminal(self, True)
        self.negTerminal = Terminal(self, False)

    def getResistance(self):
        return self.resistance

    def getPosTerminal(self):
        return self.posTerminal

    def getNegTerminal(self):
        return self.negTerminal

    def connectPosTerminal(self, node, position: str):
        if (position == "r"):
            node.getElements()[0] = self.posTerminal
        elif (position == "t"):
            node.getElements()[1] = self.posTerminal
        elif (position == "l"):
            node.getElements()[2] = self.posTerminal
        elif (position == "b"):
            node.getElements()[3] = self.posTerminal
        else:
            print('error while connecting pos terminal')

    def connectNegTerminal(self, node, position: str):
        if (position == "r"):
            node.getElements()[0] = self.negTerminal
        elif (position == "t"):
            node.getElements()[1] = self.negTerminal
        elif (position == "l"):
            node.getElements()[2] = self.negTerminal
        elif (position == "b"):
            node.getElements()[3] = self.negTerminal
        else:
            print('error while connecting neg terminal')

    @staticmethod
    def getResistorByID(id: int):
        return Resistor.resList[id]
