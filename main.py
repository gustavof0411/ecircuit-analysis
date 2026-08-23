from components import resistor as r, voltageSource as v
from util import current as c

res = r.Resistor(220)

vol = v.VoltageSource(2)

current = c.Current(res, vol)

current.showCurrent()

