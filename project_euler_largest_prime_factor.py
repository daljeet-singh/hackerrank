#!/bin/python

import sys

# def largest_prime(n):
#     if isPrime(n):
#         return n
#     if isPrime(n/2):
#         return n/2
#     for i in range( n/2, 1, -1 ):
#         if isPrime(i) and isFactor(i,n):
#             return i
    
# def isPrime(a):
#     return all(a % i for i in xrange(2, a))

# def isFactor(a,n):
#     if n%a == 0:
#         return 1
#     else:
#         return 0

# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = long(raw_input().strip())
#     print largest_prime(n)

def max__prime_factor(num):
    maxp = None
    factor = 2 
    while factor * factor <= num:
        while num % factor == 0:
            maxp = factor
            num /= factor
        factor += 1
    if (num > 1): 
        return num 
    return maxp

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    print max__prime_factor(n)