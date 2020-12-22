import sys
from copy import copy, deepcopy

with open("10_a_input.txt") as f:
    content = f.readlines()

map = []
content = [x.strip() for x in content]
map_y = 0
for line in content:
  row = []
  map_x = 0
  for pos in line:
    row.append(pos)
    map_x += 1
  map.append(row)
  map_y += 1

def count_visible(map):
  count = 0
  for row in map:
    for char in row:
      if char == '#':
        count = count + 1
  return count -1

def print_map(map):
  for row in map:
    row_s = ''
    for char in row:
      row_s += str(char)
    print row_s

print_map(map)
result = deepcopy(map)
orig_map = deepcopy(map)


asteroids_l = []
for x in range(0, map_x):
  for y in range(0, map_y):
    if map[y][x] == '#':
      pair = []
      pair.append(x)
      pair.append(y)
      asteroids_l.append(pair)

print asteroids_l

def block(map, a_x, a_y, x, y):
  print "asteroid at " + str(a_x) + "," + str(a_y) + " is blocked by asteroid at " + str(x) + "," + str(y)

  x_jump = x - a_x
  y_jump = y - a_y
  if abs(x_jump) > abs(y_jump):
    max_factor = abs(x_jump)
  else:
    max_factor = abs(y_jump)

  print "max_factor = " + str(max_factor)
  for fac in range(1, max_factor+1):
    if abs(x_jump) % fac == 0 and abs(y_jump) % fac == 0:
      my_fac = fac
  print "x_jump = " + str(x_jump) + " , y_jump = " + str(y_jump) 
  print "x_jump = " + str(x_jump) + " , y_jump = " + str(y_jump) + " , my_fac = " + str(my_fac)
  x_jump = x_jump / my_fac
  y_jump = y_jump / my_fac

  print "Blocking asteroids at jumps of " + str(x_jump) + "," + str(y_jump)

  block_x = x + x_jump
  block_y = y + y_jump

  while block_x >= 0 and block_x < map_x and block_y >= 0 and block_y < map_y:
    print "  Blocking " + str(block_x) + "," + str(block_y)
    map[block_y][block_x] = 'B'
    block_x = block_x + x_jump
    block_y = block_y + y_jump

  return map  

#asteroids_l = [[1, 0]]
for asteroid in asteroids_l:
  map = deepcopy(orig_map)

  print "Doing asteroid: "
  print asteroid
  asteroid_x = asteroid[0]
  asteroid_y = asteroid[1]

  for layer in range(1, map_x+1):
    print "----LAYER = " + str(layer)
    min_x = asteroid_x - layer
    max_x = asteroid_x + layer
    min_y = asteroid_y - layer
    max_y = asteroid_y + layer
    print "MinX = " + str(min_x)
    print "MaxX = " + str(max_x)
    print "MinY = " + str(min_y)
    print "MaxY = " + str(max_y)

    for x in range(min_x, max_x+1):
      if x < 0 or x >= map_x:
        print "Skipping x = " + str(x)
        continue
      if min_y >= 0:
        print "  Checka: " + str(x) + ',' + str(min_y)
        if map[min_y][x] == '#':
          map = block(map, asteroid_x, asteroid_y, x, min_y)
      if max_y < map_x:
        print "  Checkb: " + str(x) + ',' + str(max_y)
        if map[max_y][x] == '#':
          map = block(map, asteroid_x, asteroid_y, x, max_y)
    for y in range(min_y, max_y+1):
      if y < 0 or y >= map_y:
        print "Skipping y = " + str(y)
        continue
      if max_x < map_x:
        print "  Checkc: " + str(max_x) + ',' + str(y)
        if map[y][max_x] == '#':
          map = block(map, asteroid_x, asteroid_y, max_x, y)
      if min_x >= 0: 
        print "  Checkd: " + str(min_x) + ',' + str(y)
        if map[y][min_x] == '#':
          map = block(map, asteroid_x, asteroid_y, min_x, y)
  result[asteroid_y][asteroid_x] = count_visible(map)
  print_map(map)
  print '--------------'

print_map(result)
def get_best(map):
  best = 0
  best_pair = [[],[]]
  y = 0
  for row in map:
    x = 0
    for num in row:
      if isinstance(num,int):
        if num > best:
          best = num 
          best_pair = str(x) + ',' + str(y)
      x = x + 1
    y = y + 1
  print
  print "Best is "
  print best_pair
  print "With " + str(best) + " other asteroids detected"


get_best(result)
