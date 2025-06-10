from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from leonbot.botconfs import bot_settings


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text("", reply_to_message_id=update.message.message_id)


async def cancel_command(update, context):
	await update.message.reply_text(bot_settings.CANCEL_MSG, reply_to_message_id=update.message.message_id)
	return ConversationHandler.END