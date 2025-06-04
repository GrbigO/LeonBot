from typing import Callable

from django.conf import settings as django_settings
from django.contrib.messages.context_processors import messages
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from leonbot.account.manage import AccountManager
from leonbot.chat.enums import LeonDSL, ChatEnum
from leonbot.core.validators import request_validator

admin = "@Soroosh_80"


def get_admin_name():
	global admin
	return admin


def set_admin_name(value):
	global admin
	admin = value


class ChatManager:

	@classmethod
	async def message_handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):

		if update.message:
			group_id = update.message.chat.id
			if group_id == django_settings.GROUP_ID and not update.message.from_user.is_bot:
				print(update.message.from_user.id)

				message = update.message

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
					new_text, settings = await LeonDSL.parse(update.message)
					if not new_text is None:
						await update.message.reply_text(text=new_text, **settings)

		# user_id = update.message.from_user.username
		# user = AccountManager.get_user(user_id or update.message.from_user.id)
		# if user is None:
		#
		# 	text = ChatEnum.get_not_authenticate_msg(
		# 		id=user_id or update.message.from_user.full_name,
		# 		user=get_admin_name()
		# 	)
		#
		# 	await update.message.reply_text(reply_to_message_id=update.message.message_id, text=text)
		#
		# if user.add_new:
		# 	set_admin_name(user.username)


HANDLERS = [
	MessageHandler(filters.TEXT & (~filters.COMMAND), ChatManager.message_handler)
]