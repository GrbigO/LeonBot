from datetime import datetime, timedelta


from telegram import Update, Message, InlineKeyboardMarkup
from telegram.ext import ContextTypes


from .buttons import Button
from ..botconfs import bot_settings





class ButtonHandler:

	@classmethod
	def start(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
		raise NotImplementedError

	@classmethod
	def start_by_name(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
		raise NotImplementedError

	@classmethod
	async def settings(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
		buttons = Button.get_buttons(update)
		await update.message.reply_text(
				text=bot_settings.CALL(bot_settings.START_MSG),
				reply_to_message_id=update.message.message_id,
				reply_markup=InlineKeyboardMarkup(buttons)
			)
		return

