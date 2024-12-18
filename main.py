from config import *
import os
from dotenv import load_dotenv
from methods.summarizer.summarizer_handler import summarizer_handler_router
import asyncio

import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()

bot_token = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
# bot.set_my_commands(commands=commands)

storage = MemoryStorage()



dp = Dispatcher(storage=storage)


router = Router()

router.include_routers(summarizer_handler_router)

dp.include_routers(router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await menu_button(bot)
    await dp.start_polling(bot)    

if __name__ == "__main__":     
    asyncio.run(main())