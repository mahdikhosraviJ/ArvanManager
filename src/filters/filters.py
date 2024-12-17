from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')


# Create your filters here.
class IsAdmin(BaseFilter):
    def __init__(self):
        self.admins = os.getenv("INITIAL_ADMIN_IDS") # output like this [5894416619, 5894416619]
        self.admins = self.admins.replace("[", "").replace("]", "").replace(" ", "").split(",")
        self.admins = [int(admin) for admin in self.admins]

    async def check(self, message: Message) -> bool:
        if message.from_user.id in self.admins:
            return True
        else:
            return False

class IsCallbackFromAdmin(BaseFilter):
    def __init__(self):
        self.admins = os.getenv("INITIAL_ADMIN_IDS") # output like this [5894416619, 5894416619]
        self.admins = self.admins.replace("[", "").replace("]", "").replace(" ", "").split(",")
        self.admins = [int(admin) for admin in self.admins]

    async def check(self, callback_query: CallbackQuery) -> bool:
        if callback_query.from_user.id in self.admins:
            return True
        else:
            return False 
