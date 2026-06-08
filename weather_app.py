import requests

# -----------------------------------------------
# Weather App - Fetches Temperature, Humidity, Wind Speed
# API: OpenWeatherMap (https://openweathermap.org/api)
# -----------------------------------------------

API_KEY = "f368957185045f0cf75fbaef2b20791c"   # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    """Fetch weather data for a given city and display selected fields."""

    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"       # Use "imperial" for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract only the 3 required fields
        temperature = data["main"]["temp"]
        humidity    = data["main"]["humidity"]
        wind_speed  = data["wind"]["speed"]

        # Display output in terminal
        print("\n========== Weather Report ==========")
        print(f"  City        : {city_name.title()}")
        print(f"  Temperature : {temperature} °C")
        print(f"  Humidity    : {humidity} %")
        print(f"  Wind Speed  : {wind_speed} m/s")
        print("=====================================\n")

    elif response.status_code == 401:
        print("\n[ERROR] Invalid API key. Please check your API_KEY.")
    elif response.status_code == 404:
        print(f"\n[ERROR] City '{city_name}' not found. Please check the city name.")
    else:
        print(f"\n[ERROR] Failed to fetch data. Status code: {response.status_code}")


# -----------------------------------------------
# Main Program
# -----------------------------------------------
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
