# CSCI 220L - Lab 12 - Algorithms 

## Name: Carter Haley
##Name: Sarah Allen

import random
from graphics import *

""" Number 3. Comparative Analysis of Searches
List of 49 Elements:

Find 57 - beginning of list -The algorithms are equally as effective
Linear ->  1e-05 seconds.
Binary -> 1e-05 seconds.

Find 158 - middle of list
Binary(  -> 0.0 seconds) is more effective

Find 282 - end of list -The algorithms are equally as effective
Linear -> 1e-05 seconds.
Binary -> 1e-05 seconds.

Find 1 - not in list -The algorithms are equally as effective
Linear -> 1e-05 seconds.
Binary -> 1e-05 seconds.

##########################################
List with 10000950 elements.

Find 57 - beginning of list
Linear -> 1e-05 seconds. This algorithm is more effective for this search.

Find 500000 - middle of list
Binary -> 2e-05 seconds. This algorithm is more effective for this search.

Find 10001000 - end of list
Binary -> 2e-05 seconds. This algorithm is more effective for this search.

Find 1 - not in list
Binary -> 2e-05 seconds. This algorithm is more effective for this search.

5. Comparative Analysis of Sorts
Code to look at runtime for selection sort vs. Python's list sort.

Sorting list with 10000 elements.

Selection sort -> 0.0022 seconds.

The selection sort was more effective in that it took .00074 seconds less.

Python's sort -> 0.00294 seconds.
"""
def reverseSort(values):
    values.sort()
    values.reverse()
    
#def findAndRemoveFirst
def findAndRemoveFirst(list, value):
    name = input("Enter your name: ")
    spot = list.index(value)
    list.remove(value)
    #list.pop(spot)
    list.insert(spot, name)

def readData(filename):
    infile = open(str(filename),"r")
    nums = []

    for line in infile:
        lineSplit = line.split()
        for i in range(len(lineSplit)):
            nums.append(eval(lineSplit[i]))
##    print(nums)
    return nums

def isInLinear(searchVal, values):
    searchVal2=False
    while searchVal2== False:
        for i in range(len(values)):
            if values[i] == searchVal:
                return True

        return False


def isInBinary(searchVal, values):
    searchVal2=False
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        item = values[mid]
        if searchVal == item:
##            return mid
            return True
        elif searchVal < item:
            high = mid - 1
        else:
            low = mid + 1
## return -1
    return False
    
##    if values[i] == searchVal:
##                return True
##
##        return False

##def com

def selectionSort(values):
    n = len(values)
    for front in range(n-1):
        mp = front
        for i in range(front + 1, n):
            if values[i] < values[mp]:
                mp = i
            temp = values[mp]
            values[mp] = values[front]
            values[front] = temp
        return values

def calcArea(rectangles):
    p1 = rectangles.getP1()
    p2 = rectangles.getP2()
    p1X = p1.getX()
    p1Y = p1.getY()
    p2X = p2.getX()
    p2Y = p2.getY()
    height = abs(p1X - p2X)
    length = abs(p1Y - p2Y)
    area = height * length
    return area


def rectSort(rectangles):
    n = len(rectangles)
    for front in range(n-1):
        mp = front
        for i in range(front + 1, n):
            if rectangles[i] <  rectangles[mp]:
                mp = i
        temp = values[front]
        values[front] = values[mp]
        values[mp] = temp

def randomRects():
    randRects = []
    for i in range(10):
        rectangle = Rectangle(Point(random(),random()),Point(random(),random()) )
        randRects.append(rectangle)
    return randRects
    
    
def main():
    values= [25, 2, 5, 6, 9, 11]
    print("Before:\n",values)
    reverseSort(values)
    print("\nAfter:\n",values)

    findValue = 6
    nameList = [10, 6, 5, 4, 20 , 6, 10]
    findAndRemoveFirst(nameList, findValue)
    print(nameList)

    filename = "dataSorted.txt"
    nums = readData(filename)
    print(nums)

    find = 245
    linear = isInLinear(find, nums)
    print(linear)

    binary = isInBinary(find, nums)
    print(binary)

    sortNum = selectionSort(nums)
    print(sortNum)

    rectangles = randomRects()
    rects = calcArea(rectangles)
    print(rects)
    

    

 
    
##main()


