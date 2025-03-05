from dataclasses import dataclass
from project_types import Pipe, PipePairInfo, BallInfo
from collections.abc import Sequence
import random


SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
FPS = 30
GAP_HEIGHT = 60
PIPE_WIDTH = 30
BIRD_VY = -2.5
PIPE_VX = 2
MIN_PIPE_HEIGHT = 10

@dataclass
class Ball:
	x: float
	y: float
	radius: float
	vy: float
	# vx: float

	@property
	def top(self):
		return self.y - self.radius

	@property
	def bottom(self):
		return self.y + self.radius

	@property
	def left(self):
		return self.x - self.radius

	@property
	def right(self):
		return self.x + self.radius


@dataclass(eq = False)
class PipePairs:
	x: float
	gap_height: float
	gap_start: float
	screen_height: int

	@property
	def top_pipe(self) -> Pipe:
		return Pipe(self.x, 0, PIPE_WIDTH, self.gap_start)

	@property
	def bottom_pipe(self) -> Pipe:
		y = self.gap_start + self.gap_height
		return Pipe(self.x, y, PIPE_WIDTH, self.screen_height - y)

	@property
	def right(self):
		return self.x + PIPE_WIDTH


class Model:
	def __init__(self, screen_width: int, screen_height: int, fps: int) -> None:
		self._screen_width = screen_width
		self._screen_height = screen_height
		self._fps = fps
		self._ball = Ball(screen_width//2, screen_height//2, 10, 0)
		self._is_game_over = False
		self._pipes: list[PipePairs] = []
		self._done_pipes: set[PipePairs] = set()
		self._score = 0
		self._frame_count = 0

	def update(self, was_spacebar_pressed: bool):

		print(self._is_game_over)

		if self.is_out_of_bounds(self._ball) == True:
			self._is_game_over = True

		if self._frame_count % (self._fps * 2) == 0:
			gap_start_y = random.randint(MIN_PIPE_HEIGHT, self._screen_height - MIN_PIPE_HEIGHT - GAP_HEIGHT) 
			self._pipes.append(PipePairs(self._screen_width, GAP_HEIGHT, gap_start_y, self._screen_height))
			print("2 second has passed")

		if self._is_game_over:
			return

		if was_spacebar_pressed:
			self._ball.vy = BIRD_VY

		self._ball.vy += 0.2
		self._ball.y += self._ball.vy

		for pipe_pair in self._pipes:
			pipe_pair.x -= PIPE_VX

			if pipe_pair not in self._done_pipes and self._ball.x > pipe_pair.x:
				self._score += 10
				self._done_pipes.add(pipe_pair)

			for pipe in [pipe_pair.top_pipe, pipe_pair.bottom_pipe]:
				if self.is_in_collision(self._ball, pipe):
					self._is_game_over = True
					break

		self._pipes = [pipe_pair for pipe_pair in self._pipes
					if pipe_pair.right >= 0]

		self._done_pipes = {pipe_pair for pipe_pair in self._done_pipes
					if pipe_pair.right >= 0}

		self._frame_count += 1

	def is_in_collision(self, ball: Ball, pipe: Pipe) -> bool:

		if ball.right < pipe.left:
			test_x = pipe.left

		elif ball.left > pipe.right:
			test_x = pipe.right

		else:
			test_x = ball.x

		if ball.bottom < pipe.top:
			test_y = pipe.top

		elif ball.top > pipe.bottom:
			test_y = pipe.bottom

		else:
			test_y = ball.y

		dist = ((test_x - ball.x)**2 + (test_y - ball.y)**2)**0.5

		return dist < ball.radius

	def is_out_of_bounds(self, ball: Ball) -> bool:
		return ball.top <= 0 or ball.bottom >= self._screen_height 


	@property
	def screen_width(self):
		return self._screen_width

	@property
	def screen_height(self):
		return self._screen_height

	@property
	def fps(self):
		return self._fps

	@property
	def pipes(self) -> Sequence[PipePairInfo]:
		return self._pipes

	@property
	def ball(self) -> BallInfo:
		return self._ball

	@property
	def score(self) -> int:
		return self._score

	@property
	def is_game_over(self) -> bool:
		return self._is_game_over
	

