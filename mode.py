from collections import Counter
import csv

with open('/Users/ruth/Desktop/coding/python/c-104/heightweight.csv',newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    nNumber = fileData[i][1]
    newData.append(float(nNumber))

data = Counter(newData)
modData =   {
                '50-60':0,
                '60-70':0,
                '70-80':0
            }
for height,occurence in data.items():
    if 50<float(height)<60:
        modData['50-60']+=occurence
    elif 60<float(height)<70:
        modData['60-70']+=occurence
    elif 70<float(height)<80:
        modData['70-80']+=occurence
modRange,modOccurence = 0,0
for range,occurence in modData.items():
    if occurence>modOccurence:
        modRange,modOccurence = [int(range.split('-')[0]),int(range.split('-')[1])],occurence
mode = float((modRange[0]+modRange[1])/2)
print(mode)