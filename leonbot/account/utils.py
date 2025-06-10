async def user_to_text(users):
	text = None
	for user in users:
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

async def get_user(user_id: int, username: str):
	return await User.objects.filter(id=user_id).afirst()



