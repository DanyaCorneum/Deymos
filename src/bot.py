import os

import disnake
from disnake.ext.commands import Bot
from dotenv import load_dotenv

from config import PREFIX, SYSTEM_CHANNEL_ID, NAME


load_dotenv()


class DiscordBot(Bot):

    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=disnake.Intents.all(),
            help_command=None
        )

    async def on_ready(self):
        print(f"Bot {self.user} is ready")

    async def on_message(self, message: disnake.Message) -> None:
        if message.author.name != NAME:
            channel = self.get_channel(SYSTEM_CHANNEL_ID)
            await channel.send(content=message.content)


bot = DiscordBot()

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
