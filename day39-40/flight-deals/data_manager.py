import requests

ENDPOINT = "https://api.sheety.co/c4517082febc51336ae67b96628cfe0f/flightDeals/prices"

class DataManager:

    def get_info():
        response = requests.get(url=ENDPOINT)
        response.raise_for_status()
        return response.json()["prices"]
    
    def update_info(updated_info):
        body = {
            "price": {
                "iataCode": updated_info["iataCode"]
            }
        }
        response = requests.put(url=f"{ENDPOINT}/{updated_info["id"]}", json=body)
        response.raise_for_status()