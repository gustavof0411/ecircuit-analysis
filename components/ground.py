from components.terminal import Terminal
from util.node import Node

class Ground:
    groundList = {}
    currentID = 0
    def __init__(self) -> None:
        self.id = Ground.currentID
        Ground.groundList[Ground.currentID] = self
        Ground.currentID += 1
        self.connectedTerminal = Terminal(self, False)

    def connectNodeToBottom(self, node):
        node.getElements()[3] = self.connectedTerminal