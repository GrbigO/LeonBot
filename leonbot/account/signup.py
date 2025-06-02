from telegram import Update
from telegram.ext import (
	ApplicationBuilder,
	CommandHandler,
	MessageHandler,
	ContextTypes,
	ConversationHandler,
	filters,
)

from ..botconf import new_config



class Signup:

	@staticmethod
	async def new_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
		await update.message.reply_text(
			"برای بررسی از صحت انسانیت شما اسم پایتخت کشور را تایپ کنید(تهران)",
			reply_to_message_id=update.message.message_id,
		)
		user = update.message.from_user
		new_msg = await update.message.text

		return None



new_config(
	save_to="Conversations",
	code=ConversationHandler(
		entry_points=[CommandHandler("signup", Signup.new_user)],
		states={Signup.__name__: [MessageHandler(filters.TEXT & ~filters.COMMAND, Signup.new_user)]},
		fallbacks=[CommandHandler("cancel", Signup.cancel)]),
)
