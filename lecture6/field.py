from location import Location

class Field:
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        xDist, yDist = drunk.takeStep()
        currentLoc = self.drunks[drunk]
        self.drunks[drunk] = currentLoc.move(xDist, yDist)

    def getLoc(self, drunk):
        return self.drunks[drunk]
