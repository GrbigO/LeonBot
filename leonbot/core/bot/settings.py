import json
from django.conf import settings


def _bot_settings():
	with open(settings.BOT_SETTING_PATH, "r", encoding="utf-8") as file:
		data = json.load(file)
		_bot_settings.IS_AI_LOCK = data["IS_AI_LOCK"]
		_bot_settings.AI_URL = data["AI_URL"]
		_bot_settings.AI_IDS = data["AI_IDS"]
		_bot_settings.AI_ID = data["AI_ID"]
		_bot_settings.GangBang = data["Gang_Bang"]
		_bot_settings.ACTIVE_MODEL = data["ACTIVE_MODEL"]
		_bot_settings.DEFAULT_MODEL = data["DEFAULT_MODEL"]

	return _bot_settings


bot_settings = _bot_settings()
