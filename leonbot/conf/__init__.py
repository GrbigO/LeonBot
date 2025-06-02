from enum import Enum
from typing import Any


class Config(Enum):
	Conversation = []



def new_config(save_to: str, code: Any) -> None:
	return