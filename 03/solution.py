#!/usr/bin/env python

with open('input.txt', 'r') as file:
    data = list(map(lambda x: x.strip('\n'), file.readlines()))

def priority(x):
  return  ord(x) - 96 if ord(x)  >= 97 else ord(x) - 38

sol1 = sum([
    priority(list(set( x[:(len(x)//2)] ) & set(x[(len(x)//2):]))[0]) for x in data])

sol2 = sum([
    priority(list(set(data[x]) & set(data[x+1]) & set(data[x+2]))[0]) for x in range(0,len(data),3)])

print(f"Solution 1: {sol1}\nSolution 2: {sol2}")
