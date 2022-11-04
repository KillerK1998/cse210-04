from OutputService import OutputService
class Gem(OutputService):

    def __init__(self):

        super(Gem,self).__init__()
        self.appearance = "*"
        self.points = 1
        self._position = Point(randomNumberFrom0To1* WINDOWWIDTH, 0)