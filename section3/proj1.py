def getTemps(numDays,myArr):
    if(numDays == 0):
        return 0
    myArr.append(int(input(f"Day {len(myArr) + 1} temperature: ")))
    getTemps(numDays - 1,myArr)
    return myArr

def sum(arr):
    if len(arr) == 1:
        return arr[0]
        
    return arr[0] + sum(arr[1:])

def average(arr):
    return sum(arr) / len(arr)
    
def aboveAverage(arr,avg):
    if len(arr) == 1:
        return 1 if arr[0] > avg else 0
    if arr[0] > avg:
        return 1 + aboveAverage(arr[1:],avg)
    else:
        return 0 + aboveAverage(arr[1:],avg)
def main():
    arr = []
    print(getTemps(int(input("How many days temperatures are avaliable?")),arr))
    print(average(arr))
    print(aboveAverage(arr,average(arr)))
    
main()

