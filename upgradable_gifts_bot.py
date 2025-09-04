from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

GIFTS = [
    {
        "id": "5882129648002794519",
        "sticker": {"emoji": "🎁"},
        "star_count": 2500,
        "remaining_count": 46184,
        "total_count": 50000
    },
    {
        "id": "5170145012310081615",
        "sticker": {"emoji": "💝"},
        "star_count": 15
    }
]

def gifts(update: Update, context: CallbackContext):
    response = []
    for gift in GIFTS:
        emoji = gift["sticker"]["emoji"]
        text = f"{emoji} - {gift['star_count']} stars"
        if "remaining_count" in gift and "total_count" in gift:
            text += " (Upgradable)"
        response.append(text)
    update.message.reply_text("\n".join(response))

def main():
    updater = Updater("YOUR_BOT_TOKEN")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("gifts", gifts))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
