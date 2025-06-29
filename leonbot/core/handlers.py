from ..bot.handlers import ButtonHandler
from ..ai.handlers import AIRequestHandler
from ..ai.update import update_msg_log
from ..chat.utils import get_id_user
from ..core.request import RequestContext
from ..core.utils import slash_n




async def bot_request_handler(request: RequestContext) -> None:
	# if request.first_use:
		await ButtonHandler.settings(request.update, request.context)
	# else:
	# 	await ButtonHandler.start_by_name(request.update, request.context)



async def ai_request_handler(request: RequestContext) -> None:

	ai = AIRequestHandler

	messages, refactor_user_msg = ai.generate_msg(
		instance=request.instance,
		user=request.user,
		message=request.user_msg,
		request_in_group=request.in_group
	)

	ai_output = await ai.new_request(messages, request.instance)

	if ai_output:
		name = None
		if request.mention_user:
			name = get_id_user(request.update, request.instance)

		ai_output = ai_output.replace("**", "").replace("*", "")
		await request.update.message.reply_text(
			ai_output if name is None
			else name + slash_n() + ai_output,
			reply_to_message_id=request.update.message.message_id
		)

	await update_msg_log(
		instance=request.instance.ai,
		new_log=refactor_user_msg,
		ai_output=ai_output,
	)
