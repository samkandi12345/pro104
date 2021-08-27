import csv

with open("pro104infodata.csv") as m:
    reader = csv.reader(m)
    filedata = list(reader)

filedata.pop(0)
newData = []
for i in range(len(filedata)) :
    number = filedata[i][2]
    newData.append(float(number))

n = len(newData)
newData.sort()
if n % 2 == 0:
    median1 = float(newData[n//2])
    meadian2 = float(newData[n//2-1])
    meadian = (median1+meadian2)/2
    
else:
    meadian = newData[n//2]

print(meadian)
