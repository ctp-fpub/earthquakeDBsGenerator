import wget 
import pandas as pd

# downloads the ROMPLUS catalogue
url = 'http://www.infp.ro/data/romplus.txt'  
wget.download(url, 'romplus.txt') 

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

file.to_csv(r'romania_romplus.csv', index = False, header=True)

