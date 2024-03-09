import requests
from twilio.rest import Client


ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = -34.901112
MY_LON = -56.164532
APPID = "253682c0bd759acfb4255d4aa08c3dd7"
account_sid = "ACd378be490e791258d4c04917bcc7432b"
auth_token = "fa942d2fbfca23ed51879b0292afcca4"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": APPID,
    "cnt": 4,
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
wheather_data = response.json()
rain_condition_codes = [item["weather"][0]["id"] for item in wheather_data["list"] if item["weather"][0]["id"] < 700]
if len(rain_condition_codes) > 0:
    print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☂️",
                        from_="+19497104345",
                        to="+59891017827"
                    )

    print(message.status)

