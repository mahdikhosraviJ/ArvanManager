import requests
from dotenv import load_dotenv
import os
from ArvanAPI import ArvanAPI


load_dotenv()



class IAAS:
    def __init__(self):
        self.regions = ["ir-thr-ba1","ir-thr-fr1","ir-tbz-sh1","ir-thr-si1"]
        self.url = ArvanAPI.BASE_URL
        self.api_key = os.getenv("API_KEY")
        self.headers = {
            "Authorization": self.api_key,
            "Accept": "application/json"
        }

    def get_regions(self):
        return self.regions
    
    def get_servers(self, region):
        url = f"{self.url}/ecc/v1/regions/{region}/servers"
        response = ArvanAPI.fetch_data(url)
        return response.json()

    def get_server_info(self, region, server_id):
        url = f"{self.url}/ecc/v1/regions/{region}/servers/{server_id}"
        response = ArvanAPI.fetch_data(url)
        return response.json()
    
    def delete_server(self, region, server_id, force_delete=False, reasons=None):
        url = f"{self.url}/ecc/v1/regions/{region}/servers/{server_id}"
        payload = {
            "forceDelete": force_delete,
            "DeleteServerReasons": reasons or []
        }
        response = requests.delete(url, headers=self.headers, json=payload)
        return response.json()    




