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
        self.terminals = {}


    def connectTerminalPolarity(self, node: Node, position: NodeDirection, polarity: bool = False):
            terminal = Terminal(self, node.id)
            if self.element.hasPolarity:
                self.terminals[0] = terminal
                node.getElements()[position.value] = self.terminals[0]
            else:
                self.terminals[1] = terminal
                node.getElements()[position.value] = self.terminals[1]

    def getOppositeTerminal(self, terminal: Terminal):
        if (self.terminals[0] == terminal):
            return self.terminals[1]
        return terminal

    def elementHasPolarity(self):
        return type(self.element) is VoltageSource