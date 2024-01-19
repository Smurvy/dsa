# sums and dimension of array

def recursiveSum(myList):
    if(type(myList[0]) == list and len(myList) > 1):
        return recursiveSum(myList[0]) + recursiveSum(myList[1:])
    elif(type(myList[0]) == int and len(myList) > 1):
        return myList[0] + recursiveSum(myList[1:])
        
    elif(type(myList[0]) == list and len(myList) == 1):
        return recursiveSum(myList[0])
    else:
        return myList[0]

print(recursiveSum([1,2,3,[2,3,4],[1,2,3],[1,2,3]]))
