def factorial(myNum):
    if(myNum == 1):
        return 1
    return myNum * factorial(myNum - 1)
    

print(factorial(5))