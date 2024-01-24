def max(arr):
    if len(arr) == 1:
        return arr[0]
    
    return arr[0] if arr[0] > max(arr[1:]) else max(arr[1:])
    

print(max([1,4,6,2,3,7,8,1024]))