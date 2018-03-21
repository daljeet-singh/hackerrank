#!/bin/python

import sys
# import time

# all_prime = []

# def generate_prime():
#     all_prime.append(2)
#     for i in xrange( 3, 1299709 , 2 ):
#         if isPrime(i):
#             all_prime.append(i)

# def get_prime_at(position):
#     return all_prime[position-1]

# def isPrime(a):
#     return all(a % i for i in xrange(2, a))

# t = int(raw_input().strip())
# start_time = time.time()
# generate_prime()
# print("--- %s seconds ---" % (time.time() - start_time))
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     print get_prime_at(n)


# def isPrime(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def nthPrime(n):
#     numberOfPrimes = 0
#     prime = 1
#     while numberOfPrimes < n:
#         prime += 1
#         if isPrime(prime):
#             numberOfPrimes += 1
#     return prime

# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     print nthPrime(n)

# limit=125000
# primes = [True] * limit
# primes[0],primes[1] = [None] * 2

# def fast_nth_prime(n, limit=125000):
#     if limit % 2 != 0: limit += 1
#     count = 0
#     for ind,val in enumerate(primes):
#         if val is True:
#             primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
#             count += 1
#         if count == n: return ind
#     return False
 

# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     print fast_nth_prime(n)


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]

prime = [0]+prime_sieve(105000)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print prime[n]
