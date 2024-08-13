#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_positivo = 0
    count_negativo = 0
    count = 0
    lenght = len(arr)

    for i in arr:
        if i > 0:
            count_positivo += 1
        elif i < 0 :
            count_negativo += 1
        elif i == 0 :
            count += 1
    print(count_positivo/lenght)
    print(count_negativo/lenght)
    print(count/lenght)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
