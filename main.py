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

res2.connectNegTerminal(node2, "l")

res2.connectPosTerminal(node1, "r")

node1.printNodeScheme()
node2.printNodeScheme()


def checkClosedLoop(node: Node):
    if (node.elementT != None):
        checkClosedLoop(node.elementT)
    if (node.elementR != None):
        checkClosedLoop(node.elementR)
    if (node.elementB != None):
        checkClosedLoop(node.elementB)
    if (node.elementL != None):
        checkClosedLoop(node.elementL)

    if (node.elementB == Ground):
        print("closed")

