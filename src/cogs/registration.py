import dataclasses

import disnake
from disnake import MessageInteraction
from disnake.ext import commands

from src.config import SYSTEM_CHANNEL_ID, REGISTRATION_EMBED


class RegistrationButton(disnake.ui.View):

    def __init__(self):
        super().__init__()

    @disnake.ui.button(label="Test",
                       style=disnake.ButtonStyle.success,
                       custom_id='TEST')
    async def test(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_message('HI')


class Registration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reg(self, cxt: commands.Context):
        if cxt.channel.id != SYSTEM_CHANNEL_ID:
            await cxt.channel.send('Wrong channel for registration')
        else:
            channel = disnake.utils.get(cxt.guild.channels, id=SYSTEM_CHANNEL_ID)
            await channel.send(embed=REGISTRATION_EMBED, view=RegistrationButton())


def setup(bot) -> None:
    bot.add_cog(Registration(bot))
