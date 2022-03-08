from aiogram import Bot, Dispatcher, executor
from data.config import *
from data.states import *
from db.connect import create_pool, close_pool
from aiomysql import Cursor
from db.schema import create_tables
from locales.manager import localization, gettext

_ = gettext

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())