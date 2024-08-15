import logging
import os
import sqlite3 as sq

import disnake
from disnake.ext.commands import Bot
from dotenv import load_dotenv

from abc_for_bot import ABCDataBase
from config import PREFIX, SYSTEM_CHANNEL_ID, TOKEN, NEW_MEMBER_ROLE_ID


load_dotenv()


class BotLogger:  # I will do it soon
    pass


class UserDatabase(ABCDataBase):
    def __init__(self, name, table_name):
        super().__init__(name, table_name)

    async def add_user(self, user: disnake.Member):
        member_data = {'name': user.name,
                       'id': user.id}
        with sq.connect(self.db_name) as db:
            db.cursor().execute(f"""INSERT INTO user VALUES('{member_data['name']}', '{member_data['id']}')""")

    def remove_user(self):
        pass


class DiscordBot(Bot):

    def __init__(self, database: ABCDataBase, logger=None):
        super().__init__(
            command_prefix=PREFIX,
            intents=disnake.Intents.all(),
            help_command=None
        )

        self.load_cogs()
        self.db_user = database
        self.logger = logger

    async def on_ready(self):
        await self.db_user.init_table()
        for guild in self.guilds:
            for member in guild.members:
                await self.db_user.add_user(member)
        await self.db_user.is_database_work()
        print(f"Bot {self.user} is ready")

    async def on_member_join(self, member: disnake.Member):

        new_member = disnake.utils.get(member.guild.roles, id=NEW_MEMBER_ROLE_ID)

        member_avatar = await member.avatar.to_file()
        embed = disnake.Embed(title='NEW MEMBER!',
                              description=f"User {member.mention} has joined to server",
                              colour=0x7557ad)
        embed.set_image(file=member_avatar)

        channel = self.get_channel(SYSTEM_CHANNEL_ID)
        await member.add_roles(new_member)
        await channel.send(embed=embed)
        await self.db_user.add_user(member)

    async def on_member_remove(self, member: disnake.Member):
        member_avatar = await member.avatar.to_file()
        embed = disnake.Embed(title='MEMBER LEAVE!',
                              description=f"User {member.mention} has leaved to server",
                              colour=0xa857ad)
        embed.set_image(file=member_avatar)

        channel = self.get_channel(SYSTEM_CHANNEL_ID)
        await channel.send(embed=embed)

    def load_cogs(self) -> None:
        for file in os.listdir("./cogs"):
            if file.endswith('.py'):
                extension = file[:-3]
                if extension != "__init__":
                    try:
                        self.load_extension(f"cogs.{extension}")
                    except Exception as e:
                        print(e)

                        
bot = DiscordBot(UserDatabase('user.db', 'user'))

if __name__ == '__main__':
    bot.run(TOKEN)
