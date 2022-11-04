from point import Point
from color import Color
from datetime import datetime
from OutputService import OutputService

class Drawable:

    def __init__(self, output_service):
        self._text = "default"
        self._font_size = 10
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._output_service = output_service

    def get_color(self):
        return self._color

    def get_position(self):
        return self._position
    
    def get_font_size(self):
        return self._font_size

    def get_text(self):
        return self._text

    def get_velocity(self):
        return self._velocity

    def do_updates(self):
        self.update_position()

    def update_position(self):
        delta_time = self._output_service.get_delta_time()
        x = self._position.x + self._velocity.x * delta_time
        y = self._position.y + self._velocity.y * delta_time
        self._position = Point(x, y)

    def set_color(self, color):
        self._color = color
        return self

    def set_position(self, position):
        self._position = position
        return self

    def set_font_size(self, font_size):
        self._font_size = font_size
        return self

    def set_text(self, text):
        self._text = text
        return self

    def set_velocity(self, velocity):
        self._velocity = velocity
        return self

    def set_output_service(self, output_service):
        self._output_service = output_service
        return self

    def draw(self):
        tuple_color = self._color.to_tuple()
        
        self._output_service.draw_text(self._text, int(self._position.x),
          int(self._position.y), self._font_size, tuple_color)

def test_function():
    output_service = OutputService()
    output_service.set_width(1500)
    output_service.set_height(900)
    output_service.open_window()

    test_object = Drawable(output_service)
    test_object.set_color(Color(255, 0, 0))
    test_object.set_text("o")
    test_object.set_velocity(Point(0, 50)) #move 50 pixels/second in x direction and y direction
    test_object.set_position(Point(0, 0))
    test_object.set_font_size(25)

    while (output_service.is_window_open()):
        output_service.do_updates()
        test_object.do_updates()
        output_service.clear_buffer()
        test_object.draw()
        output_service.flush_buffer()
        
#test_function()


