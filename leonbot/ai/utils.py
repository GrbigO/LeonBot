from telegram import Update

from .handlers import AIRequestHandler
from ..botconfs import bot_settings
from ..core.request import UserRequest


def get_default_name(user: Update.effective_user) -> str:
	return user.full_name or user.username or ""


def user_not_auth_in_this_group(request: UserRequest):
	instance = request.instance
	key = request.metadata.effective_user.id
	name = get_default_name(request.metadata.effective_user)

	store = bot_settings.GET_RANDOM_STORE(name)

	values = (name, store)

	instance.stores.update({key: values})
	instance.updated_field.append("stores")
	return request


def update_msg_log(request: UserRequest):
	instance = request.instance
	instance.msg_logs.append(
		{
			AIRequestHandler.ROLE: AIRequestHandler.USER_ROLE,
			AIRequestHandler.CONTENT: request.message
		}
	)

	if request.ai_output is not None:
		instance.msg_logs.append(
			{
				AIRequestHandler.ROLE: AIRequestHandler.AI_ROLE,
				AIRequestHandler.CONTENT: request.ai_output,
			}
		)

	instance.updated_field.append("msg_logs")
	return instance
