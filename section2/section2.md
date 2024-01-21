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

|   complexity  |   name    |   sample                          |
-----------------------------------------------------------------
|   O(1)        |   constant|   a simple add numbers function   |
| O(N)          | linear    | loop through numbers from 1 to n  |
| O(LogN)       |logarithmic| find an element in a sorted array |
| O(N^2)        | quadratic |   nested loops                    |
| O(2^N)        | exponential| double recursion in fibonacci    |

##### O(1)
- most efficient complexity
- a flat line at 1 on the y axis (number of operations)
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
- we optimize for least number of operations, not for hardware (not everyting is running on a supercomputer!)
- asymptomatic analysis ignores things like hardware to ensure objective truth when observing algorithms

##### O(n^2)
```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
```
- double loops create O(n^2) time complexities
    - adding loops within loops increases this (i.e adding a loop within the "j loop" above will increase the time complexity from **O(n^2)** to **O(n^3)**)
- this is very inefficient code

###### dropping Non Dominant Terms
given code:
```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
```
we know that the first nest loop has a **O(n^2)** and the second loop has **O(n)**. The technical copmlexity of the algorithm can be expressed in **O(n^2 + n)**.
however, the n can be dropped because of how little difference it makes compared to the **O(n^2)**

##### O(logn)
- divide and conquer approach
- the base of the log is dependent on how many times you divide the array
    - divide array into two parts ->  log~2~n, 3 parts -> log~3~n, etc.
- can use attributes besides numerical value when finding what apart of the list the card is in
- relatively flat compared to O(n) and  O(n^2)

##### Space Complexity
- each time a function is called, it is added to the stack
- space complexity is dependent on the number of calls on the stack
- if your recursive function makes **n** calls based on **n** input, then it is said to have O(n) space copmlexity
    -> you can now see how this applies with all of the other complexities so far
###### exception
```python
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i,i+1)
    return total
def pair_sum(a,b):
    return a + b
```
- because the `pair_sum()` function does not exists simaltaneously on the stack (it is being calculated in the moment, w/o recursion, gets removed after it is calculated), the `pair_sum_sequence` function is said to have **O(n)** space complexity

##### Diffreent Terms for Input - add vs multiply
```python
def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
```
- this is **not O(n)** time complexity because that would assum a == b
- instead, you add them together so the actualy time complexity is **O(a+b)**
###### Rules
- if algorithm is in the form "do this, **then** do this other thing
    - **O(a+b)**
- if algorithm is in the form "do this for each time you do that", then you have an **O(a*n)** time complexity algorithm

#### How measure time compleixty of code using Big O
1. Any assingment statements and if statements that are executed once regfardless of the size of problem
    - O(1)
2.  A simple "for" loop from 0 to n (with no internal loops)
    - O(n)
3. A nested loop of the same type (each loops runs same amount of times) takes quadratic time complexity
    - O(n^2)
4. A loop in which the controlling parameter is divide by two at each step
    - O(log n)
5. When dealing with multiple statements just add them up
    - O(a*b)