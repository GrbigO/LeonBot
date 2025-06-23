from typing import Optional

from telegram import Update
from telegram.ext import ContextTypes

from leonbot.core.models import BOT
from leonbot.ai.handlers import AIRequestHandler
from .context import RequestContext
from .utils import (
	is_request_for_bot,
	is_request_in_group,
	is_request_in_pv,
	is_mention_bot,
	is_reply_to_bot,
)

MENTION_OR_NOT: bool = False


async def get_request(
		update: Update,
		c0ntext: ContextTypes.DEFAULT_TYPE
) -> Optional[RequestContext]:

	global MENTION_OR_NOT

	is_mentioned = is_mentioned_bot(update.message)
	request_for_bot = is_request_for_bot(update.message, is_mentioned)
	request_for_ai = is_mentioned or is_reply_to_bot(update.message)
	request_in_group = is_request_in_group(update)
	request_in_pv = is_request_in_pv(update)

	if request_in_group:
		id = update.effective_chat.id

	elif request_in_pv:
		id = update.effective_user.id

	else:
		# if not send message for bot in pv or group return `None`
		return

	instance, created = await BOT.objects.aget_or_create(id=id)

	request = RequestContext(
		is_request_for_bot=request_for_bot,
		is_request_for_ai=request_for_ai,
		is_request_in_group=request_in_group,
		is_request_in_pv=request_in_pv,
		first_use=created,
		instance=instance,
		update=update,
		context=c0ntext,
	)

	if MENTION_OR_NOT:
		request.mention_user = True

	MENTION_OR_NOT = not MENTION_OR_NOT

	return request