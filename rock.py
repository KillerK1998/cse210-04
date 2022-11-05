from OutputService import OutputService
from point import Point
import random
from drawable import Drawable

class Rock(Drawable):
    def __init__(self, output_service):

        super().__init__(output_service)
        self._text = "0"
        self._font_size = 25
        self._points = 1
        self._position = Point(random.randint(0, 1500), 0)
        self._velocity = Point(0, 50)