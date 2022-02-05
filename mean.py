import csv
with open('/Users/ruth/Desktop/coding/python/c-104/heightweight.csv',newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    nNumber = fileData[i][1]
    newData.append(float(nNumber))

n = len(newData)
total = 0
for x in newData:
    total = total+x

mean = total/n
print('The mean is:'+str(mean))