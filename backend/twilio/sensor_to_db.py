import requests
import json
import random


def sensor_data_to_db(data):
    url = "http://127.0.0.1:8000/deviceData/create"
    num = random.randint(1, 100)
    data["device_id"] = num
    data["user_id"] = num
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
