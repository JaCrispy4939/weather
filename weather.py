#Made by Ja'Crispy4939, please dont steal the code and name it yours
#Enjoy :)

import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import os
import time
import lxml.html

page = requests.get("https://weather.com/weather/today/l/57312336018afbd8918d5eefe6ccd5308696bf6d8056348868a1d39d80709a34")
soup=BeautifulSoup(page.content,"html.parser")
lxml = lxml.html.fromstring(page.content)

def printTodaysWeather():
    #youll have to go to https://weather.com/weather and search for your city than copy and paste the URL below where mine is
    page = requests.get("https://weather.com/weather/today/l/57312336018afbd8918d5eefe6ccd5308696bf6d8056348868a1d39d80709a34")
    soup=BeautifulSoup(page.content,"html.parser")
    current_temperature = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/span/text()""")[0]
    current_state = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/div/text()""")[0]
    current_precip = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[3]/span/text()""")[0]
    current_high = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[2]/div[1]/div[2]/span[1]/text()""")[0]
    current_low = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[2]/div[1]/div[2]/span[2]/text()""")[0]
    current_realfeel = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[1]/div[1]/span[1]/text()""")[0]
    sunset_time = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[1]/div[2]/div/div/div/div[2]/p/text()""")[0]
    sunrise_time = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[1]/div[2]/div/div/div/div[1]/p/text()""")[0]
    location = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/header/h2/text()""")[0]
    humidity = lxml.xpath("""//*[@id="todayDetails"]/section/div[2]/div[3]/div[2]/span/text()""")[0]


    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%m/%d/%Y")
    os.system("cls")
    print("Date: " + d1)
    print("Location: " + str(location))
    print("Current State: " + current_state)
    print("Rain: " + str(current_precip))
    print("Current Temp: " + current_temperature)
    print("Current Realfeel: " + current_realfeel)
    print("Humidity: " + humidity)
    print("High/Low: " + current_high + " / " + current_low)
    print("Sunrise Time: " + str(sunrise_time))
    print("Sunset Time: " + str(sunset_time))

    choice = input("\n1. Update 2. Exit\nOption: ")
    if choice == "1":
        print("Updating")
        time.sleep(.5)
        print(".")
        time.sleep(.5)
        print("..")
        time.sleep(.5)
        print("...")
        time.sleep(.5)
        printTodaysWeather()
    elif choice == "2":
        print("Exiting")
        time.sleep(2)
        os.system("cls")
        quit()

printTodaysWeather()