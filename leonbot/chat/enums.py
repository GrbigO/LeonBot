from typing import Optional

from enum import Enum


from ..ai.manage import AIManager
from ..core.bot.settings import bot_settings
from .api.func import __func__ as __work_func__


class LeonDSL(Enum):
	about = None
	delete = None
	add = None
	update = None
	model = None
	train = None
	user = None
	perm = None
	settings = None
	ai = None

	__msg_for = None
	__bug = None
	__restart = None

	@classmethod
	async def _parse_code(cls, code, message) -> tuple[Optional[str], dict]:
		prmtrs = []
		func_name = "_"
		for name in code:
			if name.startswith("-"):
				prmtrs.append(name[1:])

			name = name.lower()

			if not name in cls.__all__:
				del name

			else:
				func_name = func_name + name + "_"

		print(func_name)
		func = cls.__func__.get(func_name.strip())
		if func is None:
			return None, {}
		return await func(message=message, name=prmtrs)

	@classmethod
	async def parse(cls, message, code=None) -> tuple[Optional[str], dict]:
		if code is None:
			code = list(map(lambda x: x.lower(), message.text.split()))

			if not set(code) & cls.__all__:
				if bot_settings.IS_AI_LOCK:
					return ChatEnum.AI_LOCK_MSG.value , {"reply_to_message_id": message.message_id}
				return await AIManager.new_request(message)

		return await cls._parse_code(code, message)


LeonDSL.__all__ = set(LeonDSL.__members__.keys())
LeonDSL.__func__ = __work_func__


