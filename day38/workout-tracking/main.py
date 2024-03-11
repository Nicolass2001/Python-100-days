import requests
from datetime import datetime

APP_ID = "cac0e03c"
APP_KEY = "944966f93eb78c67c9ad51e7ac20ac37"
MY_WEIGHT = 65
MY_HEIGHT = 170
MY_AGE = 22

SHEETY_TOKEN = "Basic bnBlcmVpcmE6ZDVuTzJNekV5RXgwQ1BxUDNIdk4="

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/c4517082febc51336ae67b96628cfe0f/workoutTracking/workouts"

query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": query,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()

exercises = data["exercises"]

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

headers = {
    "Authorization": SHEETY_TOKEN,
}

for exercise in exercises:

    
    exercise_name = str(exercise["name"]).title()
    exercise_duration = round(float(exercise["duration_min"]))
    exercise_calories = round(float(exercise["nf_calories"]))

    sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=headers)
    response.raise_for_status()