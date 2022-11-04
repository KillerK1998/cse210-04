import pyray
from point import Point
from OutputService import OutputService
from drawable import Drawable

class InputService:

    def __init__(self):
        pass

    def get_direction(self):
        x = 0
        y = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            x = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            x = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            y = -1
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            y = 1

        direction = Point(x, y)

        return direction

def test_function():
    input_service = InputService()
    output_service = OutputService()
    output_service.open_window()
    output_service.clear_buffer()
    output_service.flush_buffer()
    test_object = Drawable(output_service)
    test_object.set_position(Point(0, 0))
    test_object.set_text("0")

    while output_service.is_window_open():
        direction = input_service.get_direction()
        test_object.set_text(f"{direction.x} {direction.y}")
        output_service.clear_buffer()
        test_object.draw()
        output_service.flush_buffer()

#test_function()