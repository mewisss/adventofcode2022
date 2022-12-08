file = open('data.txt', 'r')
read = file.readlines()


def split(str):
    str = str.strip()
    for i in range(len(str)):
        if str[i] == ",":
            fp, sp = str[:i], str[i+1:]
    for i in range(len(fp)):
        if "-" in fp[i]:
            a,b = fp.split("-")
            a,b = int(a), int(b)
    for j in range(len(sp)):
        if "-" in sp[j]:
            c,d = sp.split("-")
            c,d = int(c), int(d)
    retVal = [a,b,c,d]
    return(retVal)

def validate(anArray):
    if anArray[0] <= anArray[2] and anArray[1] >= anArray[3] :
        return(1)
    if anArray[2] <= anArray[0] and anArray[3] >= anArray[1] :
        return (1)
    return(0)


def game(anArray):
    finalValue = 0
    for i in range(len(anArray)):
        finalValue+= validate(split(anArray[i]))
    return finalValue

#print(game(read))

# Task 2
def overlap(anArray):
    if anArray[0] >= anArray[2] and anArray[0] <= anArray[3] :
        return(1)
    if anArray[1] >= anArray[2] and anArray[1] <= anArray[3] :
        return (1)
    if anArray[2] >= anArray[0] and anArray[2] <= anArray[1] :
        return(1)
    if anArray[3] >= anArray[0] and anArray[3] <= anArray[1] :
        return(1)
    return(0)

def game2 (anArray):
    finalValue = 0
    for i in range(len(anArray)):
        finalValue+= overlap(split(anArray[i]))
    return finalValue

print(game2(read))