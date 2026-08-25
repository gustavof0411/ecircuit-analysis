from components.resistor import Resistor
from components.voltageSource import VoltageSource
from components.ground import Ground
from components.wire import Wire
from util.current import Current
from util.node import Node
from util.voltage import Voltage

res1 = Resistor(220)
res2 = Resistor(330)

node1 = Node()

res1.connectNegTerminal(node1, "t")

node2 = Node()
res1.connectPosTerminal(node2, "b")

res2.connectNegTerminal(node2, "r")

node3 = Node()
wire1 = Wire()

res2.connectPosTerminal(node3, "l")

wire1.connectStartTerminal(node3, "b")


node4 = Node()

wire1.connectEndTerminal(node4, "t")
node1.connectElementR(node4)

ground = Ground()
ground.connectNodeToBottom(node1)

print("Node 1")
node1.printNodeScheme()

print("Node 2")
node2.printNodeScheme()

print("Node 3")
node3.printNodeScheme()

print("Node 4")
node4.printNodeScheme()

aaa = Node.getNodeList()[1]
print("aa")