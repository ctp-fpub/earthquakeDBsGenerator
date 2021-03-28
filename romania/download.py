import wget 
import pandas as pd

# downloads the ROMPLUS catalogue
url = 'http://www.infp.ro/data/romplus.txt'  
wget.download(url, 'romplus.txt') 

outputFile = "romplus.csv"

with open(outputFile, 'a', newline='') as fle:
    fle.write("Date and time,Latitude,Longitude,Depth,Magnitude \n")


# parsing data
file = pd.read_fwf('romplus.txt', 
skiprows=0, 
colspecs = [(0, 4), 
(5, 7), 
(8, 10),
(12,14),
(15,17),
(18,23),
(37, 45), 
(47, 56), 
(75, 80), 
(107, 110)], 
header=0,
names=['Year',
'Month',
'Day',
'Hour',
'Minute',
'Second',
'Latitude',
'Longitude',
'Depth',
'Magnitude'])


for i in range(0,len(file.index)):
    dt = str(file['Year'][i]) + "-" + str(file['Month'][i]) + "-" + str(file['Day'][i]) + " " +  str(file['Hour'][i]) + ":" + str(file['Minute'][i]) + ":" + str(file['Second'][i])
    with open(outputFile, 'a', newline='') as fle:
        fle.write(dt+ ',')
        fle.write(str(file['Latitude'][i]) + ',')
        fle.write(str(file['Longitude'][i]) + ',')
        fle.write(str(file['Depth'][i]) + ',')
        fle.write(str(file['Magnitude'][i]) + '\n')



