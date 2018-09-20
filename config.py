import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BACKEND = os.getenv('BACKEND', 'Text')

BOT_DATA_DIR = join(dirname(__file__), 'data')
BOT_EXTRA_PLUGIN_DIR = join(dirname(__file__), 'plugins')

BOT_LOG_FILE = join(dirname(__file__), 'errbot.log')
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = (os.getenv('ADMINS', default=None))

BOT_ASYNC = True
BOT_ASYNC_POOLSIZE = 10

BOT_IDENTITY = {
  'token': os.getenv('TOKEN', default=None)
}

BOT_PREFIX_OPTIONAL_ON_CHAT = True
BOT_ALT_PREFIXES = ('@polyxena',)
CHATROOM_PRESENCE = ()

BOT_EXTRA_STORAGE_PLUGINS_DIR = join(dirname(__file__), 'plugins/err-storage-redis') # noqa
STORAGE = 'Redis'
STORAGE_CONFIG = {
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': os.getenv('REDIS_PORT', 6379),
    'db': os.getenv('REDIS_DB', ''),
    'password': os.getenv('REDIS_PASSWORD', ''),
}
