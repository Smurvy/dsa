# solves fibonacci sequence

def fib(term, num1=1,num2=1):
    if term == 1:
        return num1
    
    num2 = num1 + num2 # 2
    num1 = num2 - num1  # 1 
    return fib(term - 1,num1,num2)
    
print(fib(479))