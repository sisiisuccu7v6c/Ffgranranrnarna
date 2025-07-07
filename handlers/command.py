from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

command = Router()

@command.message(Command("start"))
async def hand(msg: Message):
    await msg.answer("<b>👋 Hello!</b>")