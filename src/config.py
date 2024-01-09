import os

from disnake import Embed
from dotenv import load_dotenv


load_dotenv()

'''system settings'''
NAME = os.getenv('NAME')
PREFIX = os.getenv('PREFIX')
SYSTEM_CHANNEL_ID = int(os.getenv('SYSTEM_CHANNEL_ID'))
TOKEN = os.getenv('TOKEN')

'''media'''
REGISTRATION_IMAGE = 'https://cdn.discordapp.com/attachments/994485441250218015/1142678954633859102/TepidNecessaryIchidna-size_restricted.gif'

'''roles'''
NEW_MEMBER_ROLE_ID = int(os.getenv('NEW_MEMBER_ROLE_ID'))
ADMINISTRATOR_ROLE_ID = int(os.getenv('ADMINISTRATOR_ROLE_ID'))

'''embeds'''
REGISTRATION_EMBED = Embed(
    title='Registration',
    description='Hello, new member. Before chating on this server you should register',
    colour=0xba6657,
)
REGISTRATION_EMBED.set_image(REGISTRATION_IMAGE)

