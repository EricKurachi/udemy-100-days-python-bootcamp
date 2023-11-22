import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

#exercise = input("Tell me which exercises you did:")
exercise = input("Tell me which exercises you did: ")

request_body = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 75.5,
    "height_cm": 176,
    "age": 25
}

request = requests.post(exercise_endpoint, json=request_body, headers=headers)
request.raise_for_status()

exercise_json = request.json()["exercises"]

datetime_now = datetime.now()
date_now = datetime_now.strftime("%d/%m/%Y")
time_now = datetime_now.strftime("%X")

for exercise in exercise_json:
    post_params = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    workout_url = SHEET_ENDPOINT
    sheety_headers = {"Authorization": TOKEN}

    post_response = requests.post(url=workout_url, json=post_params, headers=sheety_headers)
    post_response.raise_for_status()

    print(post_response.text)
