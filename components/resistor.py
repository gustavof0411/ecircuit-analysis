from components.terminal import Terminal
from util.node import Node


class Resistor:
    resList = {}
    currentID = 0
    def __init__(self, resistance: float) -> None:
        self.id = Resistor.currentID
        Resistor.resList[Resistor.currentID] = self
        Resistor.currentID += 1

        self.hasPolarity = True
        self.resistance = resistance
        # terminal 0 is positive, terminal 1 is negative
        self.terminals:  dict[int, Terminal | None] = {
            0: None,
            1: None
        }

    def getResistance(self):
        return self.resistance

    @staticmethod
    def getResistorByID(id: int):
        return Resistor.resList[id]
