from telegram import Update
from telegram.constants import ChatMemberStatus
from telegram.ext import ContextTypes

from ..bot import models
from ..core.type import Text
from ..botconfs import bot_settings


def is_bot(update: Update) -> bool:
	# If user is a bot request not valid
	return update.effective_user.is_bot

def is_link(update: Update) -> bool:
	entities = update.message.entities
	for entity in entities:
		if entity.type in bot_settings.Type.LINK:
			return True

	return Text.is_link(update.message.text)


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

def get_id_for_mention_user(update: Update, instance: models.BOT):
	name = update.effective_user.username
	if name is None:
		name = get_random_shit(ad=slash_t(2)) + instance.ai.stores.get(update.effective_user.id, None)
	else:
		name = "@" + name

	# None or not None
	return name


