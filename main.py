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

node4 = Node()
node5 = Node()

res1 = Resistor(550)
res2 = Resistor(660)
wire2 = Wire()

elementRes1 = Element(res1)
elementRes2 = Element(res2)
elementWire2 = Element(wire2)

elementRes1.connectTerminalPolarity(node2, nd.RIGHT, True)
elementRes1.connectTerminalPolarity(node4, nd.LEFT, False)
elementRes2.connectTerminalPolarity(node4, nd.BOTTOM, True)
elementRes2.connectTerminalPolarity(node5, nd.TOP, False)
elementWire2.connectTerminalPolarity(node5, nd.LEFT, True)
elementWire2.connectTerminalPolarity(node3, nd.RIGHT, False)

node0.printNodeScheme()

node1.printNodeScheme()

node2.printNodeScheme()

node3.printNodeScheme()

node4.printNodeScheme()
node5.printNodeScheme()


def checkClosedLoop(node: Node, analysedNodeID: int, previousDirection: nd = nd.TOP):
        if analysedNodeID == node.id:
            print(f"Reached same node, closed loop identified at node ${analysedNodeID}")
        else:
            # Find all top elements in a row
            elementTerminalTop = node.elements[1]
            # Checks if the current node equals the analysed node's ID (if so, it has come full circle and a loop was found)
            if elementTerminalTop:
                if (previousDirection != nd.BOTTOM):
                    # If there's a top element in the node, starts a new analysis with the node's ID

                    #print(f'Currently on node ${node.id}, going to element ${elementTerminalTop.getConnectedElementDescription()}')
                    if (type(elementTerminalTop.connectedElement.terminals) is not Ground and len(elementTerminalTop.connectedElement.terminals) > 1):

                        oppositeTerminal = elementTerminalTop.connectedElement.getOppositeTerminal(elementTerminalTop)
                        if oppositeTerminal:
                            nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                            nextNodeID = nextNode.id
                            print(f"Starting new loop analysis at node ${node.id}")
                            print(f'Comparing node ${analysedNodeID}, current is {node.id} and next node ID is ${nextNodeID}')
                            #There's still elements to that direction, keeps checking all of them
                            # Starts a new analysis with the current node's ID
                            checkClosedLoop(nextNode, node.id, nd.TOP)

            elementTerminalRight = node.elements[0]
            if elementTerminalRight:
                if (previousDirection != nd.LEFT):
                    if not elementTerminalTop:
                        #if (type(elementTerminalRight.connectedElement.terminals) is not Ground and len(elementTerminalRight.connectedElement.terminals) > 1):
                            #print(f'Currently on node ${node.id}, going to element ${elementTerminalRight.getConnectedElementDescription()}')
                    
                            oppositeTerminal = elementTerminalRight.connectedElement.getOppositeTerminal(elementTerminalRight)
                            if oppositeTerminal:
                                nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                                nextNodeID = nextNode.id
                                print(f'Comparing node ${analysedNodeID}, current is {node.id } and next node ID is ${nextNodeID}')
                                #There's still elements to that direction, keeps checking all of them
                                checkClosedLoop(nextNode, analysedNodeID, nd.RIGHT)

            elementTerminalBottom = node.elements[3]
            if elementTerminalBottom:
                if (previousDirection != nd.TOP):
                        if (not elementTerminalRight):
                            if (type(elementTerminalBottom.connectedElement.terminals) is not Ground and len(elementTerminalBottom.connectedElement.terminals) > 1):
                                #print(f'Currently on node ${node.id}, going to element ${elementTerminalBottom.getConnectedElementDescription()}')
                                oppositeTerminal = elementTerminalBottom.connectedElement.getOppositeTerminal(elementTerminalBottom)
                                if oppositeTerminal:
                                    nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                                    nextNodeID = nextNode.id
                                    print(f'Comparing node ${analysedNodeID}, current is {node.id } and next node ID is ${nextNodeID}')

                                    #There's still elements to that direction, keeps checking all of them
                                    checkClosedLoop(nextNode, analysedNodeID, nd.BOTTOM)

            elementTerminalLeft = node.elements[2]
            if elementTerminalLeft:
                if (previousDirection != nd.RIGHT):
                        if (not elementTerminalRight): # goes to the left only if there is no elements to the right

                            if (type(elementTerminalLeft.connectedElement.terminals) is not Ground and len(elementTerminalLeft.connectedElement.terminals) > 1):
                                #print(f'Currently on node ${node.id}, going to element ${elementTerminalLeft.getConnectedElementDescription()}')
                        
                                oppositeTerminal = elementTerminalLeft.connectedElement.getOppositeTerminal(elementTerminalLeft)
                                if oppositeTerminal:
                                    nextNode = Node.getNodeList()[oppositeTerminal.connectedNodeID]
                                    nextNodeID = nextNode.id
                                    print(f'Comparing node ${analysedNodeID}, current is {node.id} and next node ID is ${nextNodeID}')
                                    #There's still elements to that direction, keeps checking all of them
                                    checkClosedLoop(nextNode, analysedNodeID, nd.LEFT)


checkClosedLoop(node0, -1)