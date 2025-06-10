import os
from typing import NoReturn, Any, Callable

from django.utils.module_loading import import_string
from dotenv import load_dotenv
import dj_database_url

from django.db.utils import DEFAULT_DB_ALIAS, ProgrammingError
from django.conf import global_settings

load_dotenv()


def empty() -> NoReturn:
	pass


def get_env(
		key: str,
		default: Any = empty,
) -> str | Any:
	try:
		value = os.environ[key]
	except KeyError:
		if default is empty:
			raise ValueError(f"{key} is not defined")

		value = default

	return value


def to_list(text: str):
	return [name.strip() for name in text.split(",") if name]


# api
API_ADDERS = "https://openrouter.ai/api/v1/chat/completions"
TOKEN_BOT = get_env("TOKEN_BOT", None)


PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


DEBUG = False
ALLOWED_HOSTS = ["*"]
SECRET_KEY = None


API_KEY = get_env("API_KEY", None)
OPENROUTER_PROVISION_KEY = get_env("OPENROUTER_PROVISION_KEY")




# learn how to ues rd.
BOT_SETTINGS = {
	"NAME": "Leon",
	"REQUEST_NAME": set(get_env("REQUEST_NAME").split()),

	"IS_LOCK": False,
	"MODEL": "deepseek/deepseek-chat-v3-0324:free",
	"BOT_USERNAME": "@LE0NAI_bot",
	"MENTION_TYPE": "mention",
	"GROUP_TYPE":  {"group", "supergroup"},
	"PV_TYPE": "private",

	"MAX_LENGTH_FOR_CALL_BOT": 100,
	"MAX_MSG_LOGS": int(get_env("MAX_MSG_LOGS", 30)),

}

INSTALLED_APPS = [
	"leonbot.account",
	"leonbot.core",
	"leonbot.ai",
]


MIDDLEWARE = []
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

if GROUP_ID is None:
	N = NotImplemented

if AI_KEY is None:
	N = NotImplemented
