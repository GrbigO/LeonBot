from typing import Callable
import hashlib

from django.conf import settings

from .bot.models import BOT
from .core.emojis import get_emoji

REQ_PER = 0


def __set_request() -> None:
	global REQ_PER
	REQ_PER += 1


def __callback_caller(callback: Callable[..., ...]):
	return callback()


async def bot_settings(init: bool = False, **kwargs):

	if init is True:
		bot_settings.HANDLE_REQ = __set_request
		bot_settings.CHOICE_CALL_BOT = (1, 2)
		bot_settings.CALL = __callback_caller


		bot_settings.BOT_USERNAME = settings.BOT_SETTINGS["USERNAME"]
		bot_settings.REQUEST_NAME = settings.BOT_SETTINGS["REQUEST_NAME"]
		bot_settings.GROUP_MAX_LENGTH = settings.BOT_SETTINGS["GROUP_MAX_LENGTH"]
		bot_settings.START_MSG = lambda: settings.BOT_SETTINGS["START_MSG"] + get_emoji()

		bot_settings.Type = {
			"GROUP": ("supergroup", "group"),
			"PV": "private",
			"LINK": ("url", "text_link"),
		}

	# Return self func for reset attrs.
	# If you call again `bot_settings` reset __all__ attribute.
	# this option for update settings and plugins.
	return bot_settings

