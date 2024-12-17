from aiogram import Router
from aiogram.types import Message
from src.keyboards.keyboards import IaasKeyboardBuilder


router: Router = Router()


@router.message()
async def Iaas(message: Message):
    await message.reply(text="""
    Welcome to the IaaS section!
    choose one of the options below.
""",reply_markup=IaasKeyboardBuilder().as_markup)