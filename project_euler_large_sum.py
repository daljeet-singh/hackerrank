#!/bin/python

import sys

t = int(raw_input().strip())
sum_val = 0
for a0 in xrange(t):
    n = int(raw_input().strip())
    sum_val += n
print str(sum_val)[:10]