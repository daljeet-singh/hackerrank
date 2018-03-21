#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
max_value = None
for i in range( 0,4 ):
    start = j = 0
    while start < 4:
        sum_value = 0
        for y in range( j, j+3 ):
            b = y+start
            sum_value += arr[i][b]
            sum_value += arr[i+2][b]
        sum_value += arr[i+1][b-1]
        if max_value < sum_value:
            max_value = sum_value
        start += 1
print max_value