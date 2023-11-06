import asyncio
import telegram as tel
import sys

async def send_message():
    bot = tel.Bot(token="6345282020:AAE4Z_7L9islIhFbBfkMcY3Sa5m2ZkrvxJE")
    chat_id = 6478368513
    await bot.send_message(chat_id=chat_id, text=sys.argv[1])

asyncio.run(send_message())  # Python 3.7 이상을 사용하고 있다면 asyncio.run으로 비동기 함수를 실행합니다.
