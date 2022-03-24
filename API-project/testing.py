import requests
import json

# An endpoint is basicly the url
def get_iss_data():
    endpoint = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=endpoint)
    data = response.json()
    longitude = data["iss_position"]['longitude']
    latitude = data["iss_position"]['latitude']
    return (latitude, longitude)
def print_sun():
    location = get_iss_data()
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={location[0]}&lng={location[1]}")
    data = response.json()
    with open("data.json", "w+") as data_file:
        json.dump(data, data_file, indent=4)
print_sun()