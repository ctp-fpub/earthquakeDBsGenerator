import wget
import os
import pandas as pd
import csv

os.system('rm -rf *.txt')
os.system('rm -rf italy.csv')

startDate = ["-01-01", "-02-01", "-03-02", "-04-01", "-05-01", "-06-01", "-07-01", "-08-01", "-09-01", "-10-01", "-11-01", "-12-01"]
endDate = ["-01-31", "-03-01", "-03-31", "-04-30", "-05-31", "-06-30", "-07-31", "-08-31", "-09-30", "-10-31", "-11-30", "-12-31"]

outputFile = "italy.csv"

with open(outputFile, 'a', newline='') as fle:
    fle.write("Year,Month,Day,Hour,Minute,Second,Latitude,Longitude,Depth,Magnitude,Magnitude type \n")

for year in range (1986, 2021):
    for month in range(0,12):

        url = "http://webservices.ingv.it/fdsnws/event/1/query?starttime=" + str(year)+startDate[month] + "T00%3A00%3A00&endtime=" + str(year) + endDate[month] + "T23%3A59%3A59&minmag=0&maxmag=10&mindepth=0&maxdepth=1000&minlat=27&maxlat=48&minlon=-7&maxlon=37.5&minversion=100&orderby=time-asc&timezone=UTC&format=text&limit=15000"
        filename = str(year) + "-" + str(month+1) + ".txt"
        wget.download(url, filename)

        dataFrame =  pd.read_csv(filename, sep='|' , engine='python')
        print("; Downloaded " + str(len(dataFrame.index)) + " events")

        for i in range(0,len(dataFrame.index)):
            timeString = str(dataFrame['Time'].loc[[i]].values)

            with open(outputFile, 'a', newline='') as fle:
                fle.write(str(int(timeString[2:6]))+ '-') # year
                fle.write(str(int(timeString[7:9]))+ '-') # month
                fle.write(str(int(timeString[10:12]))+ ' ') # day
                fle.write(str(int(timeString[13:15]))+ ':') # hour
                fle.write(str(int(timeString[16:18]))+ ':') # minute
                fle.write(str(float(timeString[19:25])) + ',') # second
                fle.write(str(float(dataFrame['Latitude'].loc[[i]].values)) + ',') # latitude
                fle.write(str(float(dataFrame['Longitude'].loc[[i]].values)) + ',') # longitude
                fle.write(str(float(dataFrame['Depth/Km'].loc[[i]].values)) + ',') # longitude
                fle.write(str(float(dataFrame['Magnitude'].loc[[i]].values)) + ',') # magnitude
                fle.write(dataFrame['MagType'][i] + '\n') # magnitude type