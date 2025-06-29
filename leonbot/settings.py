import os
from typing import Any, Callable

import dj_database_url
from django.utils.module_loading import import_string
from dotenv import load_dotenv


from django.utils.functional import empty
from django.db.utils import DEFAULT_DB_ALIAS
from django.conf import global_settings




load_dotenv()



def get_env(key: str, default: Any = empty) -> str | Any:
	try:
		value = os.environ[key]
	except KeyError:
		if default is empty:
			raise ValueError(f"{key} is not defined")

		value = default

	return value


def to_list(text: str, type_convertion: Callable[..., ...] | empty = empty) -> list:
	if not text: # maybe text == ""
		return text

	if type_convertion is empty:
		return [name.strip() for name in text.split(",") if name]

	return [type_convertion(name.strip()) for name in text.split(",") if name]



# api
API_ADDERS = "https://openrouter.ai/api/v1/chat/completions"

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

DEBUG = False
ALLOWED_HOSTS = []
SECRET_KEY = None

API_KEY = get_env("API_KEY", None)
WEBHOOK_KEY = get_env("WEBHOOK_KEY", None)
OPENROUTER_PROVISION_KEY = get_env("OPENROUTER_PROVISION_KEY")

# learn how to ues rd.
TOKEN_BOT = get_env("TOKEN_BOT", None)
BOT_LEADER_IDS = [

]


AUTH_USER_MODEL = "account.User"
ROOT_URLCONF = ""
WSGI_APPLICATION = ""
AUTH_PASSWORD_VALIDATORS = []
AUTHENTICATION_BACKENDS = [""]

DATABASES = {
	DEFAULT_DB_ALIAS: dj_database_url.parse(get_env("DATABASE_URL")),
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


INSTALLED_APPS = [
	# Django modules
	"django.contrib.postgres",
	# Local apps
	"leonbot.core",
	"leonbot.bot",
	"leonbot.ai",
	"leonbot.permission",
	"leonbot.plugin3",
]

MIDDLEWARE = []


# if GROUP_ID is None:


# if API_KEY is None:


BOT = {
	"NAME": "Leon",
	"REQUEST_NAME": get_env("REQUEST_NAME").split(","),

	"USERNAME": "@LE0NAI_bot",
	"GROUP_MAX_LENGTH": 8,
	"MAX_MSG_LOGS": int(get_env("MAX_MSG_LOGS", 200)),
}
