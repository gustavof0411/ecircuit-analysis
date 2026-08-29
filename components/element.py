from components.ground import Ground
from components.resistor import Resistor
from components.voltageSource import VoltageSource
from components.wire import Wire
from components.terminal import Terminal
from util.node import Node
from util.enums import NodeDirection

class Element:
    def __init__(self, element: Ground | Resistor | VoltageSource | Wire) -> None:
        self.element = element
        ''' 
        terminals[0] is negative, terminals[1] is positive 
        for elements that have polarity.
        Wire and Resistor classes have no polarity, but follow the same logic.
        If the element is a Ground, it will only have one terminal in terminals[0]
        '''
        self.terminals = {}


    def connectTerminalPolarity(self, node: Node, position: NodeDirection, polarity: bool = False):
            if type(self.element) is not Ground:
                terminal = Terminal(self, node.id)
                if polarity:
                    self.terminals[0] = terminal
                    node.getElements()[position.value] = self.terminals[0]
                else:
                    self.terminals[1] = terminal
                    node.getElements()[position.value] = self.terminals[1]
            else:
                print(f"Coudn't connect ${self.getElementDescription()}: must be a Ground element to use this method")
            

    def connectTerminal(self, node: Node, position: NodeDirection):
        if type(self.element) is Ground:
            terminal = Terminal(self, node.id)
            self.terminals[0] = terminal
            node.getElements()[position.value] = self.terminals[0]
        else:
            print(f"Coudn't connect ${self.getElementDescription()}: must be a Ground element to use this method")

    def getOppositeTerminal(self, terminal: Terminal):
        if (len(self.terminals) == 2):

            if (self.terminals[0].connectedNodeID != terminal.connectedNodeID):
                return self.terminals[0]
            return self.terminals[1]
        else:
            print(f"NO CORRECT AMOUNT OF TERMINALS FOR THIS ELEMENT (${self.element.__class__.__name__ + str(self.element.id)})")

    def elementHasPolarity(self):
        return type(self.element) is VoltageSource

    def getElementDescription(self):
            return self.element.__class__.__name__ + str(self.element.id)
            