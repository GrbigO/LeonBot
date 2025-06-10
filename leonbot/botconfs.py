from django.conf import settings


def _bot_settings():
	data = settings.BOT_SETTINGS
	_bot_settings.IS_AI_LOCK = data["IS_LOCK"]
	_bot_settings.AI_URL = data["AI_URL"]
	_bot_settings.AI_IDS = data["AI_IDS"]
	_bot_settings.AI_ID = data["AI_ID"]
	_bot_settings.GangBang = data["Gang_Bang"]
	_bot_settings.ACTIVE_MODEL = data["ACTIVE_MODEL"]
	_bot_settings.DEFAULT_MODEL = data["DEFAULT_MODEL"]
	_bot_settings.CANCEL_MSG = data["CANCEL_MSG"]
	_bot_settings.REQUEST_NAME = data["REQUEST_NAME"]


	return _bot_settings

bot_settings = _bot_settings()
