from aiogram import Router, types, F

from dictionary.replies import replies

router: Router = Router()


@router.message(F.new_chat_members)
async def process_somebody_added(message: types.Message) -> None:
    for user in message.new_chat_members:
        # full_name берёт сразу имя и фамилию
        await message.reply(f"{replies['new_chat_members']}{user.full_name}!")


@router.message(F.left_chat_member)
async def process_somebody_left(message: types.Message) -> None:
    await message.reply(f"{replies['left_chat_member']}{message.left_chat_member.full_name} :(")
