from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
USER = os.getenv('USER')
PASSWORD = os.getenv("PASSWORD")
list_super_admins = os.getenv('list_super_admins')

FORBIDDEN_WORDS = [
    'Козел'
]

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

