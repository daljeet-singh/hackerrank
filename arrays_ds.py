#!/bin/python

import os
import sys

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    print " ".join(str(x) for x in arr[::-1])