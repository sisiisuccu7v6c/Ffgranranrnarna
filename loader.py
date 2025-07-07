from aiogram.client.default import DefaultBotProperties as Default
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import token

bot = Bot(
    token=token, 
    default=Default(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(
    storage=MemoryStorage()
)