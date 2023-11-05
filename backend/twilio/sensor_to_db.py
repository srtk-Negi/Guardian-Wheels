import requests
import json


def sensor_data_to_db(data):
    url = "http://127.0.0.1:8000/deviceData/create"
    data["device_id"] = 2
    data["user_id"] = 2
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
