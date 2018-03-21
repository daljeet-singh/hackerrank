#!/bin/python

import sys

def staircase(n):
    spaces = n-1
    while( spaces >= 0 ):
        print ' ' * spaces + '#' * (n-spaces)
        spaces -= 1

if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)