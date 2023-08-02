import requests
from .key import api_key
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }
    try: 
      response = requests.get(base_url, params=params)
      data = response.json()
      print(data)
      if response.status_code == 200:
          city_name = data["name"]
          main_weather = data["weather"][0]["main"]
          description = data["weather"][0]["description"]
          temperature = data["main"]["temp"]
          feels_like = data["main"]["feels_like"]
          temp_min =data["main"]["temp_min"]
          temp_max =data["main"]["temp_max"]
          humidity = data["main"]["humidity"]
          wind_speed = data["wind"]["speed"]
          pressure = data["main"]["pressure"]
          return city_name,main_weather,description,temperature,humidity,wind_speed,pressure,feels_like,temp_min,temp_max
    except Exception as e:
        print(e)
        