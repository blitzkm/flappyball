from typing import Protocol
from dataclasses import dataclass

class UpdateHandler(Protocol):
	def update(self) -> None:
		pass
		

class DrawHandler(Protocol):
	def draw(self):
		...

@dataclass(frozen=True)
class Pipe:
	x: float
	y: float
	width: float
	height: float

	@property
	def top(self):
		return self.y

	@property
	def bottom(self):
		return self.y + self.height

	@property
	def left(self):
		return self.x

	@property
	def right(self):
		return self.x + self.width

# @dataclass(frozen= True)
class PipePairInfo(Protocol):
	@property
	def top_pipe(self) -> Pipe:
		...

	@property
	def bottom_pipe(self) -> Pipe:
		...



class BallInfo(Protocol):
	@property
	def x(self) -> float:
		...

	@property
	def y(self) -> float:
		...

	@property
	def radius(self) -> float:
		...
