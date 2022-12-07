# # Task 1 
file = open('data.txt', 'r')
read = file.readlines()

# roundScores = 0
# resultScores = 0

roundScorest2 = 0
resultScorest2 = 0

# # Rock      (A)(x) = 1
# # Paper     (B)(y) = 2
# # Scissors  (C)(z) = 3


# for i in range(len(read)):
#     print(roundScores)
#     print(resultScores)
#     if read[i][2] == "X":
#         roundScores +=1
#         if read[i][0] == "A":
#             resultScores +=3
#         elif read[i][0] == "C":
#             resultScores +=6
#     elif read[i][2] == "Y":
#         roundScores +=2
#         if read[i][0] == "A":
#             resultScores +=6
#         elif read[i][0] == "B":
#             resultScores +=3
#     elif read[i][2] == "Z":
#         roundScores +=3
#         if read[i][0] == "B":
#             resultScores +=6
#         elif read[i][0] == "C":
#             resultScores +=3

# print(resultScores + roundScores)


# Task 2

# X = Lose
# Y = Draw
# Z = Win

for i in range(len(read)):
    if read[i][0] == "A":
        if read[i][2] == "X":
            # Go Scissors
            resultScorest2 += 0
            roundScorest2 += 3
        elif read[i][2] == "Y":
            # Go Rock
            resultScorest2 += 3
            roundScorest2 += 1
        elif read[i][2] == "Z":
            # Go Paper
            resultScorest2 += 6
            roundScorest2 += 2
    elif read[i][0] == "B":
        if read[i][2] == "X":
            # Go Rock
            resultScorest2 += 0
            roundScorest2 += 1
        elif read[i][2] == "Y":
            # Go Paper
            resultScorest2 += 3
            roundScorest2 += 2
        elif read[i][2] == "Z":
            # Go Scissors
            resultScorest2 += 6
            roundScorest2 += 3
    elif read[i][0] == "C":
        if read[i][2] == "X":
            # Go Paper
            resultScorest2 += 0
            roundScorest2 += 2
        elif read[i][2] == "Y":
            # Go Scissors
            resultScorest2 += 3
            roundScorest2 += 3
        elif read[i][2] == "Z":
            # Go Rock
            resultScorest2 += 6
            roundScorest2 += 1

print(resultScorest2)
print(roundScorest2)

print(resultScorest2 + roundScorest2)