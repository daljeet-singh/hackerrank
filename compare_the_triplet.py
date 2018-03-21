#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    a = [int(a0),int(a1),int(a2)]
    b = [int(b0),int(b1),int(b2)]
    sa = sb = 0
    for i in xrange(3):
        if a[i] > b[i]:
            sa += 1
        elif a[i] < b[i]:
            sb += 1
    print str(sa) + ' ' + str(sb)


a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)