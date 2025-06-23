# no webhook just for test


if __name__ == "__main__":
	import os
	import django

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leonbot.settings")
	django.setup()

	from telegram.ext import (
		ApplicationBuilder,
		CommandHandler,
		MessageHandler,
		CallbackQueryHandler,
		filters,
	)
	from .botconfs import bot_settings
	from leonbot.bot.handlers import ButtonHandler
	from .chat.manage import ChatHandler

	# run bot
	print("build...")
	app = ApplicationBuilder().token(bot_settings.TOKEN_BOT).build()
	print("build...done")
	print("set handler...\n")

	app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ChatHandler.new_chat))
	app.add_handler(CommandHandler("start", ButtonHandler.start))
	app.add_handler(CommandHandler("settings", ButtonHandler.settings))
	app.add_handler(CallbackQueryHandler(ButtonHandler.button_handler))

	print("leon-bot is rdy for request...")

	app.run_polling()
