from typing import Union

import httpx
from telegram import Update


from django.conf import settings as django_settings

from ..bot.enums import BOTBrain
from ..botconfs import bot_settings
from ..bot import models
from .utils import get_name


class AIRequestHandler:

	DEFAULT_HEADERS = {
		"Authorization":f"Bearer {django_settings.API_KEY}",
		"Content-Type":"application/json"
	}
	SUCCESS_CODE = 200

	ROLE = "role"
	CONTENT = "content"

	SYSTEM_ROLE = "system"
	USER_ROLE = "user"
	AI_ROLE = "assistant"


	@classmethod
	def new_ai_input(cls, role: str, content: str) -> dict:
		return {cls.ROLE: role, cls.CONTENT: content}

	@classmethod
	def generate_msg(
			cls,
			instance: models.BOT,
			user: Update.effective_user,
			message: str,
			request_in_group: bool
	) -> tuple[list[dict], str]:

		msgs: list[dict] = []

		msgs.append(cls.new_ai_input(role=cls.SYSTEM_ROLE, content=BOTBrain.get_base_brain()))

		if instance.ai.deep:
			deep = cls.new_ai_input(role=cls.SYSTEM_ROLE, content=instance.deep)
			msgs.append(deep)

		if request_in_group:
			for store in instance.ai.generate_stores():
				msgs.append(cls.new_ai_input(role=cls.SYSTEM_ROLE, content=store))


		if instance.ai.msg_logs:
			msgs.extend(instance.ai.get_msg_logs())

		text = get_name(instance, user) + " : " + message
		msgs.append(cls.new_ai_input(role=cls.USER_ROLE, content=text))

		return (msgs, text)

	@classmethod
	async def new_request(cls, messages: list[dict], instance: Union[models.BOT, bot_settings]) -> str | None:

		data = {
			"model": "deepseek/deepseek-chat-v3-0324:free",
			"messages": messages,
			"max_tokens": 50,
		}

		ai_output = await cls.send_request(
			data=data,
			headers=cls.DEFAULT_HEADERS,
		)

		return ai_output

	@classmethod
	async def send_request(cls, data: dict, headers: dict):
		async with httpx.AsyncClient(timeout=30.0) as client:
			response = await client.post(django_settings.API_ADDERS, headers=headers, json=data)

		if response.status_code == cls.SUCCESS_CODE:

			return response.json()["choices"][0]["message"]["content"]

		return None
