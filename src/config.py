import os

from dotenv import load_dotenv


load_dotenv()

NAME = os.getenv('NAME')
PREFIX = os.getenv('PREFIX')
SYSTEM_CHANNEL_ID = int(os.getenv('SYSTEM_CHANNEL_ID'))
