from telegram import Update


from .handlers import AIRequestHandler
from ..bot.models import BOT
from ..core.type import Text



async def update_msg_log(
		instance: BOT,
		new_log: str,
		ai_output: str | None
) -> None:

	ai = AIRequestHandler
	comperes_new_log = await Text.comperes_string(new_log)
	new_log = ai.generate_ai_input(role=ai.USER_ROLE, content=comperes_new_log)
	instance.add_new_log(new_log)

	if ai_output is not None:
		comperes_ai_output = Text.comperes_string(ai_output)
		ai_output = ai.generate_ai_input(role=ai.AI_ROLE, content=comperes_ai_output)
		instance.add_new_log(ai_output)


	await instance.asave(update_fields=["msg_logs"])

	return

