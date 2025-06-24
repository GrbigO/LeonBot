from telegram import Update

from .utils import slash_n


class Text:

	DOLLAR_SIGN = f"'2 dollar sign'"
	__ = "__"
	AD = "$$"

	@classmethod
	def new(cls, name, data):
		return cls.refactor_name(name) + cls.refactor_data(data)

	@classmethod
	def bulk_new(cls, names, name_data):
		cache_names = {}

		for name in names:
			_name = cache_names.get(name)
			if _name is None:
				_name = cls.refactor_name(name)
				names[name] = _name

			for data in name_data:
				yield _name + cls.refactor_data(data)

	@classmethod
	def refactor_data(cls, data):
		refactor_data = cls.refactor(data.strip(), cls.DOLLAR_SIGN)
		return refactor_data + cls.AD + slash_n()

	@classmethod
	def refactor_name(cls, name: str):
		refactor_name = cls.refactor(name.strip(), cls.__)

		return refactor_name + cls.AD + " :" + slash_n()

	@classmethod
	def refactor(cls, text: str, refactor):
		return text.replace(cls.AD, refactor)

