# No webhook just for test
# be careful. for use this option your PC or Any


if __name__ == "__main__":

	import asyncio
	import time
	import sys
	import os
	import django

	from django.conf import settings as django_settings
	from telegram.request import HTTPXRequest
	from telegram.ext import (
		ApplicationBuilder,
		CommandHandler,
		MessageHandler,
		CallbackQueryHandler,
		filters,
	)

	# First: Run Django
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leonbot.settings")
	django.setup()

	from .bot.queryhandlers import QueryHandler
	from .bot.handlers import ButtonHandler
	from .chat.manage import ChatHandler
	from .botconfs import bot_settings

	bot_settings(reload=True)

	print("build...")
	app = ApplicationBuilder().token(django_settings.TOKEN_BOT).build()
	print("build...done")
	print("set handler...\n")

	app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ChatHandler.new_chat))
	app.add_handler(CommandHandler("start", ButtonHandler.start))
	app.add_handler(CommandHandler("settings", ButtonHandler.settings))

	print("leon-bot is rdy for request...")

	if django_settings.DEBUG:
		def dev_mod_handler(_, context):
			print(context.error)
			sys.exit(1)

		app.add_error_handler(dev_mod_handler)
	app.run_polling()

