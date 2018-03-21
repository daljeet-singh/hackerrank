#!/bin/python

import sys

def jumpingOnClouds(c, k):
    # Complete this function

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = map(int, raw_input().strip().split(' '))
    result = jumpingOnClouds(c, k)
    print result
