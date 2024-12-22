from aiogram import Router, F
from aiogram.types import CallbackQuery
from src.keyboards.keyboards import IaasKeyboardBuilder
from src.filters.filters import IaasServerCallback
from aiogram.filters import magic_data
from src.ArvanAPI.Iaas import IAAS

router: Router = Router()
iaas_client = IAAS()


@router.callback_query(IaasServerCallback.filter(F.IaasCommand == "home"))
async def Iaas_Home_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        text="Welcome to the IaaS section!\nChoose one of the options below:",
        reply_markup=IaasKeyboardBuilder().Home().as_markup()
    )

@router.callback_query(IaasServerCallback.filter(F.command == "list"))
async def List(callback: CallbackQuery, callback_data: IaasServerCallback):
    await callback.message.answer(text="List of servers:", reply_markup=IaasKeyboardBuilder().Server_List(servers=[{"id": "1", "name": "Server 1"}, {"id": "2", "name": "Server 2"}]).as_markup())

@router.callback_query(IaasServerCallback.filter(F.command == "regions"))
async def Regions(callback: CallbackQuery, callback_data: IaasServerCallback):
    await callback.answer()
    regions = iaas_client.get_regions()
    await callback.message.edit_text(
        text="Select a region:",
        reply_markup=IaasKeyboardBuilder().Region_List(regions=regions).as_markup()
    )

@router.callback_query(IaasServerCallback.filter(F.command == "servers"))
async def ListServers(callback: CallbackQuery, callback_data: IaasServerCallback):
    await callback.answer()
    try:
        servers = iaas_client.get_servers(callback_data.region)
        await callback.message.answer(
            text=f"Servers in {callback_data.region}:",
            reply_markup=IaasKeyboardBuilder().Server_List(
                servers=servers,
                region=callback_data.region
            ).as_markup()
        )
    except Exception as e:
        await callback.message.answer(f"Error fetching servers: {str(e)}")

@router.callback_query(IaasServerCallback.filter(F.command == "server_info"))
async def ServerInfo(callback: CallbackQuery, callback_data: IaasServerCallback):
    await callback.answer()
    try:
        server = iaas_client.get_server_info(callback_data.region, callback_data.server_id)
        info_text = (
            f"Server: {server.get('name')}\n"
            f"Status: {server.get('status')}\n"
            f"Region: {callback_data.region}"
        )
        await callback.message.answer(
            text=info_text,
            reply_markup=IaasKeyboardBuilder().Server_Actions(
                server_id=callback_data.server_id,
                region=callback_data.region
            ).as_markup()
        )
    except Exception as e:
        await callback.message.answer(f"Error fetching server info: {str(e)}")

@router.callback_query(IaasServerCallback.filter(F.command == "delete"))
async def DeleteServer(callback: CallbackQuery, callback_data: IaasServerCallback):
    await callback.answer()
    try:
        result = iaas_client.delete_server(callback_data.region, callback_data.server_id)
        if result:
            await callback.message.answer("Server deletion initiated successfully")
            await Regions(callback, callback_data)
        else:
            await callback.message.answer("Failed to delete server")
    except Exception as e:
        await callback.message.answer(f"Error deleting server: {str(e)}")