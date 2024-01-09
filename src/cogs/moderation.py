import typing
import datetime

import disnake
from disnake.ext import commands

from src.config import SYSTEM_CHANNEL_ID, ADMINISTRATOR_ROLE_ID


class Moderation(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(ADMINISTRATOR_ROLE_ID)
    async def kick(self,
                   ctx: commands.Context, *args: disnake.Member) -> None:
        channel = self.bot.get_channel(SYSTEM_CHANNEL_ID)
        for member in args:
            await member.kick()
            await channel.send(f'User {member} has been kicked')

    @commands.command()
    @commands.has_role(ADMINISTRATOR_ROLE_ID)
    async def ban(self,
                   ctx: commands.Context, *args: disnake.Member) -> None:
        channel = self.bot.get_channel(SYSTEM_CHANNEL_ID)
        for member in args:
            await member.ban()
            await channel.send(f'User {member} has been banned')

    @commands.command()
    @commands.has_role(ADMINISTRATOR_ROLE_ID)
    async def mute(self, ctx: commands.Context,
                   *args: disnake.Member,
                   duration: float = 60.0):
        channel = self.bot.get_channel(SYSTEM_CHANNEL_ID)
        for member in args:
            await member.timeout(until=disnake.utils.utcnow() + datetime.timedelta(seconds=duration), reason='Test')
            await channel.send(f'User {member} has been muted')


def setup(bot) -> None:
    bot.add_cog(Moderation(bot))
