from telegram.ext import Updater, CommandHandler

# Yahan tumhara actual bot token directly likha gaya hai
TOKEN = "7386973532:AAGNP-IadFCd9tTw2MohGrghFZxZF7Tk4bo"

def start(update, context):
    update.message.reply_text("Welcome to LootBazaar Bot! Use /refer to get your referral link.")

def refer(update, context):
    user_id = update.message.from_user.id
    referral_link = f"https://t.me/JoinLootBazaarBot?start={user_id}"
    update.message.reply_text(f"Your referral link:\n{referral_link}")

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("refer", refer))

updater.start_polling()
updater.idle()
