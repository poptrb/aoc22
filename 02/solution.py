#!/usr/bin/env python

# 1.
# A, X = rock; B, Y = paper; C, Z = scissors
# -1 = loss, 0 = draw, 1 = win

#    | A   B   C
#    |----------
#  X | 0   1  -1
#  Y | 1   0   1
#  Z |-1  -1   0

# 2.
# X = loss, Y = draw, Z = win
# -1 = rock, 0 = paper, 1 = scrissors

#    | A   B   C
#    |----------
#  X | 1  -1   0
#  Y |-1   0   1
#  Z | 0   1  -1


def convert(x):
  """Convert a rock, paper or scissors symbol to either 0, 1 or 2"""
  return ord(x) - 88 if ord(x) -64 >= 24 else ord(x) - 65

with open('input.txt', 'r') as file:
  data = [ x.strip('\n').split(' ') for x in file.readlines() ]

outcome = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
my_play = [[1, -1, 0], [-1, 0, 1], [0, 1, -1]]

# y is my choice, x is opponent's
sol1 = sum([ convert(y) + 1 + 3 * ( - outcome[convert(x)][convert(y)] + 1)  for x, y in data])
# y is outcome, x is opponent's choice
sol2 = sum([ convert(y) * 3 + my_play[convert(x)][convert(y)] + 2 for x,y in data ])

print(f"Solution 1: {sol1}\nSolution 2: {sol2}")
