import requests
API_KEY = "6c80c59a853895a44d8cc8998d9ad969"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for the given city."""
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric" 
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'Unable to fetch weather')}")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        print(f"\nWeather in {city_name}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def main():
    print("=== Command-line Weather App ===")
    city = input("Enter city name (or ZIP code): ").strip()

    if not city:
        print("Invalid input! Please enter a valid location.")
        return

    get_weather(city)

if __name__ == "__main__":
    main()
