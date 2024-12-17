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
    
    def get_server_counts_on_specific_region(self, region):
        url = f"{self.url}/ecc/v1/regions/{region}/servers"
        response = requests.get(url, headers=self.headers)
        return response.json()




