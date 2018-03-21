#!/bin/python

import sys

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    ans = 1
    for i in range( 1, n+1 ):
        ans = lcm( ans, i )
    print ans