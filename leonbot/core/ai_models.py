from enum import Enum


class ChatModel(Enum):

	DEEPSEEK_v3_0324 = "deepseek/deepseek-chat-v3-0324"
	DEEPSEEK_R1_0528 = "deepseek/deepseek-r1-0528:free"
	DEEPSEEK_R1 = "deepseek/deepseek-r1:free"
	DEEPSEEK_V3 = "deepseek/deepseek-chat"

	GPT_4O_MINI = "openai/gpt-4o-mini"
	GPT_4_1 = "openai/gpt-4.1"
	GPT_4_1_MINI = "openai/gpt-4.1-mini"

	GEMINI_2_0_FLASH = "google/gemini-2.0-flash-001"
	GEMINI_2_5_PRO_PREVIEW = "google/gemini-2.5-pro-preview-05-06"
	GEMINI_2_5_FLASH_PREVIEW = "google/gemini-2.5-flash-preview-05-20"

	CLAUDE_SONNET_4 = "anthropic/claude-sonnet-4"



class ImageModel(Enum):
	pass


class FileModel(Enum):
	pass