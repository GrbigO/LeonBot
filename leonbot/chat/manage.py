from typing import Callable


from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from leonbot.account.manage import AccountManage
from leonbot.core import new_config, leon
from enums import ChatEnum

admin_cache = {}

class ChatManager:

	@classmethod
	@leon
	async def message_handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE, **kwargs):
		if update.message and kwargs["is_valid_request"]:
			chat_type = update.message.chat.type
			if chat_type in ["group"]:
				user_id = update.message.from_user.username
				user = AccountManage.get_user(user_id or update.message.from_user.id)
				if user is None:

					text = ChatEnum.not_autnthecate(id=user_id or update.message.from_user.full_name, user="Soroosh_80")

					await update.message.reply_text(reply_to_message_id=update.message.message_id, text=text)

				else:
					callback = await cls.parse_request()
					await callback()

	@classmethod
	async def parse_request(cls) -> Callable[[], ...]:
		return str

new_config(
	save_to="MessageHandler",
	code=MessageHandler(filters.TEXT & (~filters.COMMAND), ChatManager.message_handler)
)






