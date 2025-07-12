#Importazione delle varie librerie usate / Import of the various libraries 
import requests
import json
from dotenv import load_dotenv
import os

#Questa funziona parsa il file .env nella cartella e carica tutte le variabile come variabili d'ambiente (?) / This function parses the file ".env" in our folder and loads all the variables as ambient variables
load_dotenv()

#La mia API di openweather / Openweather API
API_KEY = os.getenv("API_KEY") 

#Questa funzione permette di inserire la città di cui si vuole il meteo, la trova grazie alla API di openweather  e grazie a response_city la jsonizziamo e inseriamo la latitudine e la longitutine nelle variabili lat e lon
#This Function allows to insert a city we want the wather of, we find it thanks to the openweather API and thanks to response_city we can json it and insert the data of lat and lon into the variables
def find_city(API_KEY):
    city_name = input("Type the city you want to know the weather of or type 'q' to exit the program: ")
    if city_name == "q" or city_name == "Q":
        exit()
    else:
     find_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name.lower()}&appid={API_KEY}"
     response_city = requests.get(find_city).json()
     lat = response_city[0]["lat"]
     lon = response_city[0]["lon"]
     return  city_name, lat, lon

#Essenziale per mandare il risultato di lat e lon in due variabili che verranno trasferite alla funzione give_meteo
#Essential to send the values of lat and lon into two variables that will be given to the give_meteo function
city_name, lat, lon = find_city(API_KEY)

#Questa funzione trova grazie alla latitudine e la longitudine la città che abbiamo cercato in precedenza e ci restituisce varie informazioni tramite json
#This function finds the city thanks to the lat and lon we got before and returns various information through json
def give_meteo(city_name, lat, lon, API_KEY):
    url = url= f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    meteo = requests.get(url).json()
    name = meteo["name"]
    weather = meteo["weather"][0]["description"]
    temp_K = meteo["main"]["temp"]
    temp_C = temp_K - 273.15
    humidity = meteo["main"]["humidity"]
    wind_speed = meteo["wind"]["speed"]
    print("-" * 40)
    print(f"📍 Current weather for: {city_name}\n Weather: {weather}\n 🌡️  Temperature in Celsius: {round(temp_C, 2)}\n 💧 Humidity: {humidity}%\n 🌬️  Wind: {wind_speed} km/s")
    print("-" * 40)



#Ciclo per permettere di cercare più città senza dover riavviare il programma
#Cycle that allows to search more city without restarting the program
give_meteo(city_name, lat, lon, API_KEY)
while True: 
     city_name, lat, lon = find_city(API_KEY)
     give_meteo(city_name, lat, lon, API_KEY)

