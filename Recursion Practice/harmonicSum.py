def harmonicSum(n):
    if(n == 1):
        return 1
    return (1/n) + harmonicSum(n - 1)

print(harmonicSum(30))