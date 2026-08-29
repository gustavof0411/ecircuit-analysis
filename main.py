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
elementWire1.connectTerminalPolarity(node3, nd.LEFT, True)
elementWire1.connectTerminalPolarity(node0, nd.RIGHT, False)
elementGround.connectTerminal(node0, nd.BOTTOM)

node0.printNodeScheme()

node1.printNodeScheme()

node2.printNodeScheme()

node3.printNodeScheme()


def checkClosedLoop(node: Node, firstNodeID: int, previousDirection: nd = nd.TOP):
    nodeID = node.id
    nextNodeID=-1
    # Find all top elements in a row
    elementTerminalTop = node.elements[1]
    '''
    elementTerminalRight = node.elements[0]
    elementTerminalBottom = node.elements[3]
    elementTerminalLeft = node.elements[2]
    elementAnalysed = ""
    if elementTerminalTop:
        elementAnalysed = elementTerminalTop
        print("top")
    elif elementTerminalRight:
        elementAnalysed = elementTerminalRight
        print("rigth")
    elif elementTerminalBottom:
        elementAnalysed = elementTerminalBottom
        print("bottom")
    elif elementTerminalLeft:
        elementAnalysed = elementTerminalLeft
        print("left")
    '''

    if (firstNodeID != node.id):
        if elementTerminalTop:
            if (previousDirection != nd.BOTTOM):
                firstNodeID = node.id
                print(f'Currently on node ${node.id}, going to element ${elementTerminalTop.getConnectedElementDescription()}')

                oppositeTerminal = elementTerminalTop.connectedElement.getOppositeTerminal(elementTerminalTop)
                if oppositeTerminal:
                    nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                    nextNodeID = nextNode.id
                    print(f'Comparing node ${firstNodeID}, next node ID is ${nextNodeID}')
                    #There's still elements to that direction, keeps checking all of them
                    checkClosedLoop(nextNode, firstNodeID, nd.TOP)

        elementTerminalRight = node.elements[0]
        if elementTerminalRight:
            if (previousDirection != nd.LEFT):
                if (firstNodeID != node.id):
                    print(f'Currently on node ${node.id}, going to element ${elementTerminalRight.getConnectedElementDescription()}')
            
                    oppositeTerminal = elementTerminalRight.connectedElement.getOppositeTerminal(elementTerminalRight)
                    if oppositeTerminal:
                        nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                        nextNodeID = nextNode.id
                        print(f'Comparing node ${firstNodeID}, next node ID is ${nextNodeID}')
                        #There's still elements to that direction, keeps checking all of them
                        checkClosedLoop(nextNode, firstNodeID, nd.RIGHT)

        elementTerminalBottom = node.elements[3]
        if elementTerminalBottom:
            if (previousDirection != nd.TOP):
                print(f'Currently on node ${node.id}, going to element ${elementTerminalBottom.getConnectedElementDescription()}')
                oppositeTerminal = elementTerminalBottom.connectedElement.getOppositeTerminal(elementTerminalBottom)
                if oppositeTerminal:
                    nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                    nextNodeID = nextNode.id
                    print(f'Comparing node ${firstNodeID}, next node ID is ${nextNodeID}')
                    #There's still elements to that direction, keeps checking all of them
                    checkClosedLoop(nextNode, firstNodeID, nd.BOTTOM)

        elementTerminalLeft = node.elements[2]
        if elementTerminalLeft:
            if (previousDirection != nd.RIGHT):
                print(f'Currently on node ${node.id}, going to element ${elementTerminalLeft.getConnectedElementDescription()}')
        
                oppositeTerminal = elementTerminalLeft.connectedElement.getOppositeTerminal(elementTerminalLeft)
                if oppositeTerminal:
                    nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                    nextNodeID = nextNode.id
                    print(f'Comparing node ${firstNodeID}, next node ID is ${nextNodeID}')
                    #There's still elements to that direction, keeps checking all of them
                    checkClosedLoop(nextNode, firstNodeID, nd.LEFT)


    
    if firstNodeID == nextNodeID and nextNodeID > -1:
        print("Reached same node, closed loop identified")


checkClosedLoop(node0, -1)
