from random import randint


support_emojis = [
	"🥹", "🤬", "😤", "🫠", "😾",
	"🤢", "🤮", "👹","🤰🏿", "🎅🏿",
	"👵🏿", "🥶",
]



def get_emoji() -> str:
	return support_emojis[randint(0, 11)]