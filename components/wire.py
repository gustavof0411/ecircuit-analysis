from util.current import Current
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

    @staticmethod
    def getWireList():
        return Wire.wireList

