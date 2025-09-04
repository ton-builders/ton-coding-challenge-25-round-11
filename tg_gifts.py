import os
from aiohttp import web
import aiohttp
import asyncio

BOT_TOKEN = "YOUR_BOT_TOKEN"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

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

async def handle(request):
    data = await request.json()
    message = data.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if text == "/gifts":
        response = []
        for gift in GIFTS:
            emoji = gift["sticker"]["emoji"]
            line = f"{emoji} - {gift['star_count']} stars"
            if "remaining_count" in gift and "total_count" in gift:
                line += " (Upgradable)"
            response.append(line)
        async with aiohttp.ClientSession() as session:
            await session.post(f"{API_URL}/sendMessage", json={
                "chat_id": chat_id,
                "text": "\n".join(response)
            })
    return web.Response()

def main():
    app = web.Application()
    app.router.add_post("/", handle)
    web.run_app(app, port=8080)

if __name__ == "__main__":
    main()
