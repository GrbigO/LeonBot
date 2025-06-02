from telegram.ext import ApplicationBuilder

from leonbot.botconf.configs import Config

if __name__ == "__main__":
    TOKEN = "7519884445:AAEvY5JIIQVQWyQJu6h-AoEEuc6CVIixaO4"
    print("build...")
    app = ApplicationBuilder().token(TOKEN).build()
    print("build...done")
    print("set handler...\n")

    for handler in Config.Conversation.value:
        app.add_handler(handler)
    print("leon-bot is rdy for request...")
    app.run_polling()
