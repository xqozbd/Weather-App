#Import Libraries
import requests
import math

#Key to the API
API_KEY = "7a5bb5a0a30e456f925224328250902"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

#Talk to the weather API
def get_weather_data(city, state):
    location = f"{city}, {state}"
    params = {
        "key": API_KEY,
        "q": location,
        "days": 1
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}: {response.text}")
        return None


