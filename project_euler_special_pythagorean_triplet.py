#!/bin/python

import sys


# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     got = 0
#     max_val = None
#     for a in range(1, n):
#         for b in range(a, n):
#             c = n - a - b
#             if c > 0:
#                 if c*c == a*a + b*b:
#                     if a*b*c > max_val:
#                         max_val = a*b*c
#                     got = 1
#                     break
#     if got == 0:
#         print -1
#     else:
#         print max_val

# # import time

# def py_number(n):
#     for num in range(n/2,1,-1):
#         for dig in range(n - num,num, -1):
#             i = n - num - dig
#             # print "%s,%s,%s"% ( num,dig,i)
#             if num * num + dig * dig == i * i:
#                 # print "%s,%s,%s"% ( num,dig,i)
#                 return num * dig * i
#     return -1

# t = int(raw_input().strip())

# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     # start = time.time()
#     print py_number(n)
    
# # elapsed = time.time() - start               
# # print("Time: {:.5f} seconds".format(elapsed))

# def py_number(n):
#     for a in range(n/2,1,-1):
#         num * dig + 1000 * i == 500000


# t = int(raw_input().strip())

# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     # start = time.time()
#     print py_number(n)

# import time

# def py_number(n):
#     for a in range(n/2,1,-1):
#         for b in range(n/2,a,-1):
#             c = (n - a) - b
#             if a < b < c:
#                 if a**2 + b**2 == c**2:
#                     print "%s,%s,%s" % ( a,b,c)
#                     return a * b * c
#     return -1


# t = int(raw_input().strip())

# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     # start = time.time()
#     print py_number(n)
#     # elapsed = time.time() - start 
#     # print("Time: {:.5f} seconds".format(elapsed)) 

import time

def py_number(n):
    max_val = -1
    for a in range(n/2,1,-1):
        b = (n**2-2*a*n)/(2*n-2*a)
        c = n-a-b
        if a > 0 and b > 0 and c > 0:
            if a**2 + b**2 == c**2:
                if max_val < a*b*c:
                    max_val = a*b*c
    return max_val


t = int(raw_input().strip())

for a0 in xrange(t):
    n = int(raw_input().strip())
    # start = time.time()
    print py_number(n)
    # elapsed = time.time() - start 
    # print("Time: {:.5f} seconds".format(elapsed)) 