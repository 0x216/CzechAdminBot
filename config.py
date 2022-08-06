from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = '5568460231:AAGBUkv23kYL2n1E8aFxE0-1KE0VGLkJBAY'
USER = 'postgres'
PASSWORD = 'Loverdr2'

# BOT_TOKEN = os.getenv('BOT_TOKEN')
# CHAT_ID = os.getenv('CHAT_ID')
# USER = os.getenv('USER')
# PASSWORD = os.getenv("PASSWORD")

ADMINS = []
FORBIDDEN_WORDS = [
    'Козел'
]

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

