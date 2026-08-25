class Terminal:
    def __init__(self, elementID, isPositive: bool, connectedNodeID) -> None:
        self.id = elementID
        self.elementType = elementID.__class__.__name__
        self.connectedNodeID = connectedNodeID
        self.isPositive = isPositive

    def getConnectedNodeID(self):
        return self.connectedNodeID