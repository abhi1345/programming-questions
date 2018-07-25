#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    mylist = [0]*(n+1)
    for q in queries:
        x, y, incr = q[0], q[1], q[2]
        mylist[x-1] += incr
        if((y)<=len(mylist)): 
            mylist[y] -= incr
    mymax = 0
    x = 0
    for i in mylist:
        x=x+i;
        
        if(mymax<x): 
            mymax=x
            
    return(mymax)

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
