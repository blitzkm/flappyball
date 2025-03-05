import pyxel

from project_types import UpdateHandler


class View:

	def __init__(self) -> None:
		self._update_handler = None
		

	def start(self, screen_width:int, screen_height:int, fps: int, update_handler: UpdateHandler):
		self._update_handler = update_handler

		pyxel.init(screen_width, screen_height, fps= fps) # you can add fps for third parameter
		pyxel.run(update_handler.update, self.draw) 

	# def update(self):
	# 	self._update_handler.update()


	def draw(self):
		...



	def temp(self):
		pyxel.cls(0)

		for pipe_pair in pipes:
			for pipe in [pipe_pair.top_pipe, pipe_pair.bottom_pipe]:
				pyxel.rect(pipe.x, pipe.y, pipe.width, pipe.height, 5)

		pyxel.circ(bird.x, bird.y, bird.radius, 7)

		pyxel.text(SCREEN_WIDTH // 2 - 3, 15, str(score), 8)

		if is_game_over:
			pyxel.text(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2, "GAME OVER", 8)