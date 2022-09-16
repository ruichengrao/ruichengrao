
import xlsxwriter as xl
from datetime import datetime
import schedule, time
wb = xl.Workbook('solarPanel.xlsx')
ws = wb.add_worksheet('A Test Sheet')
print("workbook added")


from pyephem_sunpath.sunpath import sunpos
from altitudo import altitudo
from geopy.geocoders import Nominatim




#ws.write(Row, Column, )
ws.write(0, 0, "Date")
ws.write(0, 1, "Latitude")
ws.write(0, 2, "Longitude")
ws.write(0, 3, "Elevation")
ws.write(0, 4, "Altitude")
ws.write(0, 5, "Azimuth")

print("row 1 added")

i = 0

def addRow():
    global i
    geolocator = Nominatim(user_agent="Solar Tracker")
    location = geolocator.geocode("201 Walt Banks Rd, Peachtree City, GA 30269")
    lat = location.latitude
    lon = location.longitude
    elv = altitudo(lat=lat, lon=lon)
    date = datetime.now()
    tz = -4
    alt, azm = sunpos(date, lat, lon, tz, dst=True)
    print("sunpos gotten")

    ws.write(i, 0, datetime.now())
    ws.write(i, 1, lat)
    ws.write(i, 2, lon)
    ws.write(i, 3, elv)
    ws.write(i, 4, alt)
    ws.write(i, 5, azm)
    i += 1
    wb.close()
    print("wb closed")

schedule.every(1).seconds.do(addRow)
print('run once')

while True:
    schedule.run_pending()
    time.sleep(1)

