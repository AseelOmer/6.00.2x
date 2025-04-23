import random

class Drunk:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'This drunk is named {self.name}'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]  # North, South, East, West
        return random.choice(stepChoices)
