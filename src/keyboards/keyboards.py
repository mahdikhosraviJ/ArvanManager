# Create your keyboards here.
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
Start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Iaas 🚀", callback_data="Iaas"),
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
        self.add(InlineKeyboardButton(text="Create VM", callback_data="Iaas_Server_Create"))
        self.add(InlineKeyboardButton(text="List VMs", callback_data="Iaas_Server_List"))
        self.add(InlineKeyboardButton(text="Delete VM", callback_data="Iaas_Server_Delete"))
        self.add(InlineKeyboardButton(text="Back", callback_data="Start"))
        return self
    
    def Server_Create(self):
        self.add(InlineKeyboardButton(text="Back", callback_data="Iaas"))
        return self
    
    def Server_List(self, servers: list):
        for server in servers:
            self.add(InlineKeyboardButton(text=server["name"], callback_data=f"Iaas_Server_{server['id']}"))
        self.add(InlineKeyboardButton(text="Back", callback_data="Iaas"))
        return self