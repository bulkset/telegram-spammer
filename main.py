import asyncio
import random
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE, GROUP_ID, GROUP_ID2, GROUP_ID3, GROUP_ID4, SOURCE_CHANNEL

async def send_hourly_messages(client):
    while True:
        try:
            messages = await client.get_messages(SOURCE_CHANNEL, limit=1)
            if messages:
                await client.forward_messages(GROUP_ID4, messages[0])
                print(f"YUBORILDI HOURLY - {GROUP_ID4}")
        except Exception as e:
            print(f"error hourly: {e}")
        await asyncio.sleep(3600)

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(PHONE)
    print("BOT ISHLAMOQDA.")
    asyncio.create_task(send_hourly_messages(client))
    while True:
        try:
            messages = await client.get_messages(SOURCE_CHANNEL, limit=2)
            if len(messages) >= 2:
                for msg in messages:
                    groups = [GROUP_ID, GROUP_ID2, GROUP_ID3]
                    random.shuffle(groups)
                    for group in groups:
                        await client.forward_messages(group, msg)
                        print(f"YUBORILDI - {group}")
                        await asyncio.sleep(60)
            else:
                print("not enough messages in source channel")
        except Exception as e:
            print(f"error: {e}")
            await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())