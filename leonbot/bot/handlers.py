from datetime import datetime, timedelta


from telegram import Update, Message, InlineKeyboardMarkup, BotCommandScopeChatMember
from telegram.ext import ContextTypes


from .buttons import Button
from .enums import BOTMassage




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
				text=BOTMassage.get_start_msg_shit(),
				reply_to_message_id=update.message.message_id,
				reply_markup=InlineKeyboardMarkup(buttons)
			)
		return

