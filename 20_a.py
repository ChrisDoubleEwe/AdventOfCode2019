import sys
from printf import printf
import copy
import re


with open("20_input.txt") as f:
    content = f.readlines()

map = []
max_x = 0
max_y = 0
for line in content:
  max_y += 1
  blank_row = []
  row = []
  for c in line.strip('\n'):
    row.append(c)
    blank_row.append(' ')
  row.append(' ')
  row.append(' ')
  row.append(' ')
  map.append(row)
map.append(blank_row)
map.append(blank_row)
map.append(blank_row)

x = 0
y = 0
max_x = len(blank_row) - 3


def print_map():
  global map
  for row in map:
    for c in row:
      printf(str(c))
    print ' ' 

portals = {}
for x in range(0, max_x+1):
  for y in range(0, max_y+1):
    label = ''
    if map[y][x].isalpha() and map[y][x+1].isalpha() and map[y][x+2] == '.':
       label = map[y][x] + map[y][x+1]
       x_coord = x+2
       y_coord = y
    if map[y][x] == '.' and map[y][x+1].isalpha() and map[y][x+2].isalpha():
       label = map[y][x+1] + map[y][x+2]
       x_coord = x
       y_coord = y
    if map[y][x].isalpha() and map[y+1][x].isalpha() and map[y+2][x] == '.':
       label = map[y][x] + map[y+1][x]
       x_coord = x
       y_coord = y+2
    if map[y][x] == '.' and map[y+1][x].isalpha() and map[y+2][x].isalpha():
       label = map[y+1][x] + map[y+2][x]
       x_coord = x
       y_coord = y
    if label != '':
      pair = []
      pair.append(x_coord)
      pair.append(y_coord)

      if label in portals.keys():
        portals[label].append(pair)
      else:
        portals[label] = []
        portals[label].append(pair)





#print_map()

pair = portals['AA']
start_x = pair[0][0]
start_y = pair[0][1]

pair = portals['ZZ']
end_x = pair[0][0]
end_y = pair[0][1]

portals.pop('AA')
portals.pop('ZZ')




map[start_y][start_x]=0

def moves():
  global map
  global portals
  for z in portals.keys():
    pair = portals[z]
    a = pair[0]
    b = pair[1]
    if isinstance(map[a[1]][a[0]], (int, long)) and map[b[1]][b[0]] == '.':
      steps = map[a[1]][a[0]]
      map[b[1]][b[0]] = steps + 1
    if isinstance(map[b[1]][b[0]], (int, long)) and map[a[1]][a[0]] == '.':
      steps = map[b[1]][b[0]]
      map[a[1]][a[0]] = steps + 1
  for x in range(0, max_x+1):
    for y in range(0, max_y+1):
      if isinstance(map[y][x], (int, long)):
        steps = map[y][x]
        if map[y-1][x] == '.':
          map[y-1][x] = steps+1
        if map[y+1][x] == '.':
          map[y+1][x] = steps+1
        if map[y][x-1] == '.':
          map[y][x-1] = steps+1
        if map[y][x+1] == '.':
          map[y][x+1] = steps+1

 
for iter in range(0, 50000000):
  #print '------------'
  moves()
  #print_map()
  if isinstance(map[end_y][end_x], (int, long)):
    print map[end_y][end_x]
    exit()


