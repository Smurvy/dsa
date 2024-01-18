# sum multidimensional array???

def sumRecursively(list):
    if(type(list) == int):
        return list
    
    if(len(list) == 1):
        return sumRecursively(list[0])
    else:
        return list[0] + sumRecursively[1:]
    