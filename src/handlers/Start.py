from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from src.keyboards.keyboards import Start_keyboard
from src.filters.filters import IaasServerCallback

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        text="Welcome to Cloud Manager! Please select an option:",
        reply_markup=Start_keyboard
    )

@router.callback_query(F.data == "Start")
async def start_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        text="Welcome to Cloud Manager! Please select an option:",
        reply_markup=Start_keyboard
    )
