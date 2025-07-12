#Importazione delle varie librerie usate / Import of the various libraries 
import requests
import json
from dotenv import load_dotenv
import os

#Questa funziona parsa il file .env nella cartella e carica tutte le variabile come variabili d'ambiente (?) / This function parses the file ".env" in our folder and loads all the variables as ambient variables
load_dotenv()

#La mia API di openweather / Openweather API
API_KEY = os.getenv("API_KEY") 

#Questo blocco permette di inserire la città di cui si vuole il meteo, la trova grazie alla API di openweather  e grazie a response_city la jsonizziamo e inseriamo la latitudine e la longitutine nelle variabili lat e lon
#This block allows to insert a city we want the wather of, we find it thanks to the openweather API and thanks to response_city we can json it and insert the data of lat and lon into the variables
city_name= input("Type the city you want to know the weather of: ")
limit= 2
find_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name.lower()}&limit={limit}&appid={API_KEY}"
response_city = requests.get(find_city).json()
lat = response_city[0]["lat"]
lon = response_city[0]["lon"]

#Questo blocco trova grazie alla latitudine e la longitudine la città che abbiamo cercato in precedenza e ci restituisce varie informazioni tramite json
#This block finds the city thanks to the lat and lon we got before and returns various information through json
part = 1
url= f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
meteo = requests.get(url).json()

#Qui prendiamo solo le informazioni che vogliamo e le salviamo in delle variabili e poi stampiamo
#We takes only the informations we wants and we save them into variables, then we print
name = meteo["name"]
weather = meteo["weather"][0]["description"]
temp_K = meteo["main"]["temp"]
temp_C = temp_K - 273.15
humidity = meteo["main"]["humidity"]
wind_speed = meteo["wind"]["speed"]
print(f"📍 Current weather for {name}\n Weather: {weather}\n 🌡️ Temperature in Celsius: {round(temp_C, 2)}\n 💧 Humidity: {humidity}%\n 🌬️ Wind: {wind_speed} km/s")
