from ....bot.enums import ButtonInfo
from ....core.utils import slash_n


class ButtonSort:
	CHOICES = (
		(132, ButtonInfo.Info.name + slash_n() + ButtonInfo.Models.name + slash_n() + ButtonInfo.Settings.name),
		(213, ButtonInfo.Models.name + slash_n() + ButtonInfo.Info.name + slash_n() + ButtonInfo.Settings.name),
		(231, ButtonInfo.Models.name + slash_n() + ButtonInfo.Settings.name + slash_n() + ButtonInfo.Info.name),
		(321, ButtonInfo.Info.name + slash_n() + ButtonInfo.Models.name + slash_n() + ButtonInfo.Info.name),
		(312, ButtonInfo.Info.name + slash_n() + ButtonInfo.Info.name + slash_n() + ButtonInfo.Models.name),
	)