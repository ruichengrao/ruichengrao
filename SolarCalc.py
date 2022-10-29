#import package/modules
import csv
from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
from geopy.geocoders import Nominatim
import schedule

#csv header/stated file
header = ["Azimuth"]
filename = 'Solar_Tracking.csv'
a = True

#job function will run after every set time
def job():

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
    #csv data
    global data
    data = [str(rounded_azm)]
    global a
    with open(filename, 'a', newline="\n") as file:
        csvwriter = csv.writer(file)
        #skips header line after the first run
        if a:
          csvwriter.writerow(header)
          a = False
        csvwriter.writerow(data)

job()

#call every x min/sec

schedule.every(5).minutes.do(job)


while True:
    schedule.run_pending()
  
