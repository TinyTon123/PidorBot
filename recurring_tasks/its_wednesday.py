import asyncio

import datetime
import random
import requests as req

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hide_link

from config_data.config import load_config, Config
from dictionary.replies import replies

config: Config = load_config()
bot_token: str = config.tg_bot.token
ggl_api_key: str = config.api_config.google_api

bot_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot: Bot = Bot(bot_token, default=bot_properties)


async def its_wednesday_my_dudes():
    # Определяем, в какой день недели нужно отправлять сообщение (0 - понедельник, 6 - воскресенье)
    target_day: int = 2
    target_hour: int = 9
    chats: tuple = (391639940, -1001403290431, -1002107056835)

    while True:
        # Получаем текущие день недели и час
        current_day: int = datetime.datetime.today().weekday()
        current_hour: int = datetime.datetime.today().hour

        if (current_day == target_day) and (current_hour >= target_hour):

            ggl_url: str = f"https://customsearch.googleapis.com/customsearch/v1?cx=6120d6c5dd8c74814&" \
                           f"fileType=jpg&num=10&imgType=photo&gl=ru&lr=lang_ru&q=это%20среда%20мои%20чуваки&" \
                           f"searchType=image&siteSearch=free3d.com&siteSearchFilter=e&key={ggl_api_key}"
            ggl_search_result: dict[str, list[dict[str, str]]] = req.get(ggl_url).json()

            link: str = ggl_search_result['items'][random.randint(0, 9)]['link']
            answer: str = f"""{hide_link(link)}{replies['wednesday']}"""

            # Рассылаем сообщения пулу чатов
            for chat_id in chats:
                await bot.send_message(chat_id=chat_id, text=answer)
                await asyncio.sleep(3)

            # Ждем неделю и повторяем процесс
            await asyncio.sleep(60 * 60 * 24 * 7)
        else:
            # Если текущий день недели не является целевым, ждем 1 час и проверяем снова
            await asyncio.sleep(60 * 60)
