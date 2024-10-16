"""
Main Module.

This module is the entry point of the application. 
It sets up the bot's routes and starts the bot.
"""

import asyncio

from aiogram import (
    Bot,
    Dispatcher,
)

from config import (
    API_TOKEN,
    base_logger,
)
from routers import MAIN_ROUTER


l = base_logger(__name__)

BOT = Bot(API_TOKEN)
DP = Dispatcher()


async def main() -> None:
    """
    Entry point of the program.

    Includes all routes and starts the bot.
    """

    l.info("The bot was started!")

    DP.include_router(MAIN_ROUTER)

    await BOT.delete_webhook(drop_pending_updates=True)
    await DP.start_polling(BOT)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        l.info("The bot was stopped!")
