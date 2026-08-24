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

        if self.elementR is not None:
            print("Right of Node " + str(self.id) + ": " + str(self.elementR.id))


        if self.elementT is not None:
            print("Top of Node " + str(self.id) + ": " + str(self.elementT.id))


        if self.elementL is not None:
            print("Left of Node " + str(self.id) + ": " + str(self.elementL.id))


        if self.elementB is not None:
            print("Bottom of Node " + str(self.id) + ": " + str(self.elementB.id))

    def getID(self):
        return self.id

    def getElementID(self, element):
        if (element):
            print("Class: " + element.__class__.__name__ + ", ID: " + str(element.id))
        else:
            print("element is None")