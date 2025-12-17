from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# CORS setup
origins = ["http://localhost:5173", "http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WeatherRequest(BaseModel):
    city: str

# Current weather endpoint
@app.post("/weather")
async def get_weather(request: WeatherRequest):
    city_name = request.city
    api_key = "0239cc0da50579678b18fd19ab8cfb54"

    # Current weather
    current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    # 5-day forecast
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"

    try:
        # Current weather
        current_resp = requests.get(current_url).json()
        if current_resp.get("cod") != 200:
            return {"error": current_resp.get("message", "City not found")}

        current_weather = {
            "city": city_name,
            "temperature": current_resp["main"]["temp"],
            "description": current_resp["weather"][0]["description"],
        }

        # Forecast
        forecast_resp = requests.get(forecast_url).json()
        forecast_list = []
        for item in forecast_resp["list"][:8]:  # next 24 hours (3-hour interval × 8)
            forecast_list.append({
                "time": item["dt_txt"].split(" ")[1][:5],  # HH:MM
                "temperature": item["main"]["temp"],
                "description": item["weather"][0]["description"]
            })

        return {"current": current_weather, "forecast": forecast_list}

    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"status": "Weather backend running"}
