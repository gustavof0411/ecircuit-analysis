from util.voltage import Voltage

class VoltageSource:
    def __init__(self, voltage: Voltage) -> None:
        self.voltage = voltage

    def getVoltage(self):
        return self.voltage