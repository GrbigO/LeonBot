from telegram import Update
from telegram.constants import MessageEntityType

from leonbot.core.models import BOT
from leonbot.botconfs import bot_settings


def is_reply_to_bot(message: Update.message) -> bool:
	rtm = message.reply_to_message
	if rtm and rtm.from_user is not None:
		if rtm.from_user.is_bot:
			return True

	return False


def is_mention_bot(message: Update.message) -> bool:
	mention = False
	if message.entities:
		for entity in message.entities:
			if entity.type == MessageEntityType.MENTION:
				mention_text = message.text[entity.offset:entity.offset + entity.length]
				if mention_text == bot_settings.BOT_USERNAME:
					mention = True
					break

	return mention


def is_request_in_group(update: Update) -> bool:
	return update.effective_chat.type in bot_settings.Type.GROUP


def is_request_in_pv(update: Update) -> bool:
	return update.effective_chat.type == bot_settings.Type.PV


def is_request_for_bot(message: Update.message, is_mentioned: bool) -> bool:
	list_text = message.text.split()
	if is_mentioned:
		if len(list(map(lambda x: x.strip(), list_text))) == 1:
			return True

	if set(list_text) & bot_settings.REQUEST_NAME:
		return True

	return False

