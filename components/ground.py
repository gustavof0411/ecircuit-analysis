from components.terminal import Terminal

class Ground:
    groundList = {}
    currentID = 0
    def __init__(self) -> None:
        self.id = Ground.currentID
        Ground.groundList[Ground.currentID] = self
        Ground.currentID += 1
        # terminal 0 is positive, terminal 1 is negative
        self.terminals:  dict[int, Terminal | None] = {
            0: None
        }
        self.hasPolarity = True