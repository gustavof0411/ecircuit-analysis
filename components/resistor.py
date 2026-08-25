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
        self.posTerminal = Terminal(self, True, None)
        self.negTerminal = Terminal(self, False, None)

    def addItem(self):
        self.currentID += 1

    def getResistance(self):
        return self.resistance

    def getPosTerminal(self):
        return self.posTerminal

    def getNegTerminal(self):
        return self.negTerminal

    def connectPosTerminal(self, node: Node, position: str):
        self.posTerminal.connectedNodeID = node.id
        if (position == "r"):
            node.elementR = self.negTerminal
        elif (position == "t"):
            node.elementT = self.negTerminal
        elif (position == "l"):
            node.elementL = self.negTerminal
        elif (position == "b"):
            node.elementB = self.negTerminal
        else:
            print('error while connecting pos terminal')

    def connectNegTerminal(self, node: Node, position: str):
        self.negTerminal.connectedNodeID = node.id
        if (position == "r"):
            node.elementR = self.negTerminal
        elif (position == "t"):
            node.elementT = self.negTerminal
        elif (position == "l"):
            node.elementL = self.negTerminal
        elif (position == "b"):
            node.elementB = self.negTerminal
        else:
            print('error while connecting neg terminal')

    @staticmethod
    def getResistorByID(id: int):
        return Resistor.resList[id]
