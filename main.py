# -*- coding: utf-8 -*-

import asyncio
import logging
import datetime
import random
import requests as req

from aiogram import Bot, Dispatcher
from aiogram.utils.markdown import hide_link

from config_data.config import load_config, Config
from dictionary.replies import replies
from handlers import re_handlers, chat_members_handlers


# Загружаем конфиг в переменную config
config: Config = load_config()
bot_token: str = config.tg_bot.token
ggl_api_key: str = config.api_config.google_api


async def main() -> None:
    dp: Dispatcher = Dispatcher()
    dp.include_router(re_handlers.router)
    dp.include_router(chat_members_handlers.router)
    bot: Bot = Bot(bot_token, parse_mode="HTML")

    async def send_message_on_specific_day():
        # Определите, в какой день недели нужно отправлять сообщение (0 - понедельник, 6 - воскресенье)
        target_day = 2
        target_hour = 9

        while True:
            # Получаем текущий день недели
            current_day = datetime.datetime.today().weekday()
            current_hour = datetime.datetime.today().hour

            ggl_url: str = f"https://customsearch.googleapis.com/customsearch/v1?cx=6120d6c5dd8c74814&" \
                           f"fileType=jpg&num=10&imgType=photo&gl=ru&lr=lang_ru&q=это%20среда%20мои%20чуваки&" \
                           f"searchType=image&siteSearch=free3d.com&siteSearchFilter=e&key={ggl_api_key}"
            ggl_search_result: dict[str, list[dict[str, str]]] = req.get(ggl_url).json()

            link: str = ggl_search_result['items'][random.randint(0, 10)]['link']
            answer: str = f"""{hide_link(link)}{replies['wednesday']}"""

            if (current_day == target_day) and (current_hour >= target_hour):
                # Отправляем сообщение
                await bot.send_message(chat_id=1403290431, text=answer)
                # Ждем неделю перед отправкой следующего сообщения
                await asyncio.sleep(60 * 60 * 24 * 6)
            else:
                # Если текущий день недели не является целевым, ждем 1 час и проверяем снова
                await asyncio.sleep(60 * 60)

    loop = asyncio.get_event_loop()
    loop.create_task(send_message_on_specific_day())
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.send_message(chat_id=391639940, text=f"{replies['startup']}")
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
