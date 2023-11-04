import requests


def get_location():
    response = requests.get('https://ipinfo.io')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


if __name__ == "__main__":
    location_info = get_location()
    if location_info:
        print(f"IP Address: {location_info['ip']}")
        print(f"City: {location_info['city']}")
        print(f"Region: {location_info['region']}")
        print(f"Country: {location_info['country']}")
        print(f"Location: {location_info['loc']}")
    else:
        print("Unable to fetch location data.")
