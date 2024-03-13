from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
sheet_data = DataManager.get_info()

for row in sheet_data:

    if row["iataCode"] == "":
        iataCode = FlightSearch.search_city(row["city"])
        row["iataCode"] = iataCode
        DataManager.update_info(row)

    data = FlightSearch.search_flight(row["iataCode"])

    print(f"{row["city"]}: {data["price"]}")
    
    if int(data["price"]) < int(row["lowestPrice"]):

        message = FlightData().get_message(data)

        NotificationManager.send_message(message)

        print(message)




