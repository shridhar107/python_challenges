'''
Sock Merchant
https://www.hackerrank.com/challenges/sock-merchant/problem?
Sample Input:
9
10 20 20 10 10 30 50 10 20
Sample output:
3
Explanation:
Combination of (10, 10) - 2
Combination of (20, 20) - 1
Each digit represents color of a sock, output is how many pairs possible ?
'''
#!/bin/python3

import math
import os
import random
import re
import sys


def search_modify(element, array):
    for i in range(0, len(array)):
        if element == array[i]:
            array.pop(i)
            return array
    array.append(element)
    return array

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    new_ar = []
    new_n = 0
    count = 0
    if len(ar) > 0: 
        new_ar.append(ar[0])
        new_n += 1
    for i in range(1, len(ar)):
        new_ar = search_modify(ar[i], new_ar)
        if new_n > len(new_ar):
            count += 1
        new_n = len(new_ar)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys


def search_modify(element, array):
    for i in range(0, len(array)):
        if element == array[i]:
            array.pop(i)
            return array
    array.append(element)
    return array

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    new_ar = []
    new_n = 0
    count = 0
    if len(ar) > 0: 
        new_ar.append(ar[0])
        new_n += 1
    for i in range(1, len(ar)):
        new_ar = search_modify(ar[i], new_ar)
        if new_n > len(new_ar):
            count += 1
        new_n = len(new_ar)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
