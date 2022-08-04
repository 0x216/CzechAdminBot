from config import bot, USER, PASSWORD, ADMINS
from datetime import datetime, timedelta
from aiogram.dispatcher.filters import Filter
from aiogram.types import Message, User
from typing import Tuple, Any
from pathlib import Path
import asyncio
import psycopg2
from loguru import logger
import psycopg2
from aiogram.contrib.middlewares.i18n import I18nMiddleware


LANG_STORAGE = {}
LANGS = []

I18N_DOMAIN = "mybot"
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:

        user: User = User.get_current()

        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "en"
        *_, data = args
        language = data['locale'] = LANG_STORAGE[user.id]
        return language

# Setup i18n middleware
i18n = Localization(I18N_DOMAIN, LOCALES_DIR)

_ = i18n.lazy_gettext




class MyDatabase():
    def __init__(self, user=USER, password=PASSWORD, host='127.0.0.1', port='5432', db='postgres'):
        self.conn = psycopg2.connect(user=user, password=password, host=host, port=port, database=db)
        self.cur = self.conn.cursor()

    def create(self, table):
        self.cur.execute(table)
        logger.info("Таблица успешно создана в PostgreSQL")

    def close(self):
        self.cur.close()
        self.conn.close()
        logger.info("Соединение с PostgreSQL закрыто")


# db = MyDatabase()
# db.create('''CREATE TABLE mobile
#             (ID INT PRIMARY KEY     NOT NULL,
#             MODEL           TEXT    NOT NULL,
#             PRICE         REAL); ''')
# db.close()


class MuteModerator:

    async def mute_for_sometime(self, chat_id, user_id, time):
        TIME = []
        for i in time:
            TIME.append(i)
            if i == 'd':
                time_from_now = datetime.now() + timedelta(days=TIME[0])
                await bot.ban_chat_member(chat_id, user_id, '{:%H:%M:%S}'.format(time_from_now))

            elif i == 'h':
                time_from_now = datetime.now() + timedelta(hours=TIME[0])
                await bot.ban_chat_member(chat_id, user_id, '{:%H:%M:%S}'.format(time_from_now))

            elif i == 'm':
                time_from_now = datetime.now() + timedelta(minutes=TIME[0])
                await bot.ban_chat_member(chat_id, user_id, '{:%H:%M:%S}'.format(time_from_now))

            elif i == 'forever':
                await bot.ban_chat_member(chat_id, user_id)

    async def unmute(self, chat_id, user_id):
        await bot.unban_chat_member(chat_id=chat_id, user_id=user_id)


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: Message):
        return message.from_user.id in ADMINS



