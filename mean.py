import csv
from os import read

with open("pro104infodata.csv") as f:
    reader = csv.reader(f)
    fileData = list(reader)
    
fileData.pop(0)
fileData.pop(1)
newData = []
for i in range(len(fileData)) :
    number = fileData[i][2]
    newData.append(float(number))

n = len(newData)
total = 0
for x in newData:
    total += x

mean = total/n
print(mean)




