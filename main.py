from model import Model
from controller import Controller
from view import View

def main():
	screen_width = 200
	screen_height = 200
	fps = 30

	model = Model(screen_width, screen_height, fps)
	view = View()
	controller = Controller(model, view)

	controller.start()


if __name__ == '__main__':
	main()

