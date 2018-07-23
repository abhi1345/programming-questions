#!/bin/python3

import sys

primes = [2,3,5,7,11,13]

def isPrime(n):
    if n in primes:
        return True
    end = int(n**(0.5))
    for i in range(2, end+1):
        if n % i == 0:
            return False
        
    primes.append(n)
    return True
    

    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    start = primes[-1]
    while len(primes) < n:
        y = isPrime(start)
        start += 1
        
    print(primes[n-1])
    
        
   
