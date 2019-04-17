import random
# Print 1-255
def PrintOneTwoFiftyFive():
    for x in range(0,256):
        print(x)

# Write a program that would print all the odd numbers from 1 to 1000
def PrintOdds():
    for x in range(1,1001):
        if x % 2 == 1:
            print(x)

# Write a program that would print the sum of all the odd numbers from 1 to 5000
def SumOdds():
    sum = 0
    for x in range(1,5001):
        if x % 2 == 0:
            sum += x
    print(sum)

#
""" 
    Iterating Through the Array
Given an array X say [1,3,5,7,9,13], write a program that would iterate through each member of the array 
and print each value on the screen.  

"""
def IterateThruArr(X):
    for x in X:
        print(x)

# Find Max
def FindMax(Arr):
    my_max = Arr[0]
    for x in range(1,len(Arr)):
        if my_max < Arr[x]:
            my_max = Arr[x]
    print(my_max)

# Find Average
def FindAvg(Arr):
    length = len(Arr)
    my_sum = 0
    for x in Arr:
        my_sum += x
    return my_sum / length

"""
    Array With Odd Numbers
Write a program that creates an array 'Y' that contains all the odd numbers between 1 to 255. 
When the program is done, 'y' should have the value of [1, 3, 5, 7, ... 255].

"""

def ArrWithOddNums():
    my_arr = []
    for x in range(1,256):
        if x % 2 == 1:
            my_arr.append(x)
    return my_arr

"""
    Greater Than Y
Write a program that takes an array and returns the number of values in that array whose value is greater than y. 
For example, if array = [1,3, 5, 7] and y = 3,
 after your program is run it will print 2 (since there are two values in the array whose value is greater than 3). 

"""
def GreaterThanY(Arr, Y):
    counter = 0
    for x in Arr:
        if x > Y:
            counter += 1
    return counter


# Square the Values
def SquareTheValues(Arr):
    for x in range(len(Arr)):
        Arr[x] *= Arr[x]

    return Arr


"""
Eliminate Negative Numbers
    Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that 
    replaces any negative number with the value of 0.  
    When the program is done x should have no negative values (e.g. [1, 5, 10, 0]).
"""
def EliminateNegativeNumbers(Arr):
    for x in range(len(Arr)):
        if Arr[x] < 0:
            Arr[x] = 0
    return Arr


"""

Max, Min, and Average
Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that prints the maximum number in the array,
 minimum value in the array as well as the average values in the array. 

"""
def MaxMinAvg(Arr):
    my_max = Arr[0]
    my_min = Arr[0]
    my_sum = Arr[0]
    for x in range(1,len(Arr)):
        if my_max < Arr[x]:
            my_max = Arr[x]
        if my_min > Arr[x]:
            my_max = Arr[x]
        my_sum += Arr[x]
    print(my_max, my_min, my_sum / len(Arr))

"""

    Shifting the values in the array
Given an array x (e.g. [1,5, 10, 7, -2]), create an algorithm (sets of instructions) that shifts 
each number by one (to the front).  
For example when the program is done x (assuming it was [1,5,10,7,-2]) should become [5,10,7,-2, 0].  

"""
def ShiftingTheValues(arr):
    for x in range(1, len(arr)):
        arr[x - 1] = arr[x]
    arr[len(arr) - 1] = 0
    print(arr)

"""

    Number to String
Write a program that takes an array of numbers and replaces any number that's negative to a string called 'Dojo'. 
For example if array = [-1, -3, 2] after your program is done array should be ['Dojo', 'Dojo', 2].

"""
def NumberToString(arr):
    for x in range(len(arr)):
        if arr[x] < 0:
            arr[x] = 'Dojo'

    print(arr)

"""

Assignment: Random Array
Create an array X and fill the array with 10 values, each value being a random integer between 0 to 100.  
For example when your program is done, X could be something like this: [35, 15, 3, 39, 53, 93, 25, 39, 59, 21].

"""
def RandomArray():
    
    randomArr = []
    for x in range(10):
        randomArr.append(random.randint(0,101))
    return randomArr

