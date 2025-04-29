import os
from telegram.ext import Updater, CommandHandler
from telegram import ChatMember, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@JoinLootBazaar"  # Telegram channel
INSTAGRAM_URL = "https://www.instagram.com/md.samir.bhaiii?igsh=ZXVsbDg5Zm53ZnAw"  # Instagram

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def is_user_member(update, context):
    user_id = update.effective_user.id
    try:
        member = context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        return member.status in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.OWNER]
    except:
        return False

def start(update, context):
    if is_user_member(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to LootBazaar Bot!")
    else:
        keyboard = [
            [InlineKeyboardButton("Join Telegram Channel", url="https://t.me/JoinLootBazaar")],
            [InlineKeyboardButton("Join Telegram Group", url="https://t.me/JoinLootBazaarGroup")],
            [InlineKeyboardButton("Follow on Instagram", url=INSTAGRAM_URL)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Bot use karne ke liye pehle hamara channel aur group join karo, aur Instagram par follow karo.",
            reply_markup=reply_markup
        )

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
