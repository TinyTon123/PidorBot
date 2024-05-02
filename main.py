# -*- coding: utf-8 -*-

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_data.config import load_config, Config
from dictionary.replies import replies
from handlers import re_handlers, chat_members_handlers, mock_news
from recurring_tasks.its_wednesday import its_wednesday_my_dudes


# Загружаем конфиг в переменную config
config: Config = load_config()
bot_token: str = config.tg_bot.token
ggl_api_key: str = config.api_config.google_api
ydx_cloud_api_key: str = config.api_config.yandex_api
ydx_cloud_catalogue_id: str = config.api_config.yandex_catalogue_id


async def main() -> None:
    dp: Dispatcher = Dispatcher()
    dp.include_router(re_handlers.router)
    dp.include_router(chat_members_handlers.router)
    dp.include_router(mock_news.router)
    bot: Bot = Bot(bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.workflow_data.update({'bot': bot,
                             'ggl_api_key': ggl_api_key,
                             'ydx_cloud_api_key': ydx_cloud_api_key,
                             'ydx_cloud_catalogue_id': ydx_cloud_catalogue_id})

    loop = asyncio.get_event_loop()
    loop.create_task(its_wednesday_my_dudes())

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.send_message(chat_id=391639940, text=f"{replies['startup']}")
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
    asyncio.run(main())
