from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot)

GIFTS = [
    {"id": "5882129648002794519", "sticker": {"emoji": "🎁"}, "star_count": 2500, "remaining_count": 46184, "total_count": 50000},
    {"id": "5170145012310081615", "sticker": {"emoji": "💝"}, "star_count": 15}
]

def format_gifts():
    for gift in GIFTS:
        text = f"{gift['sticker']['emoji']} - {gift['star_count']} stars"
        if "remaining_count" in gift and "total_count" in gift:
            text += " (Upgradable)"
        yield text

@dp.message_handler(commands=["gifts"])
async def send_gifts(message: types.Message):
    await message.reply("\n".join(format_gifts()))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
