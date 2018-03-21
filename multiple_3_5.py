#!/bin/python

def sum(n, k):
    d = n // k
    return k * (d * (d+1)) // 2
  
def euler1(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)

t = int(raw_input().strip())
for i in range(t):
    N = int(raw_input().strip())
    print euler1(N - 1)