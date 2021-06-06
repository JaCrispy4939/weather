#Made by Ja'Crispy4939, please dont steal the code and name it yours
#Enjoy :)

import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import os
import time

def printTodaysWeather():
    #youll have to go to https://weather.com/weather and search for your city than copy and paste the URL below where mine is
    page = requests.get("https://weather.com/weather/today/l/57312336018afbd8918d5eefe6ccd5308696bf6d8056348868a1d39d80709a34")
    soup=BeautifulSoup(page.content,"html.parser")
    soup_condition=BeautifulSoup(page.content,"html.parser")
    current_temperature = soup.find(class_="CurrentConditions--tempValue--3KcTQ").text
    current_state = soup_condition.find(class_="CurrentConditions--phraseValue--2xXSr").text
    current_precip = soup.find(class_="CurrentConditions--precipValue--RBVJT")
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%m/%d/%Y")

    print("Date: " + d1)
    print(current_state)
    print("Rain: " + str(current_precip))
    print("Current Temp: " + current_temperature)

printTodaysWeather()