#!/bin/python

S = [k*k for k in xrange(1,101)]
n = len(S)
k = n/2

sums = [{0:1}]
for i in xrange(k):
    sums += [{}]

for s in S:
    for j in xrange(k-1,-1,-1):
        L = sums[j].keys()
        for s0 in L:
            s1 = s + s0
            if sums[j][s0] == 2 or s1 in sums[j+1]:
                sums[j+1][s1] = 2
            else:
                sums[j+1][s1] = 1

print sum(i for i in sums[k] if sums[k][i] == 1)