from dotenv import load_dotenv
import os
import requests

load_dotenv(dotenv_path='../.env')

API_BASE_URL = "https://napi.arvancloud.ir"

class ArvanAPI:
    BASE_URL = API_BASE_URL

    @staticmethod
    async def fetch_data(endpoint, server_id=None, headers=None):
        url = f"{ArvanAPI.BASE_URL}{endpoint}"
        if server_id:
            url = url.format(server_id=server_id)
        async with requests.get(url, headers=headers) as response:
            response.raise_for_status()
            return await response.json()
