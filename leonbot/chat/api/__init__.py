async def not_valid_code(msg_id):
	return await "not valid code", {"reply_to_message_id": msg_id}


async def _delete_(**kwargs):
	return await not_valid_code(kwargs["message"].message_id)


def _add_delete_(**kwargs):
	pass