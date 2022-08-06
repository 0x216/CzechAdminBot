from aiogram.dispatcher.filters import Filter, Text
from aiogram.types import Message
from config import ADMINS, FORBIDDEN_WORDS, dp, bot


def is_permitted():

    @dp.message_handler(Text(contains=FORBIDDEN_WORDS, ignore_case=True))
    async def delete_forbidden_words(message: Message):
        await bot.delete_message(message.chat.id, message.message_id)


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: Message):
        return message.from_user.id in ADMINS

#
# class WordChecker(Filter):
#
#     key = 'words_checker'
#
#     @dp.message_handler(Text(contains=FORBIDDEN_WORDS, ignore_case=True))
#     async def delete_forbidden_words(self, message: Message):
#         return bot.delete_message(self, message.chat.id, message.message_id)
#

# def check_for_forbidden():
#     @dp.message_handler(Text(contains=FORBIDDEN_WORDS, ignore_case=True))
#     async def delete_forbidden_words(message: Message):
#         await bot.delete_message(message.chat.id, message.message_id)
