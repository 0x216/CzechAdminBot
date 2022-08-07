from aiogram.types import Message
from handlers.mute import MuteModerator
from i18.Localization import _
from filters.filters import IsAdmin, SuperAdmin, is_permitted
from config import dp
from aiogram.dispatcher.filters import Command
from Database.Database import TablesModerate, Database

tables = TablesModerate()
mute_mode = MuteModerator()
is_permitted()


@dp.message_handler(Command(commands="add_admin", prefixes='!'), SuperAdmin())
async def add_to_admins(message: Message):
    try:
        if int(message.text.split()[1]) in Database().get_admins():
            await message.reply(_(f"Юзер уже и так админ!\n\nСписок админов: {Database().get_admins()}"))
        else:
            tables.add_new_admin(message.text.split()[1], message.text.split()[2])
            await message.reply(_(f"Админ успешно добавлен!\n\nСписок админов: {Database().get_admins()}"))
    except IndexError:
        await message.reply(_('Упс, похоже вы ошиблись и добавили нужную информацию не полностью'))


@dp.message_handler(Command("ban", prefixes='!'), IsAdmin())
async def ban(message: Message):
    if message.reply_to_message:
        try:
            condition = message.text.split()[1]
            await mute_mode.mute_for_sometime(message.chat.id, message.from_user.id, condition)
            await message.reply(_(f'{message.from_user.full_name} забанен\n\nБан на {condition}'))
        except IndexError:
            await message.reply(_('Упс, похоже вы ошиблись и добавили нужную информацию не полностью'))
    else:
        await message.reply("Вы должны применить команду на сообщение!")


@dp.message_handler(Command("unmute", prefixes='!'), IsAdmin())
async def unmute(message: Message):
    if message.reply_to_message:
        await mute_mode.unmute(message.chat.id, message.from_user.id)
        await message.reply(_(f'Пользователь {message.from_user.full_name} разбанен'))
    else:
        await message.reply(_("Вы должны применить команду на сообщение!"))


@dp.message_handler(Command('massban', prefixes='!'), IsAdmin())
async def massban(message: Message):
    if message.reply_to_message:
        await mute_mode.massban(message.from_user.id)
        await message.reply(_(f'Пользователь {message.from_user.full_name} забанен везде'))
    else:
        await message.reply(_("Вы должны применить команду на сообщение!"))
