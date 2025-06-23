import httpx
from telegram import Update


from django.conf import settings as django_settings


from ..bot import models
from ..core.type import Text
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
	def generate_ai_input(cls, role: str, content: str) -> dict:
		return {cls.ROLE: role, cls.CONTENT: content}

	@classmethod
	def generate_msg(
			cls,
			instance: models.BOT,
			user: Update.effective_user,
			message: str,
			request_in_group: bool
	):

		msgs = []
		if instance.deep:
			deep = cls.generate_ai_input(role=cls.SYSTEM_ROLE, content=instance.deep)
			msgs.append(deep)

		if request_in_group:
			group_stores = instance.stores
			msgs.extend(group_stores.comperes())


		if instance.msg_logs:
			msgs.extend(instance.get_msg_logs())

		text = Text.new(get_name(instance, user), message)
		msgs.append({ROLE: USER_ROLE, CONTENT: text})

		return (msgs, text)

	@classmethod
	async def new_request(cls, messages: list[dict], instance: models.BOT) -> str | None:

		data = {
			"model": instance.ai.active_model,
			"messages": messages,
		}

		ai_output = await cls.send_request(
			data=data,
			headers=cls.DEFAULT_HEADERS,
		)

		return ai_output


	async def send_request(cls, data: dict, headers: dict):

		async with httpx.AsyncClient() as client:
			response = await client.post(django_settings.API_ADDERS, headers=headers, json=data)

		if response.status_code == cls.SUCCESS_CODE:

			return response.json()["choices"][0]["message"]["content"]

		return None
