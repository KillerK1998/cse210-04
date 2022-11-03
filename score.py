from pyray import *
class Score:
    def __init__(self):
        self.value = 0
    def display_score(self):
        #displays current scores
        print(f"Score: {self.value}", 20, 20,25)
    def update_score(self,points):
        self.value += points