from aiogram.filters import BaseFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')


# Create your filters here.
class IsAdmin(BaseFilter):
    """
    This filter checks if the user is an admin or not.
    """ 
    def __init__(self):
        self.admins = os.getenv("INITIAL_ADMIN_IDS") # output like this [5894416619, 5894416619]
        self.admins = self.admins.replace("[", "").replace("]", "").split(",")
        self.admins = [int(admin) for admin in self.admins]

    async def check(self, message: Message) -> bool:
        if message.from_user.id in self.admins:
            return True
        else:
            return False
    
    async def __call__(self, message: Message) -> bool:
        return await self.check(message)

class IsCallbackFromAdmin(BaseFilter):
    def __init__(self):
        self.admins = os.getenv("INITIAL_ADMIN_IDS") # output like this [5894416619, 5894416619]
        self.admins = self.admins.replace("[", "").replace("]", "").split(",")
        self.admins = [int(admin) for admin in self.admins]

    async def check(self, callback_query: CallbackQuery) -> bool:
        if callback_query.from_user.id in self.admins:
            return True
        else:
            return False 

    async def __call__(self, callback_query: CallbackQuery) -> bool:
        return await self.check(callback_query)

class IaasServerCallback(CallbackData, prefix="Iaas"):
    IaasCommand: str
    server_id: str = None
    region: str = None

class IaasFilter(BaseFilter):
    async def check(self, callback_query: CallbackQuery) -> bool:
        if IaasServerCallback.unpack(callback_query.data).IaasCommand:
            return True
        else:
            return False

    async def __call__(self, callback_query: CallbackQuery) -> bool:
        return await self.check(callback_query)
