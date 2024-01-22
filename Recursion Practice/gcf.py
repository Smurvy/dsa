# assumes num1 > num2

def gcf(num1,num2):

    if num2 % num1 == 0:
        return num2
    
    return gcf(num1 - 1,num2)

print(gcf(81,27))