from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def send_help(message: types.Message):
    await message.answer(text="Men sizga yordam beraman")