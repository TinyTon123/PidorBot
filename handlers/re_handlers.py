import requests as req
import random

from aiogram import Router, F, types
from aiogram.utils.markdown import hide_link

from dictionary.replies import replies, answer_for_roma
from filters import re_functions

router: Router = Router()
router.message.filter(F.text, F.chat.id == -1002107056835)


# Хендлеры для ответа на реплики
@router.message(re_functions.net_answer_filter)
async def net_answer(message: types.Message) -> None:
    net: str = message.text
    if net[-1].lower() in ['t', 'т']:
        await message.answer(f"{replies['net']}")
    else:
        for i in range(1, len(net) + 1):
            if net[-i].lower() in ['t', 'т']:
                await message.answer(f"{replies['net']}{net[-i + 1:]}")
                break


@router.message(re_functions.nit_answer_filter)
async def nit_answer(message: types.Message) -> None:
    nit: str = message.text
    if nit[-1].lower() in ['t', 'т']:
        await message.answer(f"{replies['nit']}")
    else:
        for i in range(1, len(nit) + 1):
            if nit[-i].lower() in ['t', 'т']:
                await message.answer(f"{replies['nit']}{nit[-i + 1:]}")
                break


@router.message(re_functions.no_answer_filter)
async def no_answer(message: types.Message) -> None:
    no: str = message.text
    if no[-1].lower() in ['o', 'у']:
        await message.answer(f"{replies['no']}")
    else:
        for i in range(1, len(no) + 1):
            if no[-i].lower() in ['o', 'у']:
                await message.answer(f"{replies['no']}{no[-i + 1:]}")
                break


@router.message(re_functions.nope_answer_filter)
async def nope_answer(message: types.Message) -> None:
    nope: str = message.text
    if nope[-1].lower() in ['п', 'e']:
        await message.answer(f"{replies['nope']}")
    else:
        for i in range(1, len(nope) + 1):
            if nope[-i].lower() in ['п', 'e']:
                await message.answer(f"{replies['nope']}{nope[-i + 1:]}")
                break


@router.message(re_functions.nein_answer_filter)
async def nein_answer(message: types.Message) -> None:
    nein: str = message.text
    if nein[-1].lower() in ['n', 'н']:
        await message.answer(f"{replies['nein']}")
    else:
        for i in range(1, len(nein) + 1):
            if nein[-i].lower() in ['n', 'н']:
                await message.answer(f"{replies['nein']}{nein[-i + 1:]}")
                break


