from telegram import Update, User, Message
from telegram.ext import ContextTypes

from leonbot.bot import models


class RequestContext:
	__slots__ = (
		"for_bot",
		"for_ai",
		"in_pv",
		"in_group",
		"instance",
		"update",
		"context",
		"mention_user",
		"first_use",
	)

	def __init__(
			self,
			is_request_for_bot: bool | None = None,
			is_request_for_ai: bool | None = None,
			is_request_in_pv: bool | None = None,
			is_request_in_group: bool | None = None,
			first_use: bool = False,
			instance: models.BOT | None = None,
			update: Update | None = None,
			context: ContextTypes.DEFAULT_TYPE | None = None,
	):
		self.for_bot: bool | None = is_request_for_bot
		self.for_ai: bool | None = is_request_for_ai
		self.in_pv: bool | None = is_request_in_pv
		self.in_group: bool | None = is_request_in_group
		self.instance: BOT | None = instance
		self.update: Update | None = update
		self.context: ContextTypes.DEFAULT_TYPE = context

		self.first_use = first_use
		self.mention_user: bool = False

	@property
	def user(self) -> User:
		return self.update.effective_user

	@property
	def user_msg(self) -> Message:
		return self.update.message.text

