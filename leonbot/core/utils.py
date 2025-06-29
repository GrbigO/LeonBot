from telegram import Update, Message
from telegram.constants import MessageEntityType

from leonbot.ai.models import AISettings
from leonbot.bot.models import BOT
from leonbot.chat.utils import is_bot
from leonbot.botconfs import bot_settings


# For Any func this __file__
# If not `Message obj` in Update obj -> your app get a AttributeError
# use this funcs in location that Message obj in Update hast



def is_reply_to_me(update: Update) -> bool:
	# for spam
	if update.effective_user.is_bot:
		return False

	reply_to_msg = update.message.reply_to_message
	if reply_to_msg and reply_to_msg.from_user:
		return reply_to_msg.from_user.is_bot

	return False

# me == self-bot
def is_mention_me(message: Message) -> bool:
	mention = False
	if message.entities:
		for entity in message.entities:
			if entity.type == MessageEntityType.MENTION:
				mention_text = message.text[entity.offset:entity.offset + entity.length]
				if mention_text == bot_settings.BOT_USERNAME:
					mention = True
					break

	return mention


def is_request_in_group(update: Update) -> bool:
	return update.effective_chat.type in bot_settings.Type["GROUP"]


def is_request_in_pv(update: Update) -> bool:
	return update.effective_chat.type == bot_settings.Type["PV"]


def is_request_for_bot(message: Message, is_mentioned: bool) -> bool:
	list_text = message.text.split()
	if is_mentioned:
		if len(list(map(lambda x: x.strip(), list_text))) in bot_settings.CHOICE_CALL_BOT:
			return True

	if set(list_text) & bot_settings.REQUEST_NAME:
		return True

	return False


async def aget_or_create(telegram_id: int) -> tuple[BOT, bool]:
	telegram_id = str(telegram_id)
	try:
		created = False
		instance = await BOT.objects.select_related("ai").aget(telegram_id=telegram_id)
	except BOT.DoesNotExist:
		created = True
		ai_settings = await AISettings.objects.acreate()
		instance = await BOT.objects.acreate(telegram_id=telegram_id, ai=ai_settings)

	return (instance, created)

async def comperes_string(text: str) -> str:
	pass

def slash_t(x: int | None = None):
	return "\t" * x if x else "\t"


def slash_n(x: int | None = None):
	return "\n" * x if x else "\n"