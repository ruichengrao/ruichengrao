from RpiMotorLib import RpiMotorLib
import RPi.GPIO as GPIO
import schedule
from time import sleep, time
from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
from geopy.geocoders import Nominatim
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
    difference = rounded_azm - int(row)
    angle_diff = round(difference, 3)
    
def runner():
    # Calculating step count
    step_count= angle_diff / 5.625
    global round_step
    round_step = round(step_count, 0)

    


GpioPins = [18, 23, 24, 25]


mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")


mymotortest.motor_run(GpioPins, .01, round_step, False, True, "half", .05)
