#!/usr/bin/env python

from itertools import chain

with open('input.txt', 'r') as file:
  data =list(map(lambda x: x.strip('\n'), file.readlines()))

count1, count2 = 0, 0
for d in data:
  # Parse the ranges into a list of 4 elements
  min_a, max_a, min_b, max_b = \
    map(lambda x: int(x), list(chain(*list(map(lambda x: x.split('-'), d.split(','))))))

  if (min_a <= min_b and max_a >= max_b) or (min_b <= min_a and max_b >= max_a):
    count1 += 1
  if min_a > min_b:
      min_a, max_a, min_b, max_b = min_b, max_b, min_a, max_a
  if min_b >= min_a and min_b <= max_a:
      count2 += 1

print(f"Solution 1: {count1}\nSolution 2: {count2}")
