from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot)

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

@dp.message_handler(commands=["gifts"])
async def send_gifts(message: types.Message):
    response = []
    for gift in GIFTS:
        emoji = gift["sticker"]["emoji"]
        text = f"{emoji} - {gift['star_count']} stars"
        if "remaining_count" in gift and "total_count" in gift:
            text += " (Upgradable)"
        response.append(text)
    await message.reply("\n".join(response))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