# @router.message(re_functions.yes_answer_filter)
# async def yes_answer(message: types.Message) -> None:
#     yes: str = message.text
#     if yes[-1].lower() in ['с', 's']:
#         await message.answer(f"{replies['yes']}")
#     else:
#         for i in range(1, len(yes) + 1):
#             if yes[-i].lower() in ['с', 's']:
#                 await message.answer(f"{replies['yes']}{yes[-i + 1:]}")
#                 break
#
#
# @router.message(re_functions.da_answer_filter)
# async def da_answer(message: types.Message) -> None:
#     # Обращаемся к API гугла за картинкой сковороды (deprecated since 21.08.23)
#     # ggl_url: str = f"https://customsearch.googleapis.com/customsearch/v1?" \
#     #                f"cx=6120d6c5dd8c74814&fileType=jpg&num=10&imgType=clipart&gl=ru&" \
#     #                f"lr=lang_ru&q=старая%20сковорода&searchType=image&siteSearch=free3d.com&" \
#     #                f"siteSearchFilter=e&key={ggl_api_key}"""
#     # ggl_search_result: dict[str, list[dict[str, str]]] = req.get(ggl_url).json()
#     # links_list: list = []
#     # for i in range(10):
#     #     links_list.append(ggl_search_result['items'][i]['link'])
#     #
#     # link: str = random.choice(links_list)
#
#     # answer: str = f"""{hide_link(link)}{replies['da']}"""
#
#     # da: str = message.text
#     # if da[-1].lower() in ['а', 'a']:
#     #     await message.answer(f"{replies['da']}")
#     # else:
#     #     for i in range(1, len(da) + 1):
#     #         if da[-i].lower() in ['а', 'a']:
#     #             await message.answer(f"{replies['da']}{da[-i + 1:]}")
#     #             break
#     await message.answer_animation('CgACAgIAAxkBAAIK62U3-oLjJrkyAAFlG3C7rosUenHnTwACeA4AAoNlsUmcXbpBC6TEtDAE')
#
#
# @router.message(re_functions.traktorista_answer_filter)
# async def traktorista_answer(message: types.Message, ggl_api_key) -> None:
#     # Обращаемся к API гугла за картинкой тракториста
#     ggl_url: str = f"https://customsearch.googleapis.com/customsearch/v1?" \
#                    f"cx=6120d6c5dd8c74814&fileType=jpg&num=10&imgType=photo&gl=ru&" \
#                    f"lr=lang_ru&q=тракторист%20в%20тракторе&searchType=image&siteSearch=free3d.com&" \
#                    f"siteSearchFilter=e&key={ggl_api_key}"
#     ggl_search_result: dict[str, list[dict[str, str]]] = req.get(ggl_url).json()
#
#     link: str = ggl_search_result['items'][random.randint(0, 10)]['link']
#
#     answer: str = f"""{hide_link(link)}{replies['300']}"""
#     await message.answer(answer)
#
#
# @router.message(re_functions.gde_answer_filter)
# async def gde_answer(message: types.Message) -> None:
#     await message.answer(random.choice(replies['gde']))
#
#
# @router.message(re_functions.nu_answer_filter)
# async def nu_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['nu']}")
#
#
# @router.message(re_functions.kto_answer_filter)
# async def kto_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['kto']}")
#
#
# @router.message(re_functions.cho_answer_filter)
# async def cho_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['cho']}")
#
#
# @router.message(re_functions.kak_answer_filter)
# async def kak_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['kak']}")
#
#
# @router.message(re_functions.zdraste_answer_filter)
# async def zdraste_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['zdraste']}")
#
#
# @router.message(re_functions.kogda_answer_filter)
# async def kogda_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['kogda']}")
#
#
# @router.message(re_functions.pochemu_answer_filter, ~(F.from_user.id == 125360250))
# async def pochemu_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['pochemu']}")
#
#
# @router.message(re_functions.zachem_answer_filter)
# async def zachem_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['zachem']}")
#
#
# @router.message(re_functions.mne_answer_filter)
# async def mne_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['mne']}")
#
#
# @router.message(re_functions.vot_ona_answer_filter)
# async def vot_ona_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['vot_ona']}")
#
#
# @router.message(re_functions.chto_podelat_answer_filter)
# async def chto_podelat_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['chto_podelat']}")
#
#
# @router.message(F.reply_to_message.from_user.id == 6017337446, F.text.regexp(r"^[хХ]уй на!?$"))
# async def na_answer(message: types.Message):
#     await message.answer(f"{replies['na']}")
#
#
# @router.message(F.from_user.id == 119954087, F.reply_to_message.from_user.id == 6017337446)
# async def joke_answer(message: types.Message):
#     await message.answer(text=random.choice(answer_for_roma))
#
#
# @router.message(re_functions.friday)
# async def friday(message: types.Message, ending: str):
#     answer = random.randint(0, 2)
#     if answer == 0:
#         await message.answer_sticker('CAACAgIAAxkBAAIQLGS6_AABY7w_kG2cNfLL5u9IL_TgvQACAgADEaneGLjjUpACUz9RLwQ')
#     elif answer == 1:
#         await message.answer_video('BAACAgIAAxkBAAIPrGVlGjCbIo9uuQIUbBGJtB2Btp2rAAKHNQACRsW4Sq4EAlt95oxIMwQ')
#     else:
#         await message.answer(f"{replies['friday'] + ending}")


@router.message(re_functions.kak_dela_answer_filter)
async def kak_dela_answer(message: types.Message) -> None:
    await message.answer(f"{replies['kak_dela']}")


# @router.message(re_functions.v_smysle_answer_filter)
# async def v_smysle_answer(message: types.Message) -> None:
#     await message.answer(f"{replies['v_smysle']}")
