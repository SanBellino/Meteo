import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("API_KEY")
print(API_KEY)

city_name= input("Scrivi la città di cui ottenere il meteo: ")
limit= 2
find_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_KEY}"
response_city = requests.get(find_city).json()
print(response_city)
lat = response_city[0]["lat"]
lon = response_city[0]["lon"]

part = 1

url= f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
meteo = requests.get(url).json()
print(meteo)

name = meteo["name"]
weather = meteo["weather"][0]["description"]
temp_K = meteo["main"]["temp"]
temp_C = temp_K - 273.15
humidity = meteo["main"]["humidity"]
wind_speed = meteo["wind"]["speed"]
print(f"📍 Current weather for {name}\n Weather: {weather}\n 🌡️ Temperature in Celsius: {round(temp_C, 2)}\n 💧 Humidity: {humidity}%\n 🌬️ Wind: {wind_speed} km/s")
