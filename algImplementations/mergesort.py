def sort(arr):
    if(len(arr) == 2):
        if(arr[0] < arr[1]):
            return arr
        else:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            return arr
    return 
        


        