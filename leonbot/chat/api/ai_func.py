from leonbot.ai.models import AI



async def _settings_ai_(**kwargs):
	name = kwargs.get("name")
	text = ""

	if not name:
		for key, value in bot_settings.__dict__.items():
			text += f"{key}: {value}\n"

	else:
		try:
			ai_instance = await AI.objects.select_related("created_by").aget(name=name[0])
		except Exception as e:
			return "name if ai is not pida", {}

		text += f"name: {ai_instance.name}\n\n"

		text += f"store0: {ai_instance.description0}{await get_n(ai_instance.description0)}"
		text += f"store1: {ai_instance.description1}{await get_n(ai_instance.description1)}"
		text += f"store2: {ai_instance.description2}{await get_n(ai_instance.description2)}"
		text += f"store3: {ai_instance.description3}{await get_n(ai_instance.description3)}"

		text += f"created_who: {ai_instance.created_by.name}\n"
		text += f"updated_who: {ai_instance.created_by.name}"

	return (text, {})

ASK_NAME, ASK_STORE0, ASK_STORE1, ASK_STORE2, ASK_STORE3 = range(5)

async def _update_ai_(**kwargs):