import requests
from dotenv import load_dotenv
import os

from src.ArvanAPI import ArvanAPI

arvanapi = ArvanAPI


load_dotenv()

class IAAS:
    def __init__(self):
        self.regions = ["ir-thr-ba1","ir-thr-fr1","ir-tbz-sh1","ir-thr-si1"]
        self.url = arvanapi.BASE_URL
        self.api_key = os.getenv("API_KEY")
        self.headers = {
            "Authorization": self.api_key,
            "Accept": "application/json"
        }

    def get_regions(self):
        return self.regions
    
    def get_servers(self, region):
        url = f"{self.url}/ecc/v1/regions/{region}/servers"
        response = arvanapi.fetch_data(url)
        return response.json()

    def get_server_info(self, region, server_id):
        url = f"{self.url}/ecc/v1/regions/{region}/servers/{server_id}"
        response = arvanapi.fetch_data(url)
        return response.json()
    
    def delete_server(self, region, server_id, force_delete=False, reasons=None):
        url = f"/ecc/v1/regions/{region}/servers/{server_id}"
        payload = {
            "forceDelete": force_delete,
            "DeleteServerReasons": reasons or []
        }
        response = arvanapi.delete_data(url, headers=self.headers, json=payload)
        return response.json() if response else None

    def create_server(self, region, name, flavor_id, image_id, disk_size=None, network_id=None, 
                     security_groups=None, key_name=None, ha_enabled=False):
        """Create a new server in the specified region"""
        url = f"/ecc/v1/regions/{region}/servers"
        
        payload = {
            "name": name,
            "flavor_id": flavor_id,
            "image_id": image_id,
            "disk_size": disk_size,
            "ha_enabled": ha_enabled
        }
        
        if network_id:
            payload["network_id"] = network_id
            
        if security_groups:
            payload["security_groups"] = [{"name": sg} for sg in security_groups]
            
        if key_name:
            payload["key_name"] = key_name

        response = ArvanAPI.post_data(url, headers=self.headers, json=payload)
        return response.json() if response else None




