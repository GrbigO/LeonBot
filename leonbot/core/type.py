from typing import Union

from telegram import Update
from django.utils.functional import empty

def is_bool(value: str) -> Union[bool, empty]:
	# value = set(value.split())
	# if "true!" in value:
	# 	return True
	# elif "True!" in value:
	# 	return True

	return False

def is_shit():
	pass