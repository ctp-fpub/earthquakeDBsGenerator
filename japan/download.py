import wget
import os
import pandas as pd

os.system('rm -rf *.txt')

for month in range(7, 13):
    if month < 10:
        mnth = '0' + str(month)
    else:
        mnth = str(month)
    
    url = 'http://wwweic.eri.u-tokyo.ac.jp/CATALOG/junec/1985/1985' + mnth + '.txt'
    filename = 'junec' + str(1985) + mnth + '.txt'
    wget.download(url, filename)

for year in range(1986, 1999):
    for month in range(1, 13):
        if month < 10:
            mnth = '0' + str(month)
        else:
            mnth = str(month)

        url = 'http://wwweic.eri.u-tokyo.ac.jp/CATALOG/junec/' + str(year) + '/' + str(year) + mnth +'.txt'
        filename = 'junec' + str(year) + mnth + '.txt'
        wget.download(url, filename)

os.system('cat junec*.txt >> output.txt')
os.system('rm -rf junec*')


file = pd.read_fwf('output.txt',
colspecs = [(0, 2), 
(3, 5), 
(6, 8),
(9,11),
(12,14),
(15,20),
(32, 38), 
(22, 29), 
(41, 46), 
(48, 51)], 
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

file.to_csv(r'japan_junec.csv', index = False, header=True)