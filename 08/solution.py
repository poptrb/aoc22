#!/usr/bin/env python
import time

def read_grid(filename):
  with open(filename, 'r') as file:
    lines = map(lambda x: x.rstrip('\n'), file.readlines())
    return [[ [int(char), False] for char in line ] for line in lines ]

def visible(grid):
  len_rows, len_cols = len(grid), len(grid[0])
  maxes = [[ -1 for col in grid ], [ -1 for x in grid[0]]]
  for row in range(len_rows):
    for col in range(len_cols):
      if grid[row][col][0] > maxes[0][row]:
        maxes[0][row], grid[row][col][1] = grid[row][col][0], True 
      if grid[row][col][0] > maxes[1][col]:
        maxes[1][col], grid[row][col][1] = grid[row][col][0], True

  maxes = [[ -1 for col in grid ], [ -1 for x in grid[0]]]
  for row in range((len_rows - 1),0,-1):
    for col in range((len_cols - 1),0,-1):
      if grid[row][col][0] > maxes[0][row]:
        maxes[0][row], grid[row][col][1] = grid[row][col][0], True
      if grid[row][col][0] > maxes[1][col]:
        maxes[1][col], grid[row][col][1] = grid[row][col][0], True

  return sum([ sum([ 1 for x in row if x[1] ]) for row in grid])

def max_scenic(grid):
  len_rows, len_cols, best_score = len(grid), len(grid[0]), 0
  for row in range(len_rows):
    for col in range(len_cols):
      score = 1
      for row_step, col_step in zip([1, -1, 0 , 0], [0, 0, -1, 1]):
        s_row, s_col, s  = row, col, 0
        while True:
          s_row += row_step
          s_col += col_step
          if s_row < 0 or s_row > len_rows - 1:
            break
          if s_col < 0 or s_row > len_cols - 1:
            break
          try:
            if grid[s_row][s_col][0] < grid[row][col][0]:
              s += 1
            else:
              s += 1
              break
          except IndexError:
            break
        score *= s
      best_score = max(score, best_score)
  return best_score

grid = read_grid('input.txt')
print(f"Solution 1: {visible(grid)}\nSolution 2: {max_scenic(grid)}")
