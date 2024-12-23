import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import ErrorEvent

from config import Config, load_config
from src.handlers import Start, Iaas


logger = logging.getLogger(__name__)


async def error_handler(event: ErrorEvent, bot: Bot):
    logger.error(f"Update: {event.update}")
    logger.error(f"Exception: {event.exception}")


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Starting bot")

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token,default=DefaultBotProperties(parse_mode='HTML'))
    dp: Dispatcher = Dispatcher()

    dp.include_router(Start.router)
    dp.include_router(Iaas.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")