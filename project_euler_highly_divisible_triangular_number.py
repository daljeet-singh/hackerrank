#!/bin/python

import sys
from math import *

max_value = 10
triangle = [0]
triangle_generator = {}
final_triangle_generator = {}

def divisors(n):
    limit = int(sqrt(n))
    divisors_list = []
    for i in range(1, limit+1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n/i:
                divisors_list.append(n/i)
    return len(divisors_list)


def generate_triangle():
    for i in xrange(1,max_value+1):
        triangle.append(triangle[i-1]+i)
        factor_count = divisors(triangle[i])
        triangle_generator[triangle[i]] = factor_count

generate_triangle()

def get_triangle_number(n):
    min_val = 100000
    keylist = triangle_generator.keys()
    keylist.sort()
    for key in keylist:
        if( triangle_generator[key] > n ):
            if min_val > key:
                min_val = key
    return min_val

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print get_triangle_number(n)
