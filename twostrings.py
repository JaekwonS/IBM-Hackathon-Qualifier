#Given two strings, determine if they share a common substring. A substring may be as small as one character.
#
#For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    
    s1list = list(s1)
    s2list = list(s2)
    
    answer = list()
    
    for x in range(0, len(s1)):
        for y in range(0, len(s2)):
            if s1list[x] == s2list[y]:
                answer.append(s1list[x])
        
    print(answer)
            
    if not answer: 
        return "NO"
    else:
        return "YES"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
