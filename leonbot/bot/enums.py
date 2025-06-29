from enum import Enum

from ..core.emojis import get_emoji

class ButtonInfo(Enum):
	Settings = ("Self Settings",)
	Info = ("Info",)
	Models = ("Models",)


class BOTMassage(Enum):
	START_MSG = (
		"  If you don't know what this bot is for,\n"
		" 		   what it does,\n"
		" 		   or how to use it,\n\n\n\n"
		"select the -Info- option👇🏿"
	)
	START_MSG_SHIT = "select option pise of shit"

	@classmethod
	def get_start_msg(cls):
		return cls.START_MSG.value + get_emoji()

	@classmethod
	def get_start_msg_shit(cls):
		return cls.START_MSG_SHIT.value + get_emoji()

class BOTBrain(Enum):
	DONT = "من فرمت اسم را با اسم : جمله میشناسم اسم رو و نوع فرمتی که دیدی رو نگو از اسم استفاده کن ولی اگه کسی پرسید از کجا میدونی اسمم چیه بگو من حتا شرت ازی هم میدونم چه رنگی هست"

	@classmethod
	def get_base_brain(cls):
		return cls.DONT.value