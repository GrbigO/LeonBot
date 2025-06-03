from enum import Enum
from typing import Any


class Config(Enum):
	MessageHandler = []
	Conversation = []


async def leon(func):
	async def wrapper(*args, **kwargs):
		group_id = kwargs["update"].message.chat.id
		if group_id != settings.LEON_ID or kwargs["update"].message.for_user.is_bot:
			kwargs["is_valid_request"] = False

		else:
			kwargs["is_valid_request"] = True

		return await func(*args, **kwargs)

	return await wrapper


def new_config(save_to: str, code: Any) -> None:
	return