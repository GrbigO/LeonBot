from typing import Callable

from telegram import Update


class UserRequest:
	__slots__ = (
		"for_bot",
		"for_ai",
		"in_group",
		"in_pv",
		"message",
		"instance",
		"metadata",
		"funcs",
		"ai_output"
	)

	def __init__(
			self,
			request_for_bot: bool = False,
			request_for_ai: bool = False,
			request_in_pv: bool = False,
			request_in_group: bool = False,
			message: str | None = None,
			instance: AI | User | None = None,
			metadata: Update | None = None,
	):
		self.for_bot: bool = request_for_bot
		self.for_ai: bool = request_for_ai,
		self.in_pv: bool = request_in_pv,
		self.in_group: bool = request_in_group,

		self.message: str | None = message,
		self.instance: AI | User | None = instance,
		self.metadata: Update | None = metadata,


		self.ai_output: str | None = None
		self.funcs: list[Callable[[UserRequest], ...]] | list = []

