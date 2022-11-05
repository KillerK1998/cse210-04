from pyray import *
from drawable import Drawable
class Score(Drawable):
    def __init__(self, output_service):
        super().__init__(output_service)
        self.value = 0
        self.update_score(self.value)
        self.set_font_size(50)
    def display_score(self):
        #displays current scores
        print(f"Score: {self.value}")
    def update_score(self, points):
        self.value += points
        self._text = f"{self.value}"