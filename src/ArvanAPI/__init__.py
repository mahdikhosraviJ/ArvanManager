from dotenv import load_dotenv
import os
import requests

load_dotenv(dotenv_path='../../.env')

API_BASE_URL = "https://napi.arvancloud.ir"

class ArvanAPI:
    BASE_URL = API_BASE_URL

    @staticmethod 
    def fetch_data(endpoint, headers=None, params=None):
        """Fetch data from API endpoint"""
        url = f"{ArvanAPI.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    @staticmethod
    def delete_data(endpoint, headers=None, json=None):
        """Delete data from API endpoint"""
        url = f"{ArvanAPI.BASE_URL}{endpoint}"
        try:
            response = requests.delete(url, headers=headers, json=json)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error deleting data: {e}")
            return None

    @staticmethod
    def post_data(endpoint, headers=None, json=None):
        """Post data to API endpoint"""
        url = f"{ArvanAPI.BASE_URL}{endpoint}"
        try:
            response = requests.post(url, headers=headers, json=json)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error posting data: {e}")
            return None
