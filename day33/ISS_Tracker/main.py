from datetime import *
import smtplib
import requests
import time

MY_LAT = -34.901112
MY_LONG = -56.164532
EMAIL_SENDER = "pythonmailtest50@gmail.com"
PASSWORD_SENDER = "zpge cgrd exyo xjxg"
EMAIL_RECIVER = "python0891273654@hotmail.com"

def is_near_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    lat_dif = MY_LAT - iss_lat
    long_dif = MY_LONG - iss_long
    rigth_lat = abs(lat_dif) < 5
    rigth_long = abs(long_dif) < 5

    return rigth_lat and rigth_long


def is_currently_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "America/Argentina/Buenos_Aires"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour
    return hour_now < sunrise or hour_now > sunset


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_SENDER, password=PASSWORD_SENDER)
        connection.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=EMAIL_RECIVER,
            msg=f"Subject:Look up\n\nLook up"
        )


while True:
    if is_near_me() and is_currently_dark():
        send_email()
    time.sleep(60)