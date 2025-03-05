from model import Model
from view import View

# Controller <: UpdateHandler
class Controller:
	def __init__(self, model: Model, view: View) -> None:
		self._model = model
		self._view = view

		

	def start(self):
		model = self._model

		self._view.start(model.screen_width, model.screen_height, model.fps, self)

	def update(self):
 		print("Controller's update was called")
