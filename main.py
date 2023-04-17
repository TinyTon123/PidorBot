# -*- coding: utf-8 -*-

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import load_config, Config
from dictionary.replies import replies
from handlers import re_handlers, chat_members_handlers


# Загружаем конфиг в переменную config
config: Config = load_config()
bot_token: str = config.tg_bot.token


async def main() -> None:
    dp: Dispatcher = Dispatcher()
    dp.include_router(re_handlers.router)
    dp.include_router(chat_members_handlers.router)
    bot: Bot = Bot(bot_token, parse_mode="HTML")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.send_message(391639940, f"{replies['startup']}")
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
