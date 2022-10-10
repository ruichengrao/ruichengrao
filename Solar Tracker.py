import csv
from pyephem_sunpath.sunpath import sunpos
from datetime import date, datetime
from altitudo import altitudo
from geopy.geocoders import Nominatim
import schedule, time


def job():

    #getting lon/lat
    geolocator = Nominatim(user_agent="Solar Tracker")
    location = geolocator.geocode("201 Walt Banks Rd, Peachtree City, GA 30269")
    exact_date = datetime.now()
    global lat
    lat = location.latitude
    global lon
    lon = location.longitude
    global elv
    elv = altitudo(lat=lat, lon=lon)
    tz = -4
    global rounded_alt
    global rounded_azm
    alt, azm = sunpos(exact_date, lat, lon, tz, dst=True)
    rounded_alt = round(alt,5)
    rounded_azm = round(azm,5)
    global data
    data = [str(exact_date),str(lat),str(lon),str(elv),str(rounded_alt) + ("°"),str(rounded_azm) + ("°")]
job()
def csv_log():
    header = ['Date', 'Latitude', 'Longitude','Elvation','Altitude',"Azimuth"]
    filename = 'Solar_Tracking.csv'
    with open(filename, 'w', newline="" ) as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerow(data) 
    
csv_log()
   

schedule.every(3).seconds.do(job)
schedule.every(3).seconds.do(csv_log)

while True:
    schedule.run_pending()
    time.sleep(1)
