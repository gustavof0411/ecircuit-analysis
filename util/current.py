from components import resistor as r, voltageSource as v

class Current:
    def __init__(self, resistance: r.Resistor, voltage: v.VoltageSource) -> None:
        self.resistance = resistance
        self.voltage = voltage

    def showCurrent(self):
        print(self.voltage.getVoltage().voltage / self.resistance.getResistance())