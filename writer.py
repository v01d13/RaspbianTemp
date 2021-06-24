import csv
from datetime import date
import os


def writeData(date, time, temperature, humidity):
    with open('temp.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, temperature, humidity])


def writeDaily(date, time, temperature, humidity):
    os.chdir(os.path.join(os.getcwd(), 'daily'))
    date = date.today()
    datestr = str(date) + '.csv'
    with open(datestr, 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, temperature, humidity])
    os.chdir('../')
