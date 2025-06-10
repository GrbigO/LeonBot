from telegram import Update

from ..botconfs import bot_settings
from ..account.models import User
from ..ai.models import AI


def is_reply_to_bot(message: Update.message) -> bool:
	return (
			message.reply_to_message and
			message.reply_to_message.from_user and
			message.reply_to_message.from_user.is_bot
	)


def is_mentioned_bot(message: Update.message) -> bool:
	mention = False
	if message.entities:
		for entity in message.entities:
			if entity.type == bot_settings.MENTION_TYPE:
				mention_text = message.text[entity.offset:entity.offset + entity.length]
				if mention_text == bot_settings.BOT_USERNAME:
					mention = True
					break

	return mention


def is_request_in_group(update: Update) -> bool:
	return update.effective_chat.type in bot_settings.GROUP_TYPE


def is_request_in_pv(update: Update) -> bool:
	return update.effective_chat.type in bot_settings.PV_TYPE


def is_request_for_bot(message: Update.message, is_mentioned: bool) -> bool:
	if len(message.text) < bot_settings.MAX_LENGTH_FOR_CALL_BOT:
		list_text = message.text.split()
		if is_mentioned:
			if len(list(map(lambda x: x.strip(), list_text))) == 1:
				return True

		if set(list_text) & bot_settings.REQUEST_NAME:
			return True

	return False


async def aget_or_create(update: Update, model, is_ai_model: bool) -> AI | User:
	if is_ai_model:
		id = update.effective_chat.id
	else:
		id = update.effective_user.id


	instance = await model.objects.aget_or_create(id=id)

	return instance[0]
