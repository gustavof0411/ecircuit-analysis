from components.resistor import Resistor
from components.voltageSource import VoltageSource
from components.ground import Ground
from components.wire import Wire
from util.current import Current
from util.node import Node
from util.voltage import Voltage
from util.enums import NodeDirection as nd
from components.element import Element

volSource0 = VoltageSource(Voltage(20))
res0 = Resistor(330)
wire0 = Wire()
wire1 = Wire()

node0 = Node()
node1 = Node()
node2 = Node()
node3 = Node()

ground = Ground()

elementVolSource =  Element(volSource0)
elementRes = Element(res0)
elementWire0 = Element(wire0)
elementWire1 = Element(wire1)
elementGround = Element(ground)

elementVolSource.connectTerminalPolarity(node0, nd.TOP, False)
elementVolSource.connectTerminalPolarity(node1, nd.BOTTOM, True)
elementRes.connectTerminalPolarity(node1, nd.RIGHT, True)
elementRes.connectTerminalPolarity(node2, nd.LEFT, False)
elementWire0.connectTerminalPolarity(node2, nd.BOTTOM, True)
elementWire0.connectTerminalPolarity(node3, nd.TOP, False)
elementWire1.connectTerminalPolarity(node3, nd.RIGHT, False)
elementWire1.connectTerminalPolarity(node0, nd.LEFT, False)
elementGround.connectTerminalPolarity(node0, nd.BOTTOM)

node0.printNodeScheme()

node1.printNodeScheme()

node2.printNodeScheme()

node3.printNodeScheme()

'''
def checkClosedLoop(startNode: Node):
    startNodeID = startNode.id
    nextNodeID=-1
    # There is components to the right
    if startNode.elements[0]:
        if (startNode.elements[0].isPositive):
            nextNodeID = startNode.elements[0].connectedElement.negTerminal.connectedElement.id
            checkClosedLoop(startNode.elements[0].connectedElement.negTerminal.connectedElement)
        else:
            nextNodeID = startNode.elements[0].connectedElement.posTerminal.connectedElement.id
            checkClosedLoop(startNode.elements[0].connectedElement.posTerminal.)

    if startNode == nextNodeID and nextNodeID > -1:
        print("yes")



checkClosedLoop(node1)
'''