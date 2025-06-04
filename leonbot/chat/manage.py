import time
from typing import Any

from django.conf import settings as django_settings


from telegram import Update
from telegram.ext import (
	ApplicationBuilder,
	MessageHandler,
	filters,
	ContextTypes,
	CommandHandler,
)

from ..account.manage import AccountManager
from .enums import LeonDSL
from .commands import help_command
from ..core.bot.settings import bot_settings

admin = "@Soroosh_80"


def get_admin_name():
	global admin
	return admin


def set_admin_name(value):
	global admin
	admin = value


class ChatManager:

	@classmethod
	async def is_valid_request(cls, message, context) -> Any:
		if message:
			group_id = message.chat.id
			if group_id == django_settings.GROUP_ID and not message.from_user.is_bot:

				print(message.from_user.id)

				is_reply_to_bot = (
						message.reply_to_message and
						message.reply_to_message.from_user and
						message.reply_to_message.from_user.is_bot
				)

				is_mentioned = False
				if message.entities:
					for entity in message.entities:
						if entity.type == 'mention':
							mention_text = message.text[entity.offset:entity.offset + entity.length]
							if mention_text.lower() == f"@{context.bot.username.lower()}":
								is_mentioned = True
								break
				if is_reply_to_bot or is_mentioned:
					return (True, None)

				splx = message.text.split()

				if "سگ" in splx:
					return (False, django_settings.HOW_IM)

				if set(splx) & LeonDSL.__all__:
					return (True, splx)
		return (False, None)

	@classmethod
	async def message_handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
		is_valid, msg = await cls.is_valid_request(update.message, context)
		if not is_valid and msg:
			await update.message.reply_text(text=msg, reply_to_message_id=update.message.message_id)

		elif is_valid:
			# valid request
			if msg:
				new_text, settings = await LeonDSL.parse(update.message, msg)
			else:
				new_text, settings = await LeonDSL.parse(update.message)

			if not new_text is None:
				await update.message.reply_text(text=new_text, **settings)



HANDLERS = [
	MessageHandler(filters.TEXT & (~filters.COMMAND), ChatManager.message_handler),
	CommandHandler("help", help_command),
]
