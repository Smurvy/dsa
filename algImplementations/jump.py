def search(arr, step,target_val):

    if(len(arr) <= step):
        return 0

    if(search(arr[step:],step,target_val) == True):
        for x in range(len(arr[:step + 1])):
            if(arr[x] == target_val):
                return x

        
    
    # this is horrendous
    # single type returns functions who????
    if(arr[step] > target_val):
        return True
    
    return step + search(arr[step:],step,target_val)


def jump(arr,step,target_val):
    if(len(arr) <= step):
        for x in range((len(arr))):
            if (arr[x] == target_val):
                return x
        return -1

    if(arr[step] > target_val):
        for x in range(len(arr)):
            if(arr[x] == target_val):
                return x
            
    return step + jump(arr[step:],step,target_val)


#only works if the indnex of the element is smaller than step??
print(jump([1,2,3,4,5,6,7,8],8,9))