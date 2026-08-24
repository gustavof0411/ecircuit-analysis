from util.node import Node

class Ground:
    def __init__(self, connectedNode: Node) -> None:
        self.connectedNode = connectedNode

    def getGroundNode(self):
        return self.connectedNode