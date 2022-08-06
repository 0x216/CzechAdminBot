from aiogram import executor
from handlers.filters import IsAdmin, is_permitted
from config import dp
import bot


if __name__ == '__main__':
    dp.bind_filter(IsAdmin)
    executor.start_polling(dp)
