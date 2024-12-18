# Create your keyboards here.
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.filters.filters import IaasServerCallback

Start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Iaas 🚀", 
            callback_data=IaasServerCallback(command="home").pack()
        ),
    ],
    [
        InlineKeyboardButton(text="CDN 📦", callback_data="CDN"),
        InlineKeyboardButton(text="VOD 🎥", callback_data="VOD"),
        InlineKeyboardButton(text="PaaS 🛠", callback_data="PaaS"),
    ],
    [
        InlineKeyboardButton(text="Live 📡", callback_data="Live"),
        InlineKeyboardButton(text="Storage ☁️", callback_data="Storage"),
        InlineKeyboardButton(text="Settings ⚙️", callback_data="Settings"),
    ]
])

class IaasKeyboardBuilder(InlineKeyboardBuilder):
    def __init__(self):
        super().__init__()
    
    def Home(self):
        self.add(InlineKeyboardButton(
            text="Create VM",
            callback_data=IaasServerCallback(command="create").pack()
        ))
        self.add(InlineKeyboardButton(
            text="List VMs",
            callback_data=IaasServerCallback(command="list").pack()
        ))
        self.add(InlineKeyboardButton(
            text="Delete VM",
            callback_data=IaasServerCallback(command="delete").pack()
        ))
        self.add(InlineKeyboardButton(
            text="Back",
            callback_data="Start"
        ))
        self.adjust(2)  # Arrange buttons in rows of 2
        return self
    
    def Server_Create(self):
        self.add(InlineKeyboardButton(text="Back", callback_data="Iaas"))
        return self
    
    def return_to_home(self):
        self.add(InlineKeyboardButton(text="Back", callback_data="Iaas"))
        return self
    
    def region_list

    def Server_List(self, servers: list):
        for server in servers:
            self.add(InlineKeyboardButton(text=server["name"], callback_data=f"Iaas_Server_{server['id']}"))
        self.adjust(2)
        self.add(InlineKeyboardButton(text="Back", callback_data="Iaas"))
        return self