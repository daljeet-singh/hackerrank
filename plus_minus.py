#!/bin/python

import sys

def plusMinus(arr):
    p = n = z = 0
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    p = p/float(len(arr))
    n = n/float(len(arr))
    z = z/float(len(arr))
    print( "%.6f" % p )
    print( "%.6f" % n )
    print( "%.6f" % z )

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)