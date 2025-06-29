from telegram import Update


from .handlers import AIRequestHandler
from .models import AISettings
from ..core.utils import comperes_string


async def update_msg_log(
		instance: AISettings,
		new_log: str,
		ai_output: str | None,
) -> None:

	ai = AIRequestHandler
	new_log = ai.new_ai_input(role=ai.USER_ROLE, content=new_log)
	instance.new_log(new_log)

	if ai_output:
		ai_output = ai.new_ai_input(role=ai.AI_ROLE, content=ai_output)
		instance.new_log(ai_output)


	await instance.asave(update_fields=["msg_logs"])

	return