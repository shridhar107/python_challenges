'''

Lik: https://www.hackerrank.com/challenges/counting-valleys/problem?

Input Format

The first line contains an integer , the number of steps in Gary's hike.
The second line contains a single string , of  characters that describe his path.

Output Format

Print a single integer that denotes the number of valleys Gary walked through during his hike.

Sample Input

8
UDDDUDUU
Sample Output

1
Explanation

If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:

_/\      _
   \    /
    \/\/
He enters and leaves one valley.

'''
#!/bin/python3

import math
import os
import random
import re
import sys

def find_how_many_neg_in_array(ar):
    count = 0
    u_set = 0
    for i in ar:
        if i*(-1) > 0:
            if u_set == 0:
                count += 1
                u_set = 1
        else:
            u_set = 0
    return count

# Complete the countingValleys function below.
def countingValleys(n, s):
    ar_s = list(s)
    modified_ar = []
    modified_ar.append(0)
    for i in range(0, len(ar_s)):
        if ar_s[i] == 'U': 
            ar_s[i] = 1
        elif ar_s[i] == 'D':
            ar_s[i] = -1
        else:
            print("wrong char in input array!")
        modified_ar.append(modified_ar[i] + ar_s[i])

    return find_how_many_neg_in_array(modified_ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
