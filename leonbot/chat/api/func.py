import random
from asgiref.sync import sync_to_async

from django.forms import model_to_dict
from django.conf import settings

from leonbot.ai.models import AI
from leonbot.account.models import User
from leonbot.core.bot.settings import bot_settings


async def get_emoje(name=None):
	_ = {
		1: "🥹", 2: "🤬", 3: "😤", 4: "🫠", 5: "😾",
		6: "🤢", 7: "🤮", 8: "👹", 9: "🤰🏿", 10: "🎅🏿",
		11: "👵🏿", 12: "🥶"
	}
	if name and name in settings.BAD_USER:
		index = 9

	else:
		index = random.randint(1, 12)

	return _[index]


async def tab(x):
	return "\t" * x


async def n(x):
	return "\n" * x




async def user_to_text(users_):
	text = None
	for user in users_:
		if text is None:
			text = (
				f"name: {user.name}{await tab(2)}"
				f"id: {user.username}{await tab(2)} {await get_emoje(user.name)}{await n(2)}"
			)
		else:
			text = (
					text +
					f"name: {user.name}{await tab(2)}"
					f"id: {user.username}{await tab(2)} {await get_emoje(user.name)}{await n(2)}"
			)

	return text

# for cache
users = None

async def _user_(**kwargs):
	global users
	if users is None:
		users = await sync_to_async(lambda: list(User.objects.all()))()

	users = await user_to_text(users)

	return (users, {})

# for cache
settings_ai = None


async def get_n(value):
	if isinstance(value, str) and len(value) > 100:
		slash_n = "\n" + await get_emoje() + await n(4)
	else:
		slash_n = await n(2)
	return slash_n

async def _settings_ai_(**kwargs):
	name = kwargs.get("name")
	text = ""
	print(name)
	if not name:
		for key, value in bot_settings.__dict__.items():
			text += f"{key}: {value}\n"

	else:
		try:
			ai_instance = await AI.objects.select_related("created_by").aget(name=name[0])
		except Exception as e:
			return "name if ai is not pida", {}

		text += f"name: {ai_instance.name}\n\n"

		text += f"store0: {ai_instance.description0}{await get_n(ai_instance.description0)}"
		text += f"store1: {ai_instance.description1}{await get_n(ai_instance.description1)}"
		text += f"store2: {ai_instance.description2}{await get_n(ai_instance.description2)}"
		text += f"store3: {ai_instance.description3}{await get_n(ai_instance.description3)}"

		text += f"created_who: {ai_instance.created_by.name}\n"
		text += f"updated_who: {ai_instance.created_by.name}"

	return (text, {})


def _delete_user_(**kwargs):
	pass


__func__ = {
	_user_.__name__: _user_,
	_settings_ai_.__name__: _settings_ai_,
}
