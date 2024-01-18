def addList(list):
    if(len(list) == 1):
        return list[0]
    else:
        return list[0] + addList(list[1:])
    
myList = [1,2,3,4] # adds to 10

print(addList(myList))