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
            terminal = Terminal(self.element, node.id)
            if self.element.hasPolarity:
                self.element.terminals[0] = terminal
                node.getElements()[position.value] = self.element.terminals[0]
            else:
                self.element.terminals[1] = terminal
                node.getElements()[position.value] = self.element.terminals[1]


    def elementHasPolarity(self):
        return type(self.element) is VoltageSource