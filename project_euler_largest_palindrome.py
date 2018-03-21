#!/bin/python

import sys

def max_pali_number(num):
    i = 999
    max_num = None
    while i > 99:
        j = 999
        while j > 99:
            n = i*j
            if max_num > 0 and n <= max_num:
                break
            if n < num and n > max_num and isPalindrome(n):
                max_num = n
            j -= 1
        i -= 1
    return max_num


def isPalindrome(num):
    return str(num) == str(num)[::-1]

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    print max_pali_number(n)