from typing import Optional

from enum import Enum

from ..ai.manage import AIManager
from ..core.bot.settings import bot_settings


class LeonDSL(Enum):
	delete = None
	add = None
	update = None
	model = None
	train = None
	user = None
	perm = None
	setting = None

	__msg_for = None
	__bug = None
	__restart = None

	__all__ = None
	__func__ = dict()

	@classmethod
	async def _parse_code(cls, code, message) -> tuple[Optional[str], dict]:
		arg = {}
		func_name = "_"
		for name in code:
			if name.startswith("--"):
				arg = name
			else:
				func_name = func_name + name + "_"

		func = cls.__func__.get(func_name)
		if func is None:
			return None, {}

		return await func(message=message, arg=arg)

	@classmethod
	async def parse(cls, message) -> tuple[Optional[str], dict]:

		code = message.text.split()

		if not set(code) & cls.__all__:
			if bot_settings.IS_AI_LOCK:
				return ChatEnum.AI_LOCK_MSG.value , {"reply_to_message_id": message.message_id}
			return await AIManager.new_request(message)

		# return await cls._parse_code(code, message)

LeonDSL.__all__ = set(LeonDSL.__members__.keys())

class ChatEnum(Enum):
	AI_LOCK_MSG = ""

	@classmethod
	def get_not_authenticate_msg(cls, id, user) -> str:
		return f"@{user}اکانتش ورفای نشده کونی " + "وریفای نشده." + "اکانتت" + f"@{id}"