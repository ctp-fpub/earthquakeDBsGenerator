import pandas as pd
import sys

def isFloat(value):
  try:
    float(value)
    return float(value)
  except ValueError:
    return -1

file = pd.read_fwf(str(sys.argv[1]),
colspecs = [(0, 1), # identifier
(1, 5), # year
(5,7), # day
(7,9), # month
(9,11), # hour
(11,13), # minute
(13,17), # second
(21, 24), # lat deg
(24, 28), # lat min
(32, 36), # lon deg
(36, 40), # lon min
(44, 49), # depth
(52, 54), # magnitude
],
header = 0,
names = ['Identifier', 'Year', 'Month', 'Day', 'Hour', 'Minute', 'Second', 'Latitude deg', 'Latitude min', 'Longitude deg', 'Longitude min', 'Depth', 'Magnitude'])

outputFile = "output/japan-jma-" + str(sys.argv[1]) + ".csv"

if (int(sys.argv[2])==1):
  with open(outputFile, 'a', newline='') as fle:
      fle.write("Year,Month,Day,Hour,Minute,Second,Latitude,Longitude,Depth,Magnitude \n")

print("Processing " + str(sys.argv[1]))

for i in range(0,len(file.index)):

  if (i%1000 == 0):
    print(str(i)+"/"+str(len(file.index)))
  
  if(str(file['Identifier'].loc[[i]].values) == "['J']"):  
    with open(outputFile, 'a', newline='') as fle:
      fle.write( str(int(file['Year'].loc[[i]].values)) + ',')
      fle.write( str(int(file['Month'].loc[[i]].values))+ ',')
      fle.write( str(int(file['Day'].loc[[i]].values))+ ',')
      fle.write( str(int(file['Hour'].loc[[i]].values))+ ',')
      fle.write( str(int(file['Minute'].loc[[i]].values))+ ',')
      fle.write( str(float(file['Second'].loc[[i]].values)/100) + ',')
      fle.write( str(int(file['Latitude deg'].loc[[i]].values) + (float(file['Latitude min'].loc[[i]].values)/100)/60 )+ ',')
      fle.write( str(int(file['Longitude deg'].loc[[i]].values) + (float(file['Longitude min'].loc[[i]].values)/100)/60 )+ ',')
      fle.write( str(isFloat(file['Depth'].loc[[i]].values)/100)+ ',')
      fle.write( str(isFloat(file['Magnitude'].loc[[i]].values) / 10)+ '\n')
        

