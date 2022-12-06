#!/usr/bin/env python

from collections import deque

with open('input.txt', 'r') as file:
    data = file.readline()

def is_beggining_of_seq(pattern, msg_length):
  return len(set(pattern)) == len(pattern) if len(pattern) == msg_length else False

def find_seq_beginning(data, msg_length):
  char, idx = data[0], 0
  buf = deque([char])
  while not is_beggining_of_seq(buf, msg_length) and not char == '\n':
      idx += 1
      if len(buf) == msg_length:
          buf.popleft()
          buf.append(data[idx])
      else:
          buf.append(data[idx])
  return idx + 1

sol1 = find_seq_beginning(data, 4)
sol2 = find_seq_beginning(data, 14)
print(f"Solution 1: {sol1}\nSolution 2: {sol2}")
