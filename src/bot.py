import os
import sqlite3 as sq

import disnake
from disnake.ext.commands import Bot
from dotenv import load_dotenv

from abc_for_bot import ABCDataBase
from config import PREFIX, SYSTEM_CHANNEL_ID, NAME


load_dotenv()


class UserDatabase(ABCDataBase):
    def __init__(self, name, table_name):
        super().__init__(name, table_name)


class DiscordBot(Bot):

    def __init__(self, database: ABCDataBase):
        super().__init__(
            command_prefix=PREFIX,
            intents=disnake.Intents.all(),
            help_command=None
        )
        self.db_user = database

    async def on_ready(self):
        await self.db_user.is_database_work()
        print(f"Bot {self.user} is ready")

    async def on_message(self, message: disnake.Message) -> None:
        if message.author.name != NAME:
            channel = self.get_channel(SYSTEM_CHANNEL_ID)
            await channel.send(content=message.content)


bot = DiscordBot(UserDatabase('user.db', 'user'))

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
