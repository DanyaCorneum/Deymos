import disnake
from disnake.ext import commands

from src.config import SYSTEM_CHANNEL_ID, REGISTRATION_EMBED


class Registration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reg(self, cxt: commands.Context):
        if cxt.channel.id != SYSTEM_CHANNEL_ID:
            await cxt.channel.send('Wrong channel for registration')
        else:
            channel = disnake.utils.get(cxt.guild.channels, id=SYSTEM_CHANNEL_ID)
            await channel.send(embed=REGISTRATION_EMBED)


def setup(bot) -> None:
    bot.add_cog(Registration(bot))