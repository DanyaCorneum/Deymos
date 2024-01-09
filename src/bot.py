import os

import disnake
from disnake.ext.commands import Bot
from dotenv import load_dotenv

from config import PREFIX, TOKEN, SYSTEM_CHANNEL_ID, NEW_MEMBER_ROLE_ID


load_dotenv()


class DiscordBot(Bot):

    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=disnake.Intents.all(),
            help_command=None
        )
        self.load_cogs()

    async def on_ready(self):
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


bot = DiscordBot()

if __name__ == '__main__':
    bot.run(TOKEN)
