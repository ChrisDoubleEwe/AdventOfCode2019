import sys
from copy import copy, deepcopy
import itertools


with open("18_test4.txt") as f:
    content = f.readlines()

map = []
content = [x.strip() for x in content]
map_y = -1
for line in content:
  map_y += 1
  map_x = -1
  row = []
  for v in line.strip():
    row.append(v)
    map_x += 1
  map.append(deepcopy(row))

def print_map(m):
  for row in m:
    c_str = ''
    for c in row:
      c_str += str(c)
    print c_str

print_map(map)

nodes = []

for row in map:
  for c in row:
    if c.islower():
      nodes.append(c) 

print nodes
for i in list(itertools.permutations(nodes)):
  print i
