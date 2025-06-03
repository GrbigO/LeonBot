from enum import Enum


class DSLMethod(Enum):
	delete = None
	add = None
	update = None
	model = None
	train = None
	user = None
	perm = None
	role = None
	conf = None

	__msg_for = None
	__bag = None
	__restart = None

	@classmethod
	def parse(cls):
		pass

class ChatEnum(Enum):

	@classmethod
	def get_not_authenticate_msg(cls, id, user) -> str:
		return f"@{user}اکانتش ورفای نشده کونی " + "وریفای نشده." + "اکانتت" + f"@{id}"