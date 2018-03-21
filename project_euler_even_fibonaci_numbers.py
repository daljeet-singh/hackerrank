#!/bin/python

import sys

def even_fibonacci_sum(n):
    fn_2 = 2
    fn_1 = 8
    sum = 10
    while True :
        fn = 4 * fn_1 + fn_2
        if fn >= n: return sum
        sum += fn
        fn_2, fn_1 = fn_1, fn

t = int(raw_input().strip())
for i in range(t):
    n = int(raw_input().strip())
    print(even_fibonacci_sum(n))