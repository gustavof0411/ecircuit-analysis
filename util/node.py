import itertools

class Node:
    id_iter = itertools.count()

    def __init__(self, elementR=None, elementT=None, elementL=None, elementB=None) -> None:
        self.elementR = elementR
        self.elementT = elementT
        self.elementL = elementL
        self.elementB = elementB
        self.id = next(self.id_iter)

    def connectElementR(self, elementR):
        self.elementR = elementR

    def connectElementT(self, elementT):
        self.elementT = elementT

    def connectElementL(self, elementL):
        self.elementL = elementL

    def connectElementB(self, elementB):
        self.elementB = elementB
    

    def printNodeScheme(self):
        if (self.elementR):
            if (self.elementR.__class__.__name__ == "Terminal"):
                print("Right: " + self.elementR.__class__.__name__ + ", ID: " + str(self.elementR.elementID) + ", isPositive: " + str(self.elementR.isPositive))
            else:
                print("Right: " + self.elementR.__class__.__name__)
        else:
            print("Right: " + self.elementR.__class__.__name__)

        print("Top: " + self.elementT.__class__.__name__)

        print("Left: " + self.elementL.__class__.__name__)

        print("Bottom: " + self.elementB.__class__.__name__)

    def printSelfID(self):
        print(self.id)

    def getElementID(self, element):
        if (element):
            print("Class: " + element.__class__.__name__ + ", ID: " + str(element.id))
        else:
            print("element is None")