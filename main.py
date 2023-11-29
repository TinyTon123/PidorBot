# -*- coding: utf-8 -*-

import asyncio
import logging
import datetime

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

    async def send_message_on_specific_day():
        # Определите, в какой день недели нужно отправлять сообщение (0 - понедельник, 6 - воскресенье)
        target_day = 2
        target_hour = 7

        while True:
            # Получаем текущий день недели
            current_day = datetime.datetime.today().weekday()
            current_hour = datetime.datetime.today().hour

            if (current_day == target_day) and (current_hour >= target_hour):
                # Отправляем сообщение
                await bot.send_message(chat_id=391639940, text="Регулярное сообщение")
                # Ждем неделю перед отправкой следующего сообщения
                await asyncio.sleep(60 * 30)
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
