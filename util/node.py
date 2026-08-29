from components.ground import Ground
from components.terminal import Terminal
from util.enums import NodeDirection

class Node:
    nodeList = {}
    currentID = 0

    def __init__(self) -> None:
        self.elements: dict[int, Terminal | None] = {
        0: None,
        1: None,
        2: None,
        3: None,
        } # anti-clockwise notation: 0 is right, 1 is top, 2 is left, 3 is bottom
        self.id = Node.currentID
        Node.nodeList[Node.currentID] = self
        Node.currentID += 1
    '''
    def connectElementR(self, elementR):
        self.elements[0] = elementR
    
    def connectElementT(self, elementT):
        self.elements[1] = elementT

    def connectElementL(self, elementL):
        self.elements[2] = elementL

    def connectElementB(self, elementB):
        self.elements[3] = elementB
    '''

    def printNodeScheme(self):
        for i in range(4):
            element = self.elements[i]
            if element:
                if type(element.connectedElement.element) is not Ground:
                    if element == element.connectedElement.terminals[0]:
                        print(f"Node {self.id} {NodeDirection(i).name}: +{element.getConnectedElementDescription()}")
                    else:
                        print(f"Node {self.id} {NodeDirection(i).name}: -{element.getConnectedElementDescription()}")
                else:
                    print(f"Node {self.id} {NodeDirection(i).name}: {element.getConnectedElementDescription()}")


    def getElements(self):
        return self.elements

    @staticmethod
    def getNodeList():
        return Node.nodeList