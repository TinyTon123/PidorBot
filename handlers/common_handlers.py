from aiogram import Router, types
from aiogram.filters import CommandStart

from dictionary.replies import replies

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: types.Message):
    await message.answer(text=f"{replies['/start']}")
