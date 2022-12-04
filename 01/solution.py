#!/usr/bin/env python

with open('input.txt', 'r') as file:
  data = ''.join(file.readlines()).split('\n\n')

print(max([sum([ int(y) for y in x.split(' ') if y ]) for x in map(lambda x: x.replace('\n', ' '),data)]))
