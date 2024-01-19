
def divideAndConquer(myList, targetNum):
    middlePos = int(len(myList)/2)
    if(myList[len(myList) - 1] == targetNum):
        return 0

    if(myList[middlePos] > targetNum):
        return divideAndConquer(myList[:middlePos],targetNum)
    else:
        return middlePos + divideAndConquer(myList[middlePos:],targetNum)

print(divideAndConquer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],2))

