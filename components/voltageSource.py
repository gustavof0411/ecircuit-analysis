class VoltageSource:
    def __init__(self, voltage: float) -> None:
        self.voltage = voltage

    def getVoltage(self):
        return self.voltage