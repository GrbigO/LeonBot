from telegram import Update, User, MessageEntity
from telegram.constants import ChatMemberStatus
from telegram.ext import ContextTypes


from django.utils.functional import empty


from ..ai.handlers import AIRequestHandler
from ..bot import models
from ..core.type import is_bool
from ..botconfs import bot_settings


def is_bot(user: User) -> bool:
	# If user is a bot request not valid
	return user.is_bot

async def is_link(message_entities: list[MessageEntity], message_text: str) -> bool:
	for entity in message_entities:
		if entity.type in bot_settings.Type["LINK"]:
			return True

	return False
	# ai = AIRequestHandler
	# ai_output = await ai.new_request(
	# 	messages=[brain3164, ai.new_ai_input(ai.USER_ROLE, message_text)],
	# 	instance=bot_settings
	# )
	# is_valid = is_bool(ai_output)
	# if is_valid is empty:
	# 	# lol if empty im ban user-request for 2 min
	# 	# bucausse brain3164 handle chiat
	# 	pass
	#
	# return is_valid


async def get_chat_member(update: Update):
	chat_id = update.effective_chat.id
	user_id = update.effective_user.id

	return await context.bot.get_chat_member(chat_id, user_id)


async def is_admin_from_this_group(update: Update) -> bool:
	user = await get_chat_member(update)

	if user.status == ChatMemberStatus.ADMINISTRATOR:
		return True

	elif user.status == ChatMemberStatus.OWNER:
		return True

	return False


async def is_default_member_in_this_group(update: Update) -> bool:
	user = await get_chat_member(update)

	if user.status == ChatMemberStatus.MEMBER:
		return True

	elif user.status == ChatMemberStatus.ADMINISTRATOR:
		return True

	elif user.status == ChatMemberStatus.OWNER:
		return True

	return False

def get_id_user(update: Update, instance: models.BOT):
	name = update.effective_user.username
	if name is None:
		name = get_random_shit(ad=slash_t(2)) + instance.ai.stores.get(update.effective_user.id, None)
	else:
		name = "@" + name

	# None or not None
	return name


