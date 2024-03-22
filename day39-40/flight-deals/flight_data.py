from datetime import datetime, timedelta

FROM = "MVD"

class FlightData:

    def get_json(fly_to):
        today = datetime.now()
        date_from = (today + timedelta(days=1)).strftime("%d/%m/%Y")
        date_to = (today + timedelta(days=30*6)).strftime("%d/%m/%Y")
        return {
            "fly_from": FROM,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            # "max_stopovers": 0,
            "curr": "USD",
            "sort": "price",
            "limit": 1,
        }
    
    def get_message(data):
        price = data["price"]

        departure_city_name = data["cityFrom"]
        departure_airport_iata_code = data["cityCodeFrom"]
        arrival_city_name = data["cityTo"]
        arrival_airport_iata_code = data["cityCodeTo"]

        # ['yyyy', 'mm', 'dd']
        local_departure = data["local_departure"].split("T")[0].split("-")
        nights_in_dest = data["nightsInDest"]

        outbound_date = datetime(year=int(local_departure[0]), month=int(local_departure[1]), day=int(local_departure[2]))
        inbound_date = outbound_date + timedelta(days=nights_in_dest)

        return f"Only U$D {price} to fly from {departure_city_name}-{departure_airport_iata_code} to {arrival_city_name}-{arrival_airport_iata_code}, from {outbound_date.strftime("%Y-%m-%d")} to {inbound_date.strftime("%Y-%m-%d")}"
        