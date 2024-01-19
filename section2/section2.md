### What is Big O notation
- language to desribe efficency of algorithms
- think about it:
    -is it faster to fly a huge file to your friend or transfer it electronically
##### Time complexity
- how thhe time grows over a given period
- how to determine what code is better
##### Space complexity
- how much space code takes to run
- less memory = better algorithm

#### Different notations
- omege is best case
- theta is average case
- big O is worst case
    - anything pretaining to big is measuring worst case

|   complexity  |   name    |   sample  |
-----------------------------------------
|   O(1)        |   constant|   a simple add numbers function   |
| O(N)          | linear    | loop through numbers from 1 to n  |
| O(LogN)       |logarithmic| find an element in a sorted array |
| O(N^2)        | quadratic |   nested loops                    |
| O(2^N)        | exponential| double recursion in fibonacci    |

##### O(1)
- most efficient complexity
- a flat line at 0 on the y axis (number of operations)
- multiplying two numbers, drawing a card at random from a deck

##### O(N)
- complexity grows with size of input data (i.e a loop that prints all values from an array)
- pass number **n** in, and the function runs **n** times

###### dropping constants (remove constants)
- eliminate values easily when analyzing
**for example**
```python
def printNumbers(number):
    for i in range(number):
        print(i)
    for J in range(number):
        print(j)
```
each of these loops is **O(n)** complexity, so adding together, the function has a complexity of **O(2n)**
- the first rule fo simplifying algorithsm is dropping these constants