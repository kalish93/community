#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    num = arr[n-1]
    for i in range(n-1,0,-1):
        if arr[i-1] > num:
            arr[i] = arr [i-1]
            for i in arr:
                print(i,end=' ')
            print()
        elif arr[i-1] < num:
            arr[i] = num
            for i in arr:
                print(i,end=' ')
            break
    if arr[1] > num:
        arr [0] = num
        for i in arr:
            print(i,end=' ') 
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)