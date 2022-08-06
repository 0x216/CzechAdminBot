from aiogram.types import Message
from aiogram import types
from handlers.mute import MuteModerator
from handlers.Localization import _
from handlers.filters import IsAdmin, is_permitted
from config import dp, ADMINS, FORBIDDEN_WORDS


mute_mode = MuteModerator()
is_permitted()


@dp.message_handler(commands="add_admin")
async def add_to_admins(message: types.Message):
    ADMINS.append(message.from_user.id)
    await message.reply(_(f"Список админов: {ADMINS}"))


@dp.message_handler(IsAdmin())
@dp.message_handler(commands="ban", commands_prefix='!')
async def ban(message: types.Message):
    if message.reply_to_message:
        condition = message.text.split()[1]
        await mute_mode.mute_for_sometime(message.chat.id, message.from_user.id, condition)
        await message.reply(_(f'Забанен на {condition}'))


@dp.message_handler(IsAdmin())
@dp.message_handler(commands="unmute", commands_prefix='!')
async def unmute(message: Message):
    if message.reply_to_message:
        await mute_mode.unmute(message.chat.id, message.from_user.id)
        await message.reply(_(f'Пользователь {message.from_user.full_name} разбанен'))


@dp.message_handler(IsAdmin())
@dp.message_handler(commands='massban', commands_prefix='!')
async def massban(message: Message):
    if message.reply_to_message:
        await mute_mode.massban(message.from_user.id)
        await message.reply(_(f'Пользователь {message.from_user.full_name} забанен везде'))














