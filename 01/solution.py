#!/usr/bin/env python

with open('input.txt', 'r') as file:
  data = ''.join(file.readlines()).split('\n\n')

sol1 = (max([sum(
    [ int(y) for y in x.split(' ') if y ]) for x in map(lambda x: x.replace('\n', ' '),data)]))

sol2 = sum(sorted(
    [sum([ int(y) for y in x.split(' ') if y ]) for x in map(lambda x: x.replace('\n', ' '),data)])[-3:])

print(f"Solution 1: {sol1}\nSolution 2: {sol2}")
