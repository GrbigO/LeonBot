from telegram import Update
from telegram.ext import (
	ContextTypes,
)

from .utils import is_bot, is_link
from leonbot.core.request import get_request, RequestContext
from ..ai.update import update_msg_log
from ..ai.utils import get_name
from ..core.handlers import bot_request_handler, ai_request_handler


class ChatHandler:

	@classmethod
	async def new_chat(cls, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
		if update.message is None:
			return
		elif is_bot(update.effective_user):
			return
		elif await is_link(update.message.entities, update.message.text):
			return

		request = await get_request(update, context)
		if request is None:
			return

		await cls.request_handler(request=request)

	@classmethod
	async def request_handler(cls, request: RequestContext) -> None:

		if request.for_bot:
			await bot_request_handler(request)

		elif request.for_ai:
			await ai_request_handler(request)

		else:
			# save for log
			new_log = get_name(request.instance, request.user) + " : "+ request.user_msg
			await update_msg_log(
				request.instance.ai,
				new_log,
				None,
			)

		return
