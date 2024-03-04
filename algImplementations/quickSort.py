# Online Python compiler (interpreter) to run Python online.




def sort(arr):
    if(len(arr) == 0):
        return []
    if(len(arr) == 1):
        return arr
    if(len(arr) == 2):
        if(arr[0] < arr[1]):
            return arr
        else:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            return arr
        
    pivot = len(arr) - 1
    small = []
    big = []
    
    
    for x in arr:
        if(x <= arr[pivot]):
            small.append(x)
        else:
            big.append(x)
            
            
    print(small)
    print(big)
    return sort(small) + sort(big)
    
    
print(sort([6,456,8,2,3]))
    