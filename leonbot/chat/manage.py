from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
	MessageHandler,
	filters,
	ContextTypes,
	ConversationHandler,
)

from .utils import is_valid_request
from ..ai.handlers import AIRequestHandler
from ..core.handlers import get_request
from ..core.request import UserRequest


class ChatManager:
	KEY_BOARD = [
		InlineKeyboardButton("help", callback_data="help")
	]



	@classmethod
	async def new_chat(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
		if is_valid_request(update.message):
			request: UserRequest = await get_request(update)

			if request is not None:

				await cls.request_handler(request)

		return

	@classmethod
	async def request_handler(cls, request: UserRequest):

		if request.for_bot:
			await cls.start_bot(update, context)

		elif request.for_ai:

			ai = AIRequestHandler
			data = ai.generate_msg(request)
			response = await ai.new_request(*data)

			if response.ai_output is not None:
				await update.message.reply_text(response.ai_output, **ai.DEFAULT_SETTINGS)

			for func in response.funcs:
				response = func(response)

			instance = response.instance
			if instance.updated_field:
				await instance.asave(update_fields=instance.updated_field)


	@classmethod
	async def start_bot(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
		reply_markup = InlineKeyboardMarkup([cls.KEY_BOARD])

		await update.message.reply_text(
			"",
			reply_to_message_id=update.message.message_id,
			reply_markup=reply_markup,
		)


HANDLERS = [
	MessageHandler(filters.TEXT & (~filters.COMMAND), ChatManager.request_handler),

	# ConversationHandler(
	# 	entry_points=[
	# CallbackQueryHandler(start_register, pattern="^start_register$"),
	# CallbackQueryHandler(handle_option1, pattern="^option1$"),
	# CallbackQueryHandler(handle_option2, pattern="^option2$"),
	# 	],
	# 	states={
	#
	# 	},
	# 	fallbacks=[],
	# )
]
