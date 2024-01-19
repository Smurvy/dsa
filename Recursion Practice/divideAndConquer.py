# how to find index??

def divideAndConquer(myList, targetNum):
    middlePos = int(len(myList)/2)
    if(myList[len(myList) - 1] == targetNum):
        return len(myList)

    if(myList[middlePos] > targetNum):
        return divideAndConquer(myList[:middlePos],targetNum)
    else:
        return divideAndConquer(myList[middlePos:],targetNum)

print(divideAndConquer([1,2,3,4,5],5))

