from telegram import Update
from telegram.ext import ContextTypes

from leonbot.botconfs import bot_settings




async def set_valid_request(message: Update.message):
	if message:
		# If user is a bot request not valid
		return not message.from_user.is_bot

	return False


async def is_user_admin_from_this_group(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    member = await context.bot.get_chat_member(chat_id, user_id)

    if member.status in ['administrator', 'creator']:
        return True
    return False


async def slash_t(x: int | None = None):
	return "\t" * x if x else "\t"


async def slash_n(x: int | None = None):
	return "\n" * x if x else "\n"


async def get_emoji(name=None):
	emojis = {
		1: "🥹", 2: "🤬", 3: "😤", 4: "🫠", 5: "😾",
		6: "🤢", 7: "🤮", 8: "👹", 9: "🤰🏿", 10: "🎅🏿",
		11: "👵🏿", 12: "🥶"
	}
	# for fun
	if name and name in bot_settings.DOG_USER:
		index = 9

	else:
		index = random.randint(1, 12)

	return emojis[index]
