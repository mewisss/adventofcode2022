# Task 1 - Max
file = open('data.txt', 'r')
read = file.readlines()

tempVal =0
retVal = []


for i in range(len(read)):
    if len(read[i]) >1 :
        tempVal += int(read[i])
    elif read[i] == "\n":
        retVal.append(tempVal)
        tempVal = 0

retVal.append(tempVal)

#print(max(retVal))

#Task 2 - Sum of top 3 MAx

v1 = max(retVal)
retVal.remove(v1)
v2 = max(retVal)
retVal.remove(v2)
v3 = max(retVal)

print(v1)
print(v2)
print(v3)

print(v1+v2+v3)




