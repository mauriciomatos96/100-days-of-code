import requests
import datetime as dt

NUTRITIONIX_API_KEY = "e5c0f2a885778c6540cd96044f61d06d"
NUTRITIONIX_APP_ID = "6a83c1c1"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 105,
    "height_cm": 190,
    "age": 25
}

today = dt.datetime.today()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

response = requests.post(url=nutritionix_endpoint, headers=headers, json=parameters)
result = response.json()


sheety_endpoint = "https://api.sheety.co/50be8a6d6d45fb4f33d46550838a7ddf/workoutTracking/workouts"


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=("punisher96", "a159875321"))
    print(sheet_response.text)