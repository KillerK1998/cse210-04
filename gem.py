from OutputService import OutputService
from point import Point
import random

class Gem(OutputService):
    def __init__(self):

        super(Gem).__init__()
        self.appearance = "*"
        self.points = 1
        self._position = Point(random.randInt(0, 1) * 1500, 0)
        self._velocity(Point(0, 50))