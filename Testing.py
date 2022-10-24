# importing csv module
import csv
from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
from altitudo import altitudo
from geopy.geocoders import Nominatim

#getting lon/lat 
geolocator = Nominatim(user_agent="Solar Tracker")
location = geolocator.geocode("201 Walt Banks Rd, Peachtree City, GA 30269")
global lat
lat = location.latitude
global lon
lon = location.longitude

    #getting date
exact_date = datetime.now()

    #getting elvation
global elv
elv = altitudo(lat=lat, lon=lon)

    #getting azimuth
tz = -4
global rounded_alt
global rounded_azm
alt, azm = sunpos(exact_date, lat, lon, tz, dst=False)
rounded_alt = round(alt,5)
rounded_azm = round(azm,5)
print("azimuth calcuated")

 
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
    for col in row:
        difference = rounded_azm - float(col)
        rounded_diff = round(difference, 2)
        step_count= rounded_diff / 5.625
        print(step_count)

        
        
        
  
