import sys
import Adafruit_DHT
import time
from os import system, name
from datetime import date, datetime

def clear():
	system('clear')

while True:
	try:
		clear()
		humidity, temperature = Adafruit_DHT.read_retry(22, 4)
		date = date.today()
		now = datetime.now()
		time_now = now.strftime("%H:%M")
		print("Date: " + str(date))
		print("Time: ", time_now)
		print("Temperature: " + str(temperature) + " C")
		print("Humidity: "+ str(humidity) + " %")
		field = ['']
		time.sleep(10)
	except RuntimeError as e:
		print("Error: ", e.args)
