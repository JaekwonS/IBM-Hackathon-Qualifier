#Given an array  of  integers and a number, , perform  left rotations on the array. 
#Return the updated array to be printed as a single line of space-separated integers.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    
    if not a: 
        return "You passed a empty array"
    elif len(a) == d:
        return a
    else:
        a = a[d:] + a[:d]
        return a
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
