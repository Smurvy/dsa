import math

def search(arr,targetVal):
    point1 = math.floor(len(arr) * 0.333)
    point2 = math.floor(len(arr) * 0.666)

    

    if(targetVal == arr[point1]):
        return point1
    elif(targetVal == arr[point2]):
        return point2
    #elif(len(arr) == 3):
        #return "element not found"
    if (targetVal < arr[point1]):
        return search(arr[:point1],targetVal)
    elif(targetVal < arr[point2]):
        return point1 + search(arr[point1:point2],targetVal)
    else:
        return point2 + search(arr[point2:],targetVal)


myList = [6,789,4560]
print(search(myList,4560))