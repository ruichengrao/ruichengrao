import schedule
import RPi.GPIO as GPIO
from time import sleep
from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
from geopy.geocoders import Nominatim
from suntime import Sun, SunTimeException
from datetime import date
import csv


#getting lon/lat 
geolocator = Nominatim(user_agent="Solar Tracker")
location = geolocator.geocode("201 Walt Banks Rd, Peachtree City, GA 30269")
global lat
lat = location.latitude
global lon
lon = location.longitude

#getting date
exact_date = datetime.now()

#getting azimuth
tz = -4
global rounded_alt
global rounded_azm
alt, azm = sunpos(exact_date, lat, lon, tz, dst=False)
rounded_alt = round(alt,5)
rounded_azm = round(azm,5)


#for sunrise and sunset (worry later)
#getting sunrise/sunset
latitude = lat
longitude = lon

sun = Sun(latitude, longitude)

# date object of today's date
today = date.today()
 
year = today.year
month = today.month
day = today.day

# On a special date in your machine's local time zone
abd = datetime.date(year, month, day)
abd_sr = sun.get_local_sunrise_time(abd)
abd_ss = sun.get_local_sunset_time(abd)


# csv file name
filename = "Solar_Tracking.csv"
#currentRow = 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
index2 = csvreader.line_num - 2
index1 = csvreader.line_num - 3

 
for row in rows[index1:index2]:
    # parsing each column of a row
    difference = rounded_azm - float(row)
    angle_diff = round(difference, 3)
    

#setting up pins


DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 64   # Steps per Revolution 2038 (360 / 5.625)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

def runner():
    # Calculating step count
    step_count= angle_diff / 5.625

    roundedSteps = round(step_count, 0)
    delay = 0.0156
    for x in range(roundedSteps):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

runner()

schedule.every(5).minutes.do(runner) #set to the same time as azimuth calcuating rate






#goes back when sun sets

#sleep(.5)
#GPIO.output(DIR, CCW)
#for x in range(step_count):
    #GPIO.output(STEP, GPIO.HIGH)
    #sleep(delay)
    #GPIO.output(STEP, GPIO.LOW)
    #sleep(delay)

#
#  - motor 64 steps per revolution (full spin)
#  
