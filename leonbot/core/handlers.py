from telegram import Update

from ..ai.models import AI
from ..account.models import User
from .request import UserRequest
from .utils import (
	is_request_for_bot,
	is_request_for_ai,
	is_request_in_group,
	is_request_in_pv,
	is_mentioned_bot,
	is_reply_to_bot,
	aget_or_create,
)
from ..botconfs import bot_settings




async def get_request(update: Update) -> UserRequest | None:
	is_mentioned = is_mentioned_bot(update.message)

	request_for_bot = is_request_for_bot(update.message, is_mentioned)


	request_for_ai = is_mentioned or is_reply_to_bot(update.message)

	request_in_group = is_request_in_group(update)
	request_in_pv = is_request_in_pv(update)

	model: AI | User | None = None
	if request_in_group and request_for_ai:
		model = AI
		is_ai_model = True

	elif request_in_pv:
		model = User
		is_ai_model = False

	else:
		# if not send message for bot in pv or group return `None`
		return model

	instance = await aget_or_create(update, model, is_ai_model)

	if request_for_bot:
		return UserRequest(
			request_for_bot=request_for_bot,
			instance=instance,
		)

	return UserRequest(
		request_for_ai=request_for_ai,
		request_in_pv=request_in_pv,
		request_in_group=request_in_group,
		message=update.message.text,
		instance=instance,
		metadata=update,
	)




