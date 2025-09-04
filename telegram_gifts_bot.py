from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

GIFTS = [
    {"id": "5882129648002794519", "sticker": {"emoji": "🎁"}, "star_count": 2500, "remaining_count": 46184, "total_count": 50000},
    {"id": "5170145012310081615", "sticker": {"emoji": "💝"}, "star_count": 15}
]

async def gifts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    format_gift = lambda g: f"{g['sticker']['emoji']} - {g['star_count']} stars" + (" (Upgradable)" if "remaining_count" in g and "total_count" in g else "")
    response = list(map(format_gift, GIFTS))
    await update.message.reply_text("\n".join(response))

def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
    app.add_handler(CommandHandler("gifts", gifts))
    app.run_polling()

if __name__ == "__main__":
    main()
