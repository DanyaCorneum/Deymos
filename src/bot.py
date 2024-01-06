import os

import disnake
from disnake.ext.commands import Bot
from dotenv import load_dotenv

from config import PREFIX, TOKEN


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
        pass

    async def load_cogs(self) -> None:
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            if file.endswith('.py'):
                extension = file[:-3]
                try:
                    self.load_extension(f"cogs.{extension}")
                except Exception as e:
                    print(e)


bot = DiscordBot()

if __name__ == '__main__':
    bot.run(TOKEN)

