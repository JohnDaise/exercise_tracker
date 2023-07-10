import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Details
GENDER = "male"
WEIGHT = 88.45
HEIGHT = 180.34
AGE = 35


NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2"
SHEETY_URL = "https://api.sheety.co"


USERNAME = "cd80ca037dfac9a238904d4dd1642daa"
PROJECT_NAME = "pythonMyWorkouts"
SHEET_NAME = "workouts"

natural_lang_exercise_endpoint = f"{NUTRITIONIX_URL}/natural/exercise"
sheety_post_endpoint = f"{SHEETY_URL}/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"


exercise_query = input("Tell me what exercise you did: ")

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY")
}

nutrx_params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}


nutrix_response = requests.post(url=natural_lang_exercise_endpoint, headers=headers, json=nutrx_params)
nutrix_response.raise_for_status()

nutrix_exercise_data = nutrix_response.json()["exercises"]

now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")


for exercise in nutrix_exercise_data:
    sheet_params = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_post_endpoint, json=sheet_params)
    sheety_response.raise_for_status()

print(sheety_response.text)





