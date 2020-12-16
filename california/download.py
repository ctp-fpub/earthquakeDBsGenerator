import wget
import os
import tarfile
import pandas as pd

url = 'https://service.scedc.caltech.edu/ftp/catalogs/SCEC_DC/SCEDC_catalogs.tar.gz'
filename = 'california.tar.gz'
wget.download(url, filename)

tar = tarfile.open("california.tar.gz")
tar.extractall()
tar.close()

for year in range (1932, 2021):
    removeFirstCMD = 'tail -n +11 SCEC_DC/' + str(year) + ".catalog >> " + str(year) + '.temp'
    os.system(removeFirstCMD)
    removeLastCMD = 'head -n -2 ' + str(year) + ".temp >> " + str(year) + '.cat'
    os.system(removeLastCMD)

os.system('cat *.cat >> finalCat.txt')
os.system('rm -rf *.temp *.tar.gz *.cat')
os.system('rm -rf SCEC_DC')

file = pd.read_fwf('finalCat.txt',
colspecs = [(0, 4), 
(5, 7), 
(8, 10),
(11,13),
(14,16),
(17,22),
(39, 45), 
(46, 54), 
(56, 60), 
(29, 33)], 
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

file.to_csv(r'california.csv', index = False, header=True)
