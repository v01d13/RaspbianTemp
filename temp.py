import sys
import Adafruit_DHT
import time
from os import system, name
from datetime import date, datetime

def temp():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    date_now = date.today()
    now = datetime.now()
    time_now = now.strftime("%H:%M")
    return date_now, time_now, humidity, temperature
