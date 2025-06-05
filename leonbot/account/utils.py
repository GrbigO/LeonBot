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