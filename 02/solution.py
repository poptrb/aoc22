#!/usr/bin/env python

# A, X = rock; B, Y = paper; C, Z = scissors
#    | A   B   C
#    |----------
#  X | 0   1   -1
#  Y | 1  0   1
#  Z | -1   -1  0


def convert(x):
  """Convert a rock, paper or scissors symbol to either 0, 1 or 2"""
  return ord(x) - 88 if ord(x) -64 >= 24 else ord(x) - 65

with open('input.txt', 'r') as file:
  data = [ x.strip('\n').split(' ') for x in file.readlines() ]

# Y is my choice, X is opponent's
outcome = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
results = [ convert(y) + 1 + 3 * ( - outcome[convert(x)][convert(y)] + 1)  for x, y in data]

print(sum(results))
