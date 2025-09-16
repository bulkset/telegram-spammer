import asyncio
import random
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE, GROUP_ID

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(PHONE)
    print("BOT ISHLAMOQDA.")
    while True:
        try:
            messages = await client.get_messages('me', limit=1)
            if messages:
                message = messages[0]
                await client.forward_messages(GROUP_ID, message)
                print(f"YUBORILDI - {GROUP_ID}")
            else:
                print("saved messages not found")
            await asyncio.sleep(random.randint(30, 90))
        except Exception as e:
            print(f"error: {e}")
            await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())