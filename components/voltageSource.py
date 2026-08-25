from components.terminal import Terminal
from util.voltage import Voltage

class VoltageSource:
    voltageSourceList = {}
    currentID = 0
    def __init__(self, voltage: Voltage) -> None:
        self.id = VoltageSource.currentID
        VoltageSource.voltageSourceList[VoltageSource.currentID] = self
        VoltageSource.currentID += 1
        self.voltage = voltage
        self.posTerminal = Terminal(self, True)
        self.negTerminal = Terminal(self, False)

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

    def getVoltage(self):
        return self.voltage

    @staticmethod
    def getVoltageSourceList():
        return VoltageSource.voltageSourceList