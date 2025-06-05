from typing import Any

from django.conf import settings as django_settings

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
	MessageHandler,
	filters,
	ContextTypes,
	ConversationHandler,
	CallbackQueryHandler,
)

from ..botconfs import bot_settings
from .dsl import LeonDSL

WITH = [200, 5000, 40000]
ACCEPT = [False, True]

class ChatManager:
	KEY_BOARD = [
		InlineKeyboardButton("help", callback_data="help")
	]
	MENTION_TYPE = "mention"

	@classmethod
	async def is_request_for_what(cls, message, context) -> Any:
		is_request_for_ai = False

		is_reply_to_bot = (
				message.reply_to_message and
				message.reply_to_message.from_user and
				message.reply_to_message.from_user.is_bot
		)

		is_mentioned = False
		if message.entities:
			for entity in message.entities:
				if entity.type == cls.MENTION_TYPE:
					mention_text = message.text[entity.offset:entity.offset + entity.length]
					if mention_text.lower() == bot_settings.BOT_USERNAME_LOWER:
						is_mentioned = True
						break

		if is_reply_to_bot or is_mentioned:
			is_request_for_ai = True

		text_split: list[str] = list(map(lambda x: x.strip().lower(), message.text.split()))
		set_text_split = set(text_split)

		if bot_settings.REQUEST_NAME.lower() in set_text_split:
			return (is_request_for_ai, django_settings.HOW_IM)

		elif set_text_split & LeonDSL.__all__:
			is_request_for_ai = False
			return (is_request_for_ai, text_split)

		else:
			# request for ai or not
			return (is_request_for_ai, None)

	@classmethod
	@valid_request
	async def message_handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):

		is_request_for_ai, text, message, context = await cls.is_valid_request(update.message, context)
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

	@classmethod
	async def start_bot(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
		reply_markup = InlineKeyboardMarkup([cls.KEY_BOARD])

		await update.message.reply_text(
			"",
			reply_to_message_id=update.message.message_id,
			reply_markup=reply_markup,
		)


HANDLERS = [
	MessageHandler(filters.TEXT & (~filters.COMMAND), ChatManager.message_handler),
	ConversationHandler(
		entry_points=[
			# CallbackQueryHandler(start_register, pattern="^start_register$"),
			# CallbackQueryHandler(handle_option1, pattern="^option1$"),
			# CallbackQueryHandler(handle_option2, pattern="^option2$"),
		],
		states={
			ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_name)],
			ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
		},
		fallbacks=[],
	)
]
