import httpx
import asyncio
from typing import Optional

from . import models
from ..core.bot.settings import bot_settings
from ..account.models import User

class AIManager:
	LOAD: bool = False
	API_KEY = None
	AIMODEL: list[models.AI] = None

	# role
	system = "system"
	user = "user"
	assistant = "assistant"

	content_type = "application/json"

	@classmethod
	def gang_bang_loder(cls):
		pass

	@classmethod
	async def load_aimodel(cls):
		if bot_settings.GangBang:
			cls.AIMODEL = await models.AI.objects.ain_bulk(bot_settings.ai_ids).values()
			cls.gang_bang_loder()
		else:
			cls.AIMODEL = [await models.AI.objects.aget(name=bot_settings.AI_ID)]
			cls.API_KEY = cls.AIMODEL[0].key

	@classmethod
	async def generate_msg(cls, text, user_name= None):
		msg = None
		if bot_settings.GangBang:
			pass

		else:
			msg = []
			descriptions = cls.AIMODEL[0].get_description()
			if descriptions:
				for system_text in descriptions:
					msg.append({"role": cls.system, "content": system_text})

			else:
				print(
					"!bug\n"
					f"model we dont have description\ncreated_by: {cls.AIMODEL[0].created_by}"
				)
			msg.append({"role": cls.user, "content": text})

		return msg

	@classmethod
	async def new_request(cls, message) -> tuple[Optional[str], dict]:
		if not cls.LOAD:
			await cls.load_aimodel()
			cls.LOAD = True

		text = message.text

		headers = {
			"Authorization": f"Bearer {cls.API_KEY}",
			"Content-Type": cls.content_type,
		}
		try:
			username = message.from_user.id
			user = await User.objects.aget(username=username)
		except User.DoesNotExist:
			user = None
		data = {
			# "model": cls.AIMODEL[0].ai_models.get(bot_settings.ACTIVE_MODEL, bot_settings.DEFAULT_MODEL),
			"model": "deepseek/deepseek-chat-v3-0324",
			"messages": await cls.generate_msg(text, user.name if not user is None else None),
		}
		try:
			async with httpx.AsyncClient() as client:
				response = await client.post(bot_settings.AI_URL, headers=headers, json=data)
		except Exception as e:
			return None, {}

		if response.status_code == 200:
			content_raw = response.json()["choices"][0]["message"]["content"]
			new_text = content_raw

			return (new_text, {"reply_to_message_id": message.message_id})
		else:
			print("bug")
			print(response.json())
			return "!bug from ostad", {}
