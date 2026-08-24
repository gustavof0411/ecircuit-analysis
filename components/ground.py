from components.terminal import Terminal
from util.node import Node
import itertools

class Ground:
    id_iter = itertools.count()
    def __init__(self) -> None:
        self.id = next(self.id_iter)
        self.connectedTerminal = Terminal(self.id, False)

    def connectNodeToBottom(self, node: Node):
        node.elementB = self.connectedTerminal