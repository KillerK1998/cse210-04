from drawable import Drawable
from InputService import InputService
from point import Point
from color import Color
from datetime import datetime
from OutputService import OutputService

class DrawablePlayer(Drawable):

    def __init__(self, output_service, input_service):
        super().__init__(output_service)
        self._text = "#"
        self._input_service = input_service
        self._speed = 200 #default speed is 200 pixels per second

    def set_speed(self, speed):
        self._speed = speed
    
    def get_speed(self):
        return self._speed
    
    def do_updates(self):
        self.update_velocity()
        super().do_updates()
    
    def update_velocity(self):
        key_direction = self._input_service.get_direction()
        new_x = key_direction.x * self._speed
        new_y = key_direction.y * self._speed
        self._velocity = Point(new_x, new_y)

def test_function():
    output_service = OutputService()
    output_service.set_width(1500)
    output_service.set_height(900)
    output_service.open_window()
    input_service = InputService()

    test_object = DrawablePlayer(output_service, input_service)
    test_object.set_position(Point(0, 0))

    while (output_service.is_window_open()):
        output_service.do_updates()
        test_object.do_updates()
        output_service.clear_buffer()
        test_object.draw()
        output_service.flush_buffer()

#test_function()
