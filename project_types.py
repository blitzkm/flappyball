from typing import Protocol

class UpdateHandler(Protocol):
	def update(self) -> None:
		pass
		