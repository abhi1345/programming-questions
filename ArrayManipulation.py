#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    x = 0
    arr = [0]*(n+1)
    maxn = 0
    for q in queries:
        a, b, k = q
        arr[a-1] += k
        arr[b] -= k
    for n in arr:
        x += n
        if x > maxn:
            maxn = x
    return maxn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
