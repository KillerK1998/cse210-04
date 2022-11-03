import pyray
from color import Color

class OutputService:
    def __init__(self):
        self._width = 500
        self._height = 500
        self._caption = "test"
        self._frame_rate = 60

    def set_width(self, width):
        self._width = width
        return self

    def set_height(self, height):
        self._height = height
        return self

    def set_caption(self, caption):
        self._caption = caption
        return self

    def set_frame_rate(self, frame_rate):
        self._frame_rate = frame_rate
        return self

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_caption(self):
        return self._caption

    def get_frame_rate(self):
        return self._frame_rate

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

    def draw_text(self, text, x, y, font_size, color):
        pyray.draw_text(text, x, y, font_size, color)

    def flush_buffer(self):
        pyray.end_drawing()

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

def testFunction():
    output_service = OutputService()
    output_service.open_window()
    thing = {"x": 0, "y": 0}
    color = (255, 0, 0, 255)
    while output_service.is_window_open():
        x = thing["x"]
        y = thing["y"]
        output_service.clear_buffer
        output_service.draw_text("o", x, y, 4, color)
        output_service.flush_buffer()
        thing["x"] = thing["x"] + 1
        thing["y"] = thing["y"] + 1

testFunction()