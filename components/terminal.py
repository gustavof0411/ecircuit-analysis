class Terminal:
    def __init__(self, connectedElement, nodeID: int) -> None:
        self.connectedElement = connectedElement
        self.connectedNodeID = nodeID

    def getConnectedElement(self):
        return self.connectedElement

    def getConnectedElementDescription(self):
        return self.connectedElement.element.__class__.__name__ + str(self.connectedElement.element.id)
        