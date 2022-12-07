#!/usr/bin/env python

from collections import namedtuple

Node = namedtuple('Node', ['dirs', 'files'])

with open('input.txt') as file:
    lines = [ line.strip('\n') for line in file.readlines() ]

def parse(lines):
    tree = {}
    idx, length, dir_stack = 0, len(lines), []
    while idx < length:
      match lines[idx].split():
        case ['$', 'cd', '..']:
          idx += 1
          del dir_stack[-1]
        case ['$', 'cd', path]:
          dirs, files = [], []
          dir_stack.append(path)
          idx += 2 # Step over '$ ls'
          while idx < length and not lines[idx][0] == '$':
            if lines[idx][:3] == 'dir':
              dirs.append(lines[idx].split()[1])
            else:
              files.append(int(lines[idx].split()[0]))
            idx += 1
          full_path = dir_stack[0] + '/'.join(dir_stack[1:])
          tree[full_path] = Node(dirs, files)
    return tree

def size(path):
  sep = '' if path == '/' else '/'
  return sum(tree[path].files) + sum([size(path + sep + d) for d in tree[path].dirs])

tree = parse(lines)
dir_sizes = [ size(path) for path in tree.keys() ]

sol1 = sum(list(filter(lambda x: x < 100000, dir_sizes)))

size_target =  30000000 - (70000000 - dir_sizes[0])
sol2 = min([sz for sz in dir_sizes if sz > size_target ])

print(f"Solution 1: {sol1}\nSolution 2: {sol2}")
