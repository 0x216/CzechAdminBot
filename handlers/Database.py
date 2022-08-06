from config import USER, PASSWORD
import psycopg2
from loguru import logger


class MyDatabase:

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

ALL_CHATS = []  # Массив со всеми айдишниками чатов для !massban