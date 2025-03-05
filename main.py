import pyxel

def draw():
	pyxel.cls(0)

	for pipe_pair in pipes:
		for pipe in [pipe_pair.top_pipe, pipe_pair.bottom_pipe]:
			pyxel.rect(pipe.x, pipe.y, pipe.width, pipe.height, 5)

	pyxel.circ(bird.x, bird.y, bird.radius, 7)

	pyxel.text(SCREEN_WIDTH // 2 - 3, 15, str(score), 8)

	if is_game_over:
		pyxel.text(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2, "GAME OVER", 8)

pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps= FPS) # you can add fps for third parameter
pyxel.run(update, draw) 