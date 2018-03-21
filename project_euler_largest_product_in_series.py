#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input().strip()
    largestProduct = 0
    for i in range(0, len(num) - k):
        product = 1
        for j in range(i, i + k):
            product *= int(num[j: j + 1])
        if product > largestProduct:
            largestProduct = product
    print (largestProduct)