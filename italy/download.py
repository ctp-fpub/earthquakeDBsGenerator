import wget
import os
import tarfile
import pandas as pd

for year in range (1986, 2021):

    first = 'http://webservices.ingv.it/fdsnws/event/1/query?starttime='
    yr1=str(year)
    second = '-01-01T00%3A00%3A00&endtime='
    yr2 = str(year+1)
    third = '-01-01T23%3A59%3A59&minmag=-1&maxmag=10&mindepth=-10&maxdepth=1000&minlat=27&maxlat=48&minlon=-7&maxlon=37.5&minversion=100&orderby=time-asc&timezone=UTC&format=text&limit=10000'
    url = first + yr1 + second + yr2 + third
    filename = yr1 + '.txt'
    wget.download(url, filename)