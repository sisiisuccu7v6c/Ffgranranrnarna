from aiogram import Router
from aiogram.types import Message

echo = Router()

@echo.message()
async def hand(msg: Message):
    try:
        await msg.send_copy(chat_id=msg.chat_id)
    except TypeError:
        return
