#!/bin/python

import sys

def sum_square(num):
    return ( num*(num+1)/2 )*( num*(num+1)/2 )

def square_sum(num):
    return num*(num+1)*(2*num+1)/6

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sum_square(n) - square_sum(n)