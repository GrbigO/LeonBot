import httpx

from django.conf import settings as django_settings

from .models import AI
from leonbot.botconfs import bot_settings
from ..account.models import User


CACHE_AIMODEL: dict[int, AI] | dict = {}

class AIRequestHandler:



	SYSTEM_ROLE = "system"
	USER_ROLE = "user"
	AI_ROLE = "assistant"

	content_type = "application/json"

	@classmethod
	async def load_aimodel(cls, chat_id: int):
		global CACHE_AIMODEL
		aimodel = cls.CACHE_AIMODEL.get(chat_id, None)

		if not aimodel:
			try:
				aimodel = await AI.objects.aget(chat_id=chat_id)
			except AI.DoesNotExist:
				pass

			else:
				cls.CACHE_AIMODEL.update({chat_id: aimodel})

		return aimodel

	@classmethod
	async def generate_msg(cls, text, chat_id, aimodel: AI, user_name=None):
		msg = []
		if aimodel.STORES_CACHE is None:
			for key, value in aimodel.stores:
				msg.append({"role": cls.SYSTEM_ROLE, "content": key + " " + value})
			aimodel.STORES_CACHE = msg
			cls.CACHE_AIMODEL[chat_id] = aimodel
		else:
			msg.extend(aimodel.STORES_CACHE)

		msg.extend(aimodel.msg_log)

		text = text if user_name is None else f"im {user_name},\n{text}"

		msg.append({"role": cls.USER_ROLE, "content": text})

		return msg

	@classmethod
	async def new_request(cls, message) -> tuple[Optional[str], dict]:

		chat_id = message.chat.id
		aimodel = cls.load_aimodel(chat_id)

		if aimodel is None:
			return "", {}

		# user input
		text = message.text

		headers = {
			"Authorization": f"Bearer {django_settings.API_KEY}",
			"Content-Type": cls.content_type,
		}

		try:
			user_name = await User.objects.aget(id=message.from_user.id).name
		except (User.DoesNotExist, AttributeError):
			user_name = f"{message.from_user.full_name + " dog"}"

		messages = await cls.generate_msg(text, chat_id, aimodel, user_name)
		data = {
			# "model": cls.AIMODEL[0].ai_models.get(bot_settings.ACTIVE_MODEL, bot_settings.DEFAULT_MODEL),
			"model": aimodel.active_model,
			"messages": messages,
		}
		try:
			async with httpx.AsyncClient() as client:
				response = await client.post(bot_settings.AI_URL, headers=headers, json=data)
		except Exception as e:
			return None, {}

		if response.status_code == 200:
			ai_output = response.json()["choices"][0]["message"]["content"]

			return (ai_output, {"reply_to_message_id": message.message_id})
		else:
			print("bug")
			print(response.json())
			return "!bug from ostad", {}
