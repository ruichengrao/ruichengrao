import xlsxwriter as xl
from datetime import datetimehttps://github.com/ruichengrao/ruichengrao/blob/main/Solar%20Tracker.py
import schedule, time
wb = xl.Workbook('solarPanel.xlsx')
ws = wb.add_worksheet('A Test Sheet')
print("WorkBook Added")


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

print("Row 1 Added")
wb.close()

i = 0



schedule.every(1).seconds.do(addRow)
print('run once')

while True:
    schedule.run_pending()
    time.sleep(1)
