
# Encryption

def printList(x):
    myList = ""
    for i in x:
        myList = myList+" "+str(i)
    return myList


def numtoArr(x):
    arr = []
    for char in x:
        arr.append(int(char))
    return arr


def calculateKnapsack(M, S):
    sum = 0
    for i in range(0, len(M)):
        sum = sum + M[i]*S[i]

    return sum


M = [62, 93, 81, 88, 102, 37]  # knapsack
S = numtoArr("011000")  # plaintext

sum = calculateKnapsack(M, S)

print("sum is" + str(sum))
