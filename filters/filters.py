from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from config import FORBIDDEN_WORDS, dp, bot, list_super_admins
from aiogram.dispatcher.filters import BoundFilter
from Database.Database import Database


def is_permitted():

    @dp.message_handler(Text(contains=FORBIDDEN_WORDS, ignore_case=True))
    async def delete_forbidden_words(message: Message):
        await bot.delete_message(message.chat.id, message.message_id)


class SuperAdmin(BoundFilter):
    key = 'is_super_admin'

    async def check(self, message: Message) -> bool:
        return message.from_user.id in list_super_admins


class IsAdmin(BoundFilter):
    key = "is_admin"

    async def check(self, message: Message) -> bool:
        return message.from_user.id in Database().get_admins()

