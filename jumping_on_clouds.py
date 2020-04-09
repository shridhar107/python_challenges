'''
Problem Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # print(c)
    count = 1
    modified_c = []
    modified_c.append(c[0])
    prev_i = c[0]
    for i in range(1, len(c)):
        if c[i] == prev_i:
            count += 1
        else:
            modified_c.append(count)
            modified_c.append(c[i])
            count = 1
        prev_i = c[i]
    modified_c.append(count)
    
    # print(modified_c)
    result = 0
    len_mod_c = len(modified_c)
    for i in range(1, len_mod_c+1, 2):
        if modified_c[i-1] == 0:
            result += int(modified_c[i]/2) + 1
            # print(result)

    return result-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
