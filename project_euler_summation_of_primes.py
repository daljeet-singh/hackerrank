#!/bin/python

import sys

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]

prime = [0]+prime_sieve(1000000)

def get_sum(n):
    return 
    sum_value = 0
    for i in range(1,n):
        if prime[i] <= n:
            sum_value += prime[i]
        else:
            return sum_value
    return sum_value


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    prime = [0]+prime_sieve(n)
    print get_sum(n)


# from math import sqrt
# def sum_primes(limit):
#     sieve = range(limit+1); sieve[1] = 0
#     for n in xrange(2, int(sqrt(limit))+1):
#         if sieve[n] > 0:
#             for i in xrange(n*n, limit+1, n): sieve[i] = 0
#     return sum(sieve)

# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     print sum_primes(n)


# number to find summation of all primes below number
# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     numbers = set(xrange(3, n + 1, 2)) 
#     for number in xrange(3, int(n ** 0.5) + 1):
#         if number not in numbers:
#             continue
#         num = number
#         while num < n:
#             num += number
#             if num in numbers:
#                 numbers.remove(num)
#     print 2 + sum(numbers)