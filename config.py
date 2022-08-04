from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv



load_dotenv()

BOT_TOKEN = '5568460231:AAGBUkv23kYL2n1E8aFxE0-1KE0VGLkJBAY'
# BOT_TOKEN = os.getenv('5568460231:AAGBUkv23kYL2n1E8aFxE0-1KE0VGLkJBAY')
CHAT_ID = os.getenv('620755101')
USER = os.getenv('postgres')
PASSWORD = os.getenv("Loverdr2")

ADMINS = []
# 620755101
loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

