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
import copy

def insertionSort1(n, arr):
    # Write your code here

    unsorted_value = arr[-1]
    for i in reversed(range(len(arr) - 1)):
        if arr[i] < unsorted_value:
            arr[i + 1] = unsorted_value
            print(*arr)
            break
            
        else:
            arr[i], arr[i + 1] = arr[i], arr[i]
            print(*arr)
    
    if unsorted_value < arr[0]:
        arr[0] = unsorted_value
        print(*arr)
        
    # for i in range(n):
    #     count = 0 
    #     for j in range(n):
    #         if arr[j] < arr[i]:
    #             count += 1
    #     arr[count], arr[i] = arr[i], arr[count]

    #     print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
