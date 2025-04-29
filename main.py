import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")  # Token secure tarike se

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot chalu hai!")

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
