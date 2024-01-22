# Section 3

##### What is an Array?
- use NumPy array module to create arrays in Python
- arrays can store elements of the same data type
- elements are contiguous
    - elements are stored next to eachother with no space in between
- data structure
- collection of variables of same type
##### Types of Arrays
- 1 dimensional
- multi-dimensional

##### Arrays in memory
###### 1 Dimensional
- the system chooose a random space in RAM, though **the space chosen is contiguous**
###### 2 Dimensional
- in memory, the array is represented as a 1 dimensional array with
- this is true for any dimension of array
- How does the copmuter recognize, rows,columns,depth,etc?
##### Create an  array in python

###### With array module
```python
import array

myArray = array.array('i') # empty array with type integer
myArray = array.array('i',[1,2,3,4]) # add some numbers!
```
- only accepts primtive data types

###### With NumPy
```python
import numpy as np

npArray = np.array([],dtype = int) # empty array with type integer
npArray = np.array([1,2,3,4]) # add some numbers!

```
- wider array of features than the array module

##### Inserting into an array
**At beginning**
- all elements indeices will be  shifted forward once
- very time consuming
- **O(n)**
**In the middle**
- anything to the right of the insertion point will have their indices push to the right
**At the end**
- insert elements at the end with new index
- much more efficient than the other insertions
- **O(1)**'

to revisit a code sample from earlier....
```python
import array

myArray = array.array('i') # empty array with type integer
myArray = array.array('i',[1,2,3,4]) # add some numbers!

myArray.inser(0,6) # inserting at index 0 with element 6
```
- having a number greater than the last index of the array will always put the number at the end of the array, no matter the index

##### Array Traversal
- traversal is when you look at each element of an array

##### Deleting from an array
- deletion of last eleemnt is very efficient because there is  no reassigning of indices, however deleting form the middle of the array will cause all elements indices to shift down one.

##### When should I use arrays?
- when you want to store multiple variables of the same type
- when you want to access a random point in the array

###### Avoid
- reservememory block in array
    - if you add elements beyond the  length fo the array, you have to expand the array whicih is memory consuming