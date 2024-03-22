import requests
from flight_data import FlightData

ENDPOINT_SEARCH_CITY = "https://api.tequila.kiwi.com/locations/query"
ENDPOINT_SEARCH_FLIGHT = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "GwY21VAGIFubu1aHsBGdn_d-bl8FACGd"

class FlightSearch:

    def search_city(cityName):
        headers = {
            "apikey": API_KEY
        }

        parameters = {
            "term": cityName,
            "location_types": "city"
        }

        response = requests.get(url=ENDPOINT_SEARCH_CITY, params=parameters, headers=headers)
        return response.json()["locations"][0]["code"]
    
    def search_flight(iataCode):
        parameters = FlightData().get_json(iataCode)

        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url=ENDPOINT_SEARCH_FLIGHT, params=parameters, headers=headers)
        return response.json()["data"][0]


    
    pass