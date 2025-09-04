import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

GIFTS = [
    {"id": "5882129648002794519", "sticker": {"emoji": "🎁"}, "star_count": 2500, "remaining_count": 46184, "total_count": 50000},
    {"id": "5170145012310081615", "sticker": {"emoji": "💝"}, "star_count": 15}
]

def is_upgradable(gift):
    return "remaining_count" in gift and "total_count" in gift

@bot.message_handler(commands=["gifts"])
def send_gifts(message):
    response = []
    for gift in GIFTS:
        text = f"{gift['sticker']['emoji']} - {gift['star_count']} stars"
        if is_upgradable(gift):
            text += " (Upgradable)"
        response.append(text)
    bot.reply_to(message, "\n".join(response))

if __name__ == "__main__":
    bot.polling(none_stop=True)
