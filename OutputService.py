class OutputService:
import pyray

class OutputService:
    def __init__(self, width, height, caption, frame_rate):
        self._width = width
        self._height = height
        self._caption = caption
        self._frame_rate = frame_rate
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
    output_service = OutputService(500, 500, "test", 60)
    output_service.open_window()
    thing = {"x": 0, "y": 0}
    color = (255, 0, 0, 255)
    while output_service.is_window_open():
        x = thing["x"]
        y = thing["y"]
        output_service.clear_buffer
        output_service.draw_text("o", x, y, 4, color)
        output_service.flush_buffer()
        thing["x"] = thing["x"] + 5
        thing["y"] = thing["y"] + 5

#testFunction()