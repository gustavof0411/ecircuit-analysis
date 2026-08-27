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

    def getVoltage(self):
        return self.voltage

    @staticmethod
    def getVoltageSourceList():
        return VoltageSource.voltageSourceList