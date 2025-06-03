from typing import Callable
asy = "1"

class CathAlgorithm:

	@classmethod
	def asy(cls):
		return asy

	@classmethod
	def alg1(cls):
		pass

	@classmethod
	def alg2(cls):
		pass

	@classmethod
	def alg3(cls):
		pass

	@classmethod
	def alg4(cls):
		pass


def get_alg(
		self_text: str,
		self_user: models.User = None,
		users: tuple[models.User, str] | None = None,
) -> Callable[[], Algorithm]:
	pass



