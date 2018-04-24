#!/bin/python

import sys

# def prime_sieve(n):
#     sieve = [True] * (n//2)
#     for i in xrange(3,int(n**0.5)+1,2):
#         if sieve[i//2]:
#             sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
#     return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]

# prime = [0]+prime_sieve(1000000)

# def get_sum(n):
#     j2 = [i for i in prime if i <= n]
#     return sum(j2)


# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     print get_sum(n)




import sys

limit = 1000000
limit = 10
suml = [0] * limit
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        suml[i] = suml[i-1] + i
        for n in range(i*i, limit, i):
            a[n] = False
    else:
        suml[i] = suml[i-1]

t = int(raw_input().strip())
for a0 in range(t):
    n = int(raw_input().strip())
    print(suml[n])