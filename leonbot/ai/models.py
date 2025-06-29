from functools import partial

from django.db import models
from django.contrib.postgres.fields import ArrayField


from . import Model
from ..botconfs import bot_settings




class AISettings(models.Model):

	# Field for -Request to AI- `AIRequestHandler`
	msg_logs = ArrayField(base_field=models.JSONField(default=dict), default=partial(list, dict()))
	deep = models.CharField(max_length=1000, blank=True)
	active_model = models.TextField(default=Model.DEEPSEEK_v3_0324, choices=Model.CHOICES)

	# Special field for group
	stores = models.JSONField(default=dict)

	update_at = models.DateTimeField(auto_now=True)

	def new_log(self, log: dict) -> None:
		self.msg_logs.append(log)


	def get_msg_logs(self):
		len_msg_logs = len(self.msg_logs)

		base_index = len_msg_logs - bot_settings.MAX_MSG_LOGS + 2 \
			if len_msg_logs > bot_settings.MAX_MSG_LOGS else 0

		self.msg_logs = self.msg_logs[base_index: len_msg_logs]

		return self.msg_logs

	def generate_stores(self):
		for _, name, store in self.stores.values():
			yield name + " : " + store

