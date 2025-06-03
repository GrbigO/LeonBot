

async def request_validator(func):
	async def wrapper(*args, **kwargs):
		if kwargs["update"].message:
			group_id = kwargs["update"].message.chat.id
			if (
					group_id == settings.LEON_ID
					and not kwargs["update"].message.for_user.is_bot
			):
				await func(*args, **kwargs)


	return await wrapper