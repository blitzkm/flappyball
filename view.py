from collections.abc import Sequence
import pyxel
from project_types import DrawHandler, UpdateHandler, PipePairInfo, BallInfo

class View:

	def __init__(self, screen_width: int, screen_height: int) -> None:
		self._screen_width = screen_width
		self._screen_height = screen_height

	def start(self, fps: int, update_handler: UpdateHandler, draw_handler: DrawHandler):
		pyxel.init(self._screen_width, self._screen_height, fps= fps)
		pyxel.run(update_handler.update, draw_handler.draw) 

	def was_spacebar_pressed(self):
		return pyxel.btnp(pyxel.KEY_SPACE)

	def clear_screen(self):
		pyxel.cls(0)

	def draw_pipes(self, pipes: Sequence[PipePairInfo]):
		for pipe_pair in pipes:
			for pipe in [pipe_pair.top_pipe, pipe_pair.bottom_pipe]:
				pyxel.rect(pipe.x, pipe.y, pipe.width, pipe.height, 5)

	def draw_ball(self, ball: BallInfo):
		pyxel.circ(ball.x, ball.y, ball.radius, 7)

	def show_score(self, score:int):
		pyxel.text(self._screen_width// 2 - 3, 15, str(score), 8)


	def show_is_game_over(self):
		pyxel.text(self._screen_width // 2 - 15, self._screen_height // 2, "GAME OVER", 8)

		