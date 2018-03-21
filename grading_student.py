#!/bin/python
n = int(raw_input().strip())
for i in range(0, n):
    grade = int(raw_input().strip())
    if grade >= 38 and grade % 5 >= 3:
      grade = ((grade / 5) + 1) * 5
    print grade