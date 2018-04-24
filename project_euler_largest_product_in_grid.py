#!/bin/python

import sys

grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)
maxp = 0
rows, cols, path_size = len(grid), len(grid[0]), 4
for i in range(rows):
    for j in range(cols - path_size + 1):
        phv = max(grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3],
                  grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i])
        if i <= rows-path_size:
           pdd = max(grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3],
                     grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j])
        maxp = max(maxp, phv, pdd)
 
print maxp


# initial_max = None
# for i in range(20):
#     for j in range(20):
#         for direction in ((0,1), (1,0), (1,1), (-1,-1)):
#            try:
#               product = 1
#               for l in range(4):
#                  product *= grid[i + direction[0]*l][j + direction[1]*l]
#               if product > initial_max:
#                   initial_max = product
#            except IndexError:
#                pass
# print initial_max