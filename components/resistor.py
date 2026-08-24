from components.terminal import Terminal
from util.node import Node
import itertools

class Resistor:
    id_iter = itertools.count()    
    def __init__(self, resistance: float) -> None:
        # Sets the resistor's ID
        self.id = next(self.id_iter)

        self.resistance = resistance
        self.posTerminal = Terminal(self.id, True)
        self.negTerminal = Terminal(self.id, False)


    def getResistance(self):
        return self.resistance

    def getPosTerminal(self):
        return self.posTerminal

    def getNegTerminal(self):
        return self.negTerminal

    def connectPosTerminal(self, node: Node, position: str):
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

