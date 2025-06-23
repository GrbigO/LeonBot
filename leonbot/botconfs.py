from django.conf import settings
from .core.emojis import get_emoji


async def __set_request() -> None:
	bot_settings.REQ_PER += 1


def bot_settings():
	if getattr(bot_settings, "REGISTER", False):
		raise ValueError("Bot settings already registered")

	bot_settings.REQ_PER = 0
	bot_settings.HANDLE_REQ = property(__set_request, lambda x: None)


	data = settings.BOT_SETTINGS
	bot_settings.TOKEN_BOT = data["TOKEN_BOT"]
	bot_settings.BOT_USERNAME = data["USERNAME"]
	bot_settings.REQUEST_NAME = data["REQUEST_NAME"]
	bot_settings.GROUP_MAX_LENGTH = data["GROUP_MAX_LENGTH"]
	bot_settings.START_MSG = property(lambda: data["START_MSG"] + get_emoji())

	bot_settings.Type = lambda : bot_settings.Type.__dict__
	bot_settings.Type.GROUP = ("supergroup", "group")
	bot_settings.Type.LINK = ("url", "text_link")
	bot_settings.Type.PV = "private"


	bot_settings.REGISTER = True
	# Return self func for reset attrs.
	# If you call again `bot_settings` reset __all__ attribute.
	return bot_settings

bot_settings = bot_settings()
