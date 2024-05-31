import requests as req
import numpy as np
import requests
import asyncio

from aiogram import Router, F, types

router: Router = Router()

messages_to_mock = []


@router.message(F.text, F.chat.id == -1001403290431, ~F.forward_from, ~F.is_bot, ~(F.from_user.id == 391639940))
async def mock_news(message: types.Message, bot, ydx_cloud_api_key, ydx_cloud_catalogue_id) -> None:
    if np.random.binomial(1, 0.03):
        msg = f'''{message.text}'''
        messages_to_mock.append(msg)
        # await bot.set_message_reaction(chat_id=message.chat.id, message_id=message.message_id,
        #                                reaction=[types.ReactionTypeEmoji(emoji='👀')])
        await bot.send_message(chat_id=391639940, text=f"Записано сообщение: {message.text}.\n\n"
                                                       f"В стеке {len(messages_to_mock)} сообщений")

        if len(messages_to_mock) == 3:
            request_text = '. '.join(messages_to_mock)
            messages_to_mock.clear()
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
                await bot.send_message(chat_id=391639940, text=str(response.json()))

                await asyncio.sleep(10)

                response_id = response.json()['id']
                response_url = f"https://operation.api.cloud.yandex.net/operations/{response_id}"
                final_response = requests.get(response_url, headers=headers)

                while not final_response.json()['done']:
                    await asyncio.sleep(10)
                    final_response = requests.get(response_url, headers=headers)

                final_text = final_response.json()['response']['alternatives'][0]['message']['text'].replace('*', '')

                if not final_text.startswith('К сожалению'):
                    await bot.send_message(chat_id=-1001403290431, text=final_text)
                else:
                    await bot.send_message(chat_id=391639940, text="Генерация не прошла")

            except Exception as e:
                await bot.send_message(chat_id=391639940, text=str(e))
                pass
