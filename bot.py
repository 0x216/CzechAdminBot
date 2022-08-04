import asyncio
from aiogram.types import Message
from aiogram import types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from handlers import MuteModerator, IsAdmin, i18n
from config import dp, ADMINS


mute_mode = MuteModerator()
is_admin = IsAdmin()
dp.middleware.setup(i18n)
_ = i18n.lazy_gettext


@dp.message_handler(IsAdmin())
async def only_for_admins(message: types.Message):
    await message.reply(_("Only for admins!"))


@dp.message_handler(commands="make")
async def add_to_admins(message: types.Message):
    ADMINS.append(message.from_user.id)
    await message.reply(f"New admins list: {ADMINS}")

@dp.message_handler(commands="ban", commands_prefix='!')
async def ban(message: types.Message):
    if message.reply_to_message:

        condition = message.text.split()[1]
        await mute_mode.mute_for_sometime(message.chat.id, message.from_user.id, condition)


@dp.message_handler(commands="unmute", commands_prefix='!')
async def unmute(message: Message):
    if message.reply_to_message:

        await mute_mode.unmute(message.chat.id, message.from_user.id)

















