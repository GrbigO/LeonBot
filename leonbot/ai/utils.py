from telegram import Update

from ..core import models


def get_default_name(user: Update.effective_user) -> str:
	return user.full_name or user.username or ""


def get_system_name(instance: models.BOT, user: Update.effective_user) -> str:
	store_data = instance.ai.stores.get(user.id)
	if store_data:
		name = store_data[0]
		return name


def get_name(instance, user) -> str:
	name = get_system_name(instance, user) or get_default_name(user)
	return name

def rework_name(name, max_length) -> str:
	if len(name) > max_length:
		name = name[:max_length - 3] + "..."
	return name


def is_auth_this_group(instance: models.BOT, user) -> bool:
	store_data = instance.ai.stores.get(user.id)
	return store_data is not None
