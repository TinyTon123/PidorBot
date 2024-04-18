import requests as req
import numpy as np
import requests
import asyncio

from aiogram import Router, F, types, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_data.config import load_config, Config

router: Router = Router()

config: Config = load_config()
ydx_cloud_api_key: str = config.api_config.yandex_api
ydx_cloud_catalogue_id: str = config.api_config.yandex_catalogue_id
bot_token: str = config.tg_bot.token

bot_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot: Bot = Bot(bot_token, default=bot_properties)

messages_to_mock = []


@router.message(F.text, F.chat.id == -1001403290431, ~F.forward_from, ~F.is_bot, ~(F.from_user.id == 391639940))
async def mock_news(message: types.Message) -> None:
    if np.random.binomial(1, 0.08):
        msg = f'''{message.text}'''
        messages_to_mock.append(msg)
        await bot.set_message_reaction(chat_id=message.chat.id, message_id=message.message_id,
                                       reaction=[types.ReactionTypeEmoji(emoji='👀')])

        if len(messages_to_mock) >= 3:
            request_text = '. '.join(messages_to_mock)
            try:
                text: str = f'''Составь небольшую смешную выдуманную заметку в новостном ключе на основе следующего текста:
                                {request_text}.
                                Не более 400 символов. Не комментируй новость.
                                Не используй слова "заголовок", "текст новости" и "Вот что у меня получилось".'''

                prompt = {
                    "modelUri": f"gpt://{ydx_cloud_catalogue_id}/yandexgpt-lite",
                    "completionOptions": {
                        "stream": False,
                        "temperature": 1,
                        "maxTokens": "2000"
                    },
                    "messages": [
                        {
                            "role": "user",
                            "text": text
                        }
                    ]
                }

                url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync"
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Api-Key {ydx_cloud_api_key}"
                }

                response = req.post(url, headers=headers, json=prompt)
                print(response.json())

                await asyncio.sleep(5)

                response_id = response.json()['id']
                response_url = f"https://operation.api.cloud.yandex.net/operations/{response_id}"
                final_response = requests.get(response_url, headers=headers)
                final_text = final_response.json()['response']['alternatives'][0]['message']['text'].replace('*', '')

                if not final_text.startswith('К сожалению'):
                    await bot.send_message(chat_id=-1001403290431, text=final_text)

                messages_to_mock.clear()

            except Exception:
                pass
