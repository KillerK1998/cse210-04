from drawable_player import DrawablePlayer
from InputService import InputService
from OutputService import OutputService
from point import Point
from gem import Gem
from score import Score
import pyray
from rock import Rock

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
        self._gems = []
        self._score = Score()
        self._rocks = []

    def start_game(self):
        self._output_service.open_window()

        while (self._output_service.is_window_open()):
            self.do_updates()
            self.do_outputs()

        self._output_service.close_window()

    def do_updates(self):
        self._output_service.do_updates()
        self._player.do_updates()
        for gem in self._gems:
            gem.do_updates()
        if len(self._gems) < 20:
            self._gems.append(Gem(self._output_service))
        for gem in self._gems:
            gem_p = gem.get_position()
            player_p = self._player.get_position()

            if pyray.is_key_down(pyray.KEY_A):
                print(f"{gem_p.x} {gem_p.y} {player_p.x} {player_p.y}")
            if self.is_close(int(gem_p.x), int(player_p.x)) and self.is_close(int(gem_p.y), int(player_p.y)):
                self._gems.remove(gem)
            if gem.get_position().y >= WINDOW_HEIGHT:
                self._gems.remove(gem)

    def is_close(self, x, otherx):
        is_close = False
        precision = 50
        lower_limit = otherx - precision
        upper_limit = otherx + precision

        if lower_limit <= x <= upper_limit:
            is_close = True

        return is_close

    def do_outputs(self):
        self._output_service.clear_buffer()
        self._player.draw()
        for gem in self._gems:
            gem.draw()
        for rock in self._rocks:
            rock.draw()
        self._output_service.flush_buffer()
        Score.display_score()