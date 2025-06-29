from django.conf import settings
from django.db.utils import ProgrammingError

from .bot.models import BOT


def __bot_settings(reload: bool = False, **kwargs):
	def ai_settings():
		telegram_id = "1"
		try:
			mybot = BOT.objects.select_related("ai").get(telegram_id=telegram_id)
		except BOT.DoesNotExist:
			raise ProgrammingError(
				"you must use this command -> python .\\manage.py initial\n"
				"If you use this packig and not config your bot go read README.bot_settings"
			)

		for name, brain in mybot.settings.items():
			setattr(ai_settings, name, brain)

		ai_settings.active_model = mybot.ai.active_model
		return ai_settings

	if reload is True:

		__bot_settings.ai = ai_settings()

		__bot_settings.CHOICE_CALL_BOT = (1, 2)

		__bot_settings.BOT_USERNAME = settings.BOT["USERNAME"]
		__bot_settings.REQUEST_NAME = set(settings.BOT["REQUEST_NAME"])
		__bot_settings.GROUP_MAX_LENGTH = settings.BOT["GROUP_MAX_LENGTH"]
		__bot_settings.MAX_MSG_LOGS = settings.BOT["MAX_MSG_LOGS"]

		__bot_settings.Type = {
			"GROUP": ("supergroup", "group"),
			"LINK": ("url", "text_link"),
			"PV": "private"
		}

	# Return self func for reset attrs.
	# If you call `bot_settings()` reset __all__ attribute.
	# this option for update bot_settings and add new attr for bot_settings.
	global bot_settings
	bot_settings = __bot_settings

	return __bot_settings

bot_settings = __bot_settings
