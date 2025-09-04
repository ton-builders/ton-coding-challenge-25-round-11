from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

GIFTS = [
    {"id": "5882129648002794519", "sticker": {"emoji": "🎁"}, "star_count": 2500, "remaining_count": 46184, "total_count": 50000},
    {"id": "5170145012310081615", "sticker": {"emoji": "💝"}, "star_count": 15}
]

class GiftsBot:
    def __init__(self, token):
        self.app = ApplicationBuilder().token(token).build()
        self.app.add_handler(CommandHandler("gifts", self.gifts))

    async def gifts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        messages = []
        for gift in GIFTS:
            text = f"{gift['sticker']['emoji']} - {gift['star_count']} stars"
            if "remaining_count" in gift and "total_count" in gift:
                text += " (Upgradable)"
            messages.append(text)
        await update.message.reply_text("\n".join(messages))

    def run(self):
        self.app.run_polling()

if __name__ == "__main__":
    bot = GiftsBot("YOUR_BOT_TOKEN")
    bot.run()
