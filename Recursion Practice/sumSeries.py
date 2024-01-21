# sum series of even numbers from 0 to n

def sumSeries(num):
    if(num <= 1):
        return 0

    return num + sumSeries(num - 2)

print(sumSeries(6))