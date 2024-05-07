from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(text=f"Salom {message.from_user.first_name}!")