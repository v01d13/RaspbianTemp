import time
import csv
import schedule
from os import system, name
from datetime import date
from temp import *
from writer import *

def newWrite():
    date_new = date.today()
    datestr = str(date_new) + '.csv'
    with open(datestr, 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Time', 'Temperature', 'Humidity'])

while True:
    system('clear')
    schedule.every().day.at('00:00').do(newWrite)
    date_today, time_now, temperature, humidity = temp()
    writeData(date_today, time_now, temperature, humidity)
    writeDaily(date_today, time_now, temperature, humidity)
    print("Date: ", date_today)
    print("Time: ", time_now)
    print("Temperature: ", temperature)
    print("Humidity: ", humidity)
    time.sleep(900)
    
