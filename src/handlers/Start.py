from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from src.keyboards.keyboards import Start_keyboard

router: Router = Router()


@router.message(CommandStart())
async def Start(message: Message):
    await message.reply(text="""
    Welcome to the ArvanManager bot!
    You can use this bot to manage your ArvanCloud resources.
    To get started, click the buttons below.
""",reply_markup=Start_keyboard)
