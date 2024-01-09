import os

from dotenv import load_dotenv
from disnake import Embed


load_dotenv()

'''system settings'''
NAME = os.getenv('NAME')
PREFIX = os.getenv('PREFIX')
SYSTEM_CHANNEL_ID = int(os.getenv('SYSTEM_CHANNEL_ID'))
TOKEN = os.getenv('TOKEN')

'''media'''
ON_MEMBER_JOIN_IMAGE = 'https://cdn.discordapp.com/attachments/994485441250218015/1142678954633859102/TepidNecessaryIchidna-size_restricted.gif'

'''roles'''
NEW_MEMBER_ROLE_ID = int(os.getenv('NEW_MEMBER_ROLE_ID'))
ADMINISTRATOR_ROLE_ID = int(os.getenv('ADMINISTRATOR_ROLE_ID'))

