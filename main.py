from handlers.command import command
from handlers.echo import echo
from loader import dp, bot
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def main():
    dp.include_routers(command, echo)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())