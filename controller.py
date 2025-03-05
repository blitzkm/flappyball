from model import Model
from view import View

# Controller <: UpdateHandler
class Controller:
	def __init__(self, model: Model, view: View) -> None:
		self._model = model
		self._view = view


	def start(self):
		model = self._model

		self._view.start(model.fps, self, self)

	def update(self):
		print("Controller's update was called")

		self._model.update(self._view.was_spacebar_pressed())

	def draw(self):
		self._view.clear_screen()

		self._view.draw_pipes(self._model.pipes)

		self._view.draw_ball(self._model.ball)

		self._view.show_score(self._model.score)

		if self._model.is_game_over:
			self._view.show_is_game_over()


 