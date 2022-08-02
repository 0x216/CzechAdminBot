import psycopg2
from psycopg2 import Error
from aiogram import Bot, Dispatcher
import asyncio

BOT_TOKEN = '5568460231:AAGBUkv23kYL2n1E8aFxE0-1KE0VGLkJBAY'
# CHAT_ID = '620755101'
ADMINS = []

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)



try:
    connection = psycopg2.connect(user="postgres",
                                  password="Loverdr2",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE mobile
                          (ID INT PRIMARY KEY     NOT NULL,
                          MODEL           TEXT    NOT NULL,
                          PRICE         REAL); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)







