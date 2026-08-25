class Terminal:
    def __init__(self, connectedElement, isPositive: bool) -> None:
        self.connectedElement = connectedElement
        self.isPositive = isPositive

    def getConnectedElement(self):
        return self.connectedElement

    def getConnectedElementDescription(self):
        return self.connectedElement.__class__.__name__ + str(self.connectedElement.id)
        