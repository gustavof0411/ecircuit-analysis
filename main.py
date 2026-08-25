from components.resistor import Resistor
from components.voltageSource import VoltageSource
from components.ground import Ground
from components.wire import Wire
from util.current import Current
from util.node import Node
from util.voltage import Voltage

volSource1 = VoltageSource(Voltage(20))
res1 = Resistor(330)

node0 = Node()

volSource1.connectNegTerminal(node0, "t")

node1 = Node()
volSource1.connectPosTerminal(node1, "b")

res1.connectNegTerminal(node1, "r")

node2 = Node()
wire1 = Wire()

res1.connectPosTerminal(node2, "l")

wire1.connectStartTerminal(node2, "b")


node3 = Node()

wire1.connectEndTerminal(node3, "t")

wire2 = Wire()
wire2.connectStartTerminal(node3, "l")
wire2.connectEndTerminal(node0, "r")

ground = Ground()
ground.connectNodeToBottom(node0)

print("Node 0 -------")
node0.printNodeScheme()

print("Node 1 ------")
node1.printNodeScheme()

print("Node 2 ------")
node2.printNodeScheme()

print("Node 3 ------")
node3.printNodeScheme()