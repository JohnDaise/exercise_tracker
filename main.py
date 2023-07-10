import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Details
GENDER = "male"
WEIGHT = 88.45
HEIGHT = 180.34
AGE = 35


NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2"
natural_lang_exercise_endpoint = f"{NUTRITIONIX_URL}/natural/exercise"


exercise_query = input("Tell me what exercise you did: ")

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY")
}

params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=natural_lang_exercise_endpoint, headers=headers, json=params)
response.raise_for_status()

data = response.json()

# print(data)
# quit
