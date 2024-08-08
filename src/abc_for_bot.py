from abc import ABC, abstractmethod
import sqlite3 as sq
import os


class ABCDataBase(ABC):
    """ABC Class provides an API for working with databases"""

    def __init__(self, db_name, table_name):
        self.__db_name = db_name
        self.__table_name = table_name

    async def is_database_work(self):
        print(f'DB {self.__db_name} is connect')

    async def init_table(self):
        with sq.connect(self.__db_name) as db:
            cur = db.cursor()
            cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.__table_name} (
            id INT
            username TEXT
            )""")
            db.commit()
        db.close()

    async def delete_db(self):
        os.remove(self.__db_name)
        
    @abstractmethod
    async def add_user(self):
        pass

    @abstractmethod
    async def remove_user(self):
        pass