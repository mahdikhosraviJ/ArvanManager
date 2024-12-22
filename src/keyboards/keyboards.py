# Create your keyboards here.
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.filters.filters import IaasServerCallback

Start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Iaas 🚀", 
            callback_data=IaasServerCallback(IaasCommand="home").pack()
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
            callback_data=IaasServerCallback(IaasCommand="create").pack()
        ))
        self.add(InlineKeyboardButton(
            text="List VMs",
            callback_data=IaasServerCallback(IaasCommand="regions").pack()
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
    
    def Region_List(self, regions: list):
        for region in regions:
            self.add(InlineKeyboardButton(
                text=region,
                callback_data=IaasServerCallback(IaasCommand="servers", region=region).pack()
            ))
        self.adjust(2)
        self.add(InlineKeyboardButton(text="Back", callback_data=IaasServerCallback(IaasCommand="home").pack()))
        return self

    def Server_List(self, servers: list, region: str):
        for server in servers:
            self.add(InlineKeyboardButton(
                text=server["name"], 
                callback_data=IaasServerCallback(
                    command="server_info",
                    server_id=server["id"],
                    region=region
                ).pack()
            ))
        self.adjust(2)
        self.add(InlineKeyboardButton(text="Back", callback_data=IaasServerCallback(IaasCommand="regions").pack()))
        return self
        
    def Server_Actions(self, server_id: str, region: str):
        actions = [
            ("Delete", "delete"),
            ("Reboot", "reboot"),
            ("Power Off", "power_off"),
            ("Power On", "power_on"),
        ]
        for text, action in actions:
            self.add(InlineKeyboardButton(
                text=text,
                callback_data=IaasServerCallback(
                    command=action,
                    server_id=server_id,
                    region=region
                ).pack()
            ))
        self.adjust(2)
        self.add(InlineKeyboardButton(text="Back", callback_data=IaasServerCallback(IaasCommand="servers", region=region).pack()))
        return self