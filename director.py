from drawable_player import DrawablePlayer
from InputService import InputService
from OutputService import OutputService
from point import Point

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 900
CAPTION = "Greed"

class Director:
    def __init__(self):
        self._output_service = OutputService()
        self._output_service.set_width(WINDOW_WIDTH)
        self._output_service.set_height(WINDOW_HEIGHT)
        self._output_service.set_caption(CAPTION)

        self.input_service = InputService()
        
        self._player = DrawablePlayer(self._output_service, self.input_service)
        player_start_x = WINDOW_WIDTH / 2
        player_start_y = WINDOW_HEIGHT / 2
        self._player.set_position(Point(player_start_x, player_start_y))

    def start_game(self):
        self._output_service.open_window()

        while (self._output_service.is_window_open()):
            self.do_updates()
            self.do_outputs()

        self._output_service.close_window()

    def do_updates(self):
        self._output_service.do_updates()
        self._player.do_updates()

    def do_outputs(self):
        self._output_service.clear_buffer()
        self._player.draw()
        self._output_service.flush_buffer()