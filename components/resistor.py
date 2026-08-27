class Resistor:
    resList = {}
    currentID = 0
    def __init__(self, resistance: float) -> None:
        self.id = Resistor.currentID
        Resistor.resList[Resistor.currentID] = self
        Resistor.currentID += 1

        self.hasPolarity = True
        self.resistance = resistance

    def getResistance(self):
        return self.resistance

    @staticmethod
    def getResistorByID(id: int):
        return Resistor.resList[id]
