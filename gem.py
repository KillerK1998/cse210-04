from OutputService import OutputService
from point import Point
import random
from drawable import Drawable

class Gem(Drawable):
    def __init__(self, output_service):

        super().__init__(output_service)
        self._text = "*"
        self._font_size = 30
        self._points = 1
        self._position = Point(random.randint(0, 1500), 0)
        print(f"{self._position.x} {self._position.y}")
        self._velocity = Point(0, 50)