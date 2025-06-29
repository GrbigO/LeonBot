from django.db import models
from django.utils import timezone

from ..permission.models import PermissionsMixin
from ..plugin3.abstracts import ModelWithPluginInstaller
from ..core.models import ModelWithAuthField


class BOT(ModelWithPluginInstaller, PermissionsMixin):
	# user_id or group_id or token_bot in telegram
	telegram_id = models.CharField(max_length=45, primary_key=True, serialize=False)

	ai = models.OneToOneField(to="ai.AISettings", on_delete=models.CASCADE)
	settings = models.JSONField(default=dict)

	prent = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True)

