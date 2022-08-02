import asyncio
from aiogram.types import Message
from aiogram import types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import BOT_TOKEN
from handlers import MuteModerator
from config import dp
from config import ADMINS

mute_mode = MuteModerator()
user_message = 'Пользователь'
admin_message = 'Админ'

# @dp.message_handler(commands='start')
# async def cmd_start(message: types.Message):
#
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#
#     markup.row(user_message, admin_message)
#
#     await message.answer("Привет! 👋", reply_markup=markup)
#
#
# @dp.message_handler(text=user_message)
# async def user_mode(message: types.Message):
#
#     await message.answer('Включен пользовательский режим.', reply_markup=ReplyKeyboardRemove())
#
# @dp.message_handler(text=admin_message)
# async def admin_mode(message: types.Message):
#
#     await message.answer('Включен админский режим.', reply_markup=ReplyKeyboardRemove())



@dp.message_handler(commands="ban", commands_prefix='!')
async def ban(message: types.Message):
    if message.reply_to_message:

        if message.from_user.id in ADMINS:
            condition = message.text.split()[1]
            await mute_mode.mute_for_sometime(message.chat.id, message.from_user.id, condition)
        else:
            await message.reply(f"На данный момент вы не являйтесь админом.")




@dp.message_handler(commands="unmute", commands_prefix='!')
async def unmute(message: Message):
    if message.reply_to_message:

        if message.from_user.id in ADMINS:
            await mute_mode.un_mute(message.chat.id, message.from_user.id)
        else:
            await message.reply(f"На данный момент вы не являйтесь админом.")






if __name__ == '__main__':
    executor.start_polling(dp)




























