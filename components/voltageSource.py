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
        self.hasPolarity = True
        # terminal 0 is positive, terminal 1 is negative
        self.terminals:  dict[int, Terminal | None] = {
            0: None,
            1: None
        }

    def getVoltage(self):
        return self.voltage

    @staticmethod
    def getVoltageSourceList():
        return VoltageSource.voltageSourceList