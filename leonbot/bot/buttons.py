from telegram import Update
from telegram import InlineKeyboardButton as IKButton

from django.utils.functional import classproperty

from .enums import ButtonInfo
from ..ai.utils import rework_name
from ..botconfs import bot_settings
from ..core.utils import slash_t
from ..core.request import is_request_in_group, RequestContext

INFO_BUTTON = [IKButton(text=ButtonInfo.Info.name, callback_data=ButtonInfo.Info.name)]
MODELS_BUTTON = [IKButton(text=ButtonInfo.Models.name, callback_data=ButtonInfo.Models.name)]

class Button:

    @classmethod
    def get_info_button(cls) -> list[IKButton]:
        global INFO_BUTTON
        return INFO_BUTTON

    @classmethod
    def get_models_button(cls) -> list[IKButton]:
        global MODELS_BUTTON
        return MODELS_BUTTON

    @classmethod
    def get_settings_button(cls, update: Update) -> list[IKButton]:

        if is_request_in_group(update):
            base = ButtonInfo.Settings.name + slash_t()
            group_name = update.effective_chat.effective_name
            name = base + rework_name(name=group_name, max_length=bot_settings.GROUP_MAX_LENGTH)

            setting_button = IKButton(text=name, callback_data=name)

        else:
            arg = ButtonInfo.Settings.value[0]
            setting_button = IKButton(text=arg, callback_data=arg)


        return [setting_button]

    @classmethod
    def get_buttons(cls, update: Update) -> list[list[IKButton]]:
        return [cls.get_info_button(), cls.get_models_button(), cls.get_settings_button(update)]



