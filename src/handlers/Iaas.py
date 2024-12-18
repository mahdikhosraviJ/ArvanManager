from aiogram import Router,F
from aiogram.types import CallbackQuery
from src.keyboards.keyboards import IaasKeyboardBuilder
from src.filters.filters import IsCallbackFromAdmin, IaasServerCallback

router: Router = Router()

@router.callback_query(IaasServerCallback.filter(F.command == "home"))
async def Home(callback: CallbackQuery, callback_data: IaasServerCallback):
    await callback.answer()
    await callback.message.answer(text="""
    Welcome to the IaaS section!
    Choose one of the options below:
""", reply_markup=IaasKeyboardBuilder().Home().as_markup())

@router.callback_query(IaasServerCallback.filter(F.command == "list"))
async def List(callback: CallbackQuery, callback_data: IaasServerCallback):
    await callback.message.answer(text="List of servers:", reply_markup=IaasKeyboardBuilder().Server_List(servers=[{"id": "1", "name": "Server 1"}, {"id": "2", "name": "Server 2"}]).as_markup())