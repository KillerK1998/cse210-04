from pyray import *
from drawable import Drawable
class Score(Drawable):
    def __init__(self):
        super().__init__()
        self.value = 0
    def display_score(self):
        #displays current scores
        print(f"Score: {self.value}")
    def update_score(self,points):
        self.value += points