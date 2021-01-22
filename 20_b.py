import sys
from printf import printf
import copy
import re
from copy import copy, deepcopy

# Get a list of gates, and the other gates they can reach with the number of steps like this:
#   LP: [[x, y], [[FDi, 10], [RFo, 20]]]

all_steps = []


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
    dir = ''
    if map[y][x].isalpha() and map[y][x+1].isalpha() and map[y][x+2] == '.':
       label = map[y][x] + map[y][x+1]
       x_coord = x+2
       y_coord = y
       if x < max_x/2:
         label += 'o'
       else:
         label += 'i'

    if map[y][x] == '.' and map[y][x+1].isalpha() and map[y][x+2].isalpha():
       label = map[y][x+1] + map[y][x+2]
       x_coord = x
       y_coord = y
       if x < max_x/2:
         label += 'i'
       else:
         label += 'o'

    if map[y][x].isalpha() and map[y+1][x].isalpha() and map[y+2][x] == '.':
       label = map[y][x] + map[y+1][x]
       x_coord = x
       y_coord = y+2
       if y < max_y/2:
         label += 'o'
       else:
         label += 'i'

    if map[y][x] == '.' and map[y+1][x].isalpha() and map[y+2][x].isalpha():
       label = map[y+1][x] + map[y+2][x]
       x_coord = x
       y_coord = y
       if y < max_y/2:
         label += 'i'
       else:
         label += 'o'

    if label != '':
      pair = []
      pair.append(x_coord)
      pair.append(y_coord)

      portals[label] = []
      portals[label].append(pair)










pair = portals['AAo']
start_x = pair[0][0]
start_y = pair[0][1]

pair = portals['ZZo']
end_x = pair[0][0]
end_y = pair[0][1]






def moves():
  global map
  global portals
  result_portal_list = []
  made_move = 1
  while made_move == 1:
    made_move = 0 
    for z in portals.keys():
      pair = portals[z]
      a = pair[0]
      if isinstance(map[a[1]][a[0]], (int, long)):
        steps = map[a[1]][a[0]]
        res = []
        res.append(z)
        res.append(steps)
        if res not in result_portal_list:
          if steps > 0:
            result_portal_list.append(res)

    for x in range(0, max_x+1):
      for y in range(0, max_y+1):
        if isinstance(map[y][x], (int, long)):
          steps = map[y][x]
          if map[y-1][x] == '.':
            map[y-1][x] = steps+1
            made_move = 1
          if map[y+1][x] == '.':
            map[y+1][x] = steps+1
            made_move = 1
          if map[y][x-1] == '.':
            map[y][x-1] = steps+1
            made_move = 1
          if map[y][x+1] == '.':
            map[y][x+1] = steps+1
            made_move = 1
  return result_portal_list

 
for start_portal in portals.keys():
  copy_map = deepcopy(map)
  pair = portals[start_portal]
  start_x = pair[0][0]
  start_y = pair[0][1]
  map[start_y][start_x]=0
  possible_portals = moves()
  portals[start_portal].append(possible_portals)
  map = deepcopy(copy_map)
  

def do_move(s, p, l):
  global all_steps
  if s > 10000:
    return
  if p == 'AAo' and s > 0:
    return
  if p == 'ZZo':
    return


  for dest in portals[p][1]:
    if dest[0] == 'ZZo' and l == 0:
      all_steps.append(s + dest[1])
    if dest[0] == 'ZZo':
      continue

    if dest[0] == 'AAo':
      continue


    steps = s + dest[1] + 1
    if dest[0][2] == 'i':
      level = l +1
    else:
      level = l - 1
    if level < 0:
      continue
    if level > 100:
      return
    jump = dest[0]
    j = jump[:-1]
    if dest[0][2] == 'i':
      j+= 'o'
    else:
      j += 'i'
    do_move(steps, j, level)

start_portal = 'AAo'
steps = 0
level = 0
do_move(steps, start_portal, level)
print "Part 2: " + str(min(all_steps))
