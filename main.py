import requests
from datetime import datetime
import os

# sheety_user = "dilip84"
# sheety_password = "ZD&PBL0h&%Q0dw#7K"
sheety_user = os.environ["sheety_user"]
sheety_password = os.environ["sheety_password"]
GENDER = "male"
WEIGHT_KG = 54
AGE = 21

# APP_ID = "6d6f0859"
# APP_KEY = "7d5c6b0f52b32e4c4c5f3778a14be34f"
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {"x-app-id": APP_ID, "x-app-key": APP_KEY}
api_data = {"query": input("Tell me which exercises you did:"), "gender": GENDER, "weight_kg": WEIGHT_KG, "age": AGE}
response = requests.post(url=api_endpoint, json=api_data, headers=headers)
data = response.json()

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = str(today).split(" ")[1].split(".")[0]
# now_time = datetime.now().strftime("%X")

sheety_post_endpoint = os.environ["sheety_post_endpoint"]
for exercise in data["exercises"]:
    data_dict = {"workout": {"date": today_date, "time": today_time, "exercise": exercise["name"].title(),
                             "duration": exercise["duration_min"], "calories": exercise["nf_calories"]}}
    response = requests.post(url=sheety_post_endpoint, json=data_dict, auth=(sheety_user, sheety_password))
    print(response.text)
