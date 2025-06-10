import httpx

from django.conf import settings as django_settings

from .models import AI
from ..account.models import User
from ..botconfs import bot_settings
from ..chat.utils import slash_n
from ..core.handlers import UpdateHandler
from ..core.request import UserRequest
from ..core.enums import BOTEnum

from .utils import (
	get_default_name,
	update_msg_log,
	user_not_auth_in_this_group,
)



class AIRequestHandler:


	ROLE = "role"
	CONTENT = "content"

	SYSTEM_ROLE = "system"
	USER_ROLE = "user"
	AI_ROLE = "assistant"

	DEFAULT_SETTINGS = {"reply_to_message_id": message.message_id}

	DEFAULT_HEADERS = {
		"Authorization":f"Bearer {django_settings.API_KEY}",
		"Content-Type":"application/json"
	}

	@classmethod
	def set_stores(cls, stores: dict):
		list_of_stores: list[dict] = []
		for user_name, user_store in stores.values():
			content = BOTEnum.IM.value + user_name + BOTEnum.DONT_CALL_ME.value + slash_n() + user_store
			list_of_stores.append(
				{
					cls.ROLE: cls.SYSTEM_ROLE,
					cls.CONTENT: content
				}
			)
		return list_of_stores



	@classmethod
	def generate_msg(cls, request: UserRequest):
		msgs = []
		instance: AI | User = request.instance
		user = request.metadata.effective_user
		name = get_default_name(user=user)

		if instance.deep:
			msgs.append({cls.ROLE: cls.SYSTEM_ROLE, cls.CONTENT: instance.deep})

		if request.in_group:

			if instance.stores.get(user.id) is None:
				request.funcs.append(user_not_auth_in_this_group)
			else:
				name = instance.stores[user.id][0]

			msgs.extend(cls.set_stores(instance.stores))


		if instance.msg_logs:
			msgs.extend(instance.get_msg_logs())

		text = f"{BOTEnum.IM.value + name + BOTEnum.DONT_CALL_ME.value},\n{request.message}"

		msgs.append({cls.ROLE: cls.USER_ROLE, cls.CONTENT: text})

		return (msgs, request)

	@classmethod
	async def new_request(cls, messages: list[dict], request: UserRequest) -> UserRequest:

		data = {
			"model": request.instance.active_model,
			"messages": messages,
		}

		ai_output = await cls.send_request(
			data=data,
			headers=cls.DEFAULT_HEADER,
		)

		request.funcs.append(update_msg_log)
		request.ai_output = ai_output

		return request


	@staticmethod
	async def send_request(data: dict, headers: dict):

		async with httpx.AsyncClient() as client:
			response = await client.post(django_settings.API_ADDERS, headers=headers, json=data)

		if response.status_code == 200:

			return response.json()["choices"][0]["message"]["content"]

		return None
