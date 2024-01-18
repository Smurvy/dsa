import math as math

def integerToString(myInteger):
    if (myInteger < 10):
        return str(myInteger)
    else:
        return str((myInteger % 10)) + str(integerToString(math.floor(myInteger/10)))
        

print(integerToString(546))