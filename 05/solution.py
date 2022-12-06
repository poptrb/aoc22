#!/usr/bin/env python

import re
from collections import deque

input_stacks, instructions = [], []

move_pattern = "^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$"
with open('input.txt', 'r') as file:
    while True:
      line = file.readline()
      if line == '\n':
        continue
      elif 'move' in line:
        instruction = re.match(move_pattern, line).groups()
        instructions.append(list(map(lambda x: int(x), instruction)))
      elif 'move' not in line and line:
        input_stacks.append(line.strip('\n'))
      else:
          break

def parse_input(input_stacks, line_idx):
  elems = list(map(lambda x: x[line_idx * 4 + 1], input_stacks[-2::-1]))
  return [ x for x in elems if not x == ' ' ]

def create_stacks(input_stacks):
  return [ deque(parse_input(input_stacks, i)) for i in range(0, len(input_stacks)) ]

def move(stacks, qty, src, dest):
  [ stacks[dest - 1].append(stacks[src - 1].pop()) for i in range(0, qty) ]

def move_multiple(stacks, qty, src, dest):
  temp = [ stacks[src - 1].pop() for i in range(0, qty) ][::-1]
  stacks[dest -1].extend(temp)

def top_of_stacks(stacks):
  answer = ''
  for stack in stacks:
    try:
      answer += stack.pop()
    except IndexError:
      continue
  return answer

stacks = create_stacks(input_stacks)
for instruction in instructions:
  move(stacks, *instruction)

sol1 = top_of_stacks(stacks)

stacks = create_stacks(input_stacks)
for instruction in instructions:
  move_multiple(stacks, *instruction)

sol2 = top_of_stacks(stacks)

print(f"Solution 1: {sol1}\nSolution 2: {sol2}")
