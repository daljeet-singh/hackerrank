#!/bin/python

import sys

# if __name__ == "__main__":
#     n, m = raw_input().strip().split(' ')
#     n, m = [int(n), int(m)]
#     arr = [0] * n
#     for a0 in xrange(m):
#         a, b, k = raw_input().strip().split(' ')
#         a, b, k = [int(a), int(b), int(k)]
#         for i in range(a-1,b-1):
#             arr[i] += k
#     print max(arr)

n, inputs = raw_input().strip().split(' ')
n, inputs = [int(n), int(inputs)]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = raw_input().strip().split(' ')
    x, y, incr = [int(x), int(y), int(incr)]
    list[x-1] += incr
    if((y)<=len(list)):
        list[y] -= incr;
max = x = 0
for i in list:
    x=x+i;
    if(max<x):
        max=x;
print(max)