import csv 
from collections import Counter

with open("pro104infodata.csv") as f:
   reader =  csv.reader(f)
   filedata = list(reader)

filedata.pop(0)
filedata.pop(1)
newData = []
for i in range(len(filedata)):
    number = filedata[i][2]
    newData.append(number)

data = Counter(newData)
modeData = {
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140-150":0
}

for weight,occurence in data.items():
    if 110 < float(weight) < 120:
        modeData["110-120"] += occurence 

    elif 120 < float(weight) < 130:
        modeData["120-130"] += occurence

    elif 130 < float(weight) < 140:
        modeData["130-140"] += occurence

    elif 140 < float(weight) <150:
        modeData["140-150"] += occurence

modeRange,modeOccurence = 0,0 
for range,occurence in modeData.items():
    if occurence > modeOccurence :
        modeRange,modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0]+modeRange[1])/2)

print(mode)