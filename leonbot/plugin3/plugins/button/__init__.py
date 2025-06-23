from leonbot.bot.buttons import Button
from ....chat.utils import slash_n


class ButtonSort:
	CHOICES = (
		(132, Button.Info.name + slash_n() + Button.Models.name + slash_n() + Button.Settings.name),
		(213, Button.Models.name + slash_n() + Button.Info.name + slash_n() + Button.Settings.name),
		(231, Button.Models.name + slash_n() + Button.Settings.name + slash_n() + Button.Info.name),
		(321, Button.Info.name + slash_n() + Button.Models.name + slash_n() + Button.Info.name),
		(312, Button.Info.name + slash_n() + Button.Info.name + slash_n() + Button.Models.name),
	)