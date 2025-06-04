from enum import Enum
from typing import Any
from telegram.ext import ApplicationBuilder

import django
from django.conf import settings as django_settings

from leonbot.chat.manage import HANDLERS


# run bot
def run_bot():
	TOKEN = django_settings.TOKEN_BOT
	print("build...")
	app = ApplicationBuilder().token(TOKEN).build()
	print("build...done")
	print("set handler...\n")

	for handler in HANDLERS:
		print(handler)
		app.add_handler(handler)

	print("leon-bot is rdy for request...")
	try:
		app.run_polling()
	except Exception as e:
		print(e)

django.setup()
run_bot()