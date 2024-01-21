def sumDigits(num):
    if(num < 10):
        return num
    
    return num % 10 + sumDigits(int(num /10))

print(sumDigits(23456))