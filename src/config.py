import os

from dotenv import load_dotenv


load_dotenv()

NAME = os.getenv('NAME')
PREFIX = os.getenv('PREFIX')
ADMINISTRATOR_ROLE_ID = int(os.getenv('ADMINISTRATOR_ROLE_ID'))
SYSTEM_CHANNEL_ID = int(os.getenv('SYSTEM_CHANNEL_ID'))
TOKEN = os.getenv('TOKEN')
