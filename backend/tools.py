import requests

# Directly set your OpenWeather key
OPENWEATHER_API_KEY = "0239cc0da50579678b18fd19ab8cfb54"

def get_weather(city: str) -> str:
    if not OPENWEATHER_API_KEY:
        return "Weather API key is missing."

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&units=metric&appid={OPENWEATHER_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if response.status_code != 200:
            return f"Could not fetch weather for {city}. Please check the city name."

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"It’s {temp}°C with {description} in {city}."

    except Exception:
        return "Weather service is temporarily unavailable."
