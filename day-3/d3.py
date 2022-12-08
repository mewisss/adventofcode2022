# Task 1
file = open('data.txt', 'r')
read = file.readlines()


def splitAndCompare(str):
    # Split into 2 strings
    retVal = ""
    fp, sp = str[:len(str)//2], str[len(str)//2:]

    # Compare Each Value
    for i in range(len(fp)):
        for j in range(len(sp)):
            if fp[i] == sp[j]:
                retVal=fp[i]

    return(retVal)


def assignValue(letter):
    if letter.isupper() == True:
        reval = ord(letter)-ord("A")+27
    elif letter.isupper() ==False:
        reval = ord(letter)-ord("a")+1

    return(reval)


# def game(anArray):
#     finalScore = 0
#     for i in range(len(anArray)):
#         finalScore += assignValue(splitAndCompare(anArray[i]))
#     return finalScore

# print(game(read))

# Task 2
def compare3strings(arr):
    for i in range(len(arr[0])-2): # cheeky \n in the strings
        if arr[0][i] in arr[1] and arr[0][i] in arr[2]:
            retVal = arr[0][i]
    print(retVal)
    return(retVal)

def gamet2(anArray):
    finalScore =0
    for i in range(0, len(read), 3):
        finalScore += assignValue(compare3strings(anArray[i:i+3]))
        #print("i = " + str(i) + "\n i+3 = " + str(i+3))
    return finalScore

print(gamet2(read))

#print(assignValue(compare3strings(read[0:3])))

#print(read[0:3])
#print(read[3:6])

