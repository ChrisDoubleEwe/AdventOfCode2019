import sys
import math 

import numpy as np
from copy import copy, deepcopy

with open("10_a_input.txt") as f:
    content = f.readlines()

def anti_clockwise(x,y):
    alpha = math.degrees(math.atan2(y,x))
    return ((alpha + 360) + 90) % 360

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

def aster_sort(my_list):
  global start_x
  global start_y

  result_list = []
  lowest = 360
  while len(my_list) > 0:
    lowest = 360
    for i in range(0, len(my_list)):
      #print str(i) + " out of " + str(len(my_list))
      pair = my_list[i]
      delta_x = pair[0]-start_x
      delta_y = pair[1]-start_y
      angle = anti_clockwise(delta_x, delta_y)
      if angle < lowest:
        lowest = angle
        lowest_index = i
    pair = my_list.pop(lowest_index)
    result_list.append(pair)
  return result_list


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

def sort_unique(l):
  res = []
  for p in l:
    if p in res:
      continue
    else:
      res.append(p)
  return res

def block(map, a_x, a_y, x, y):
  global unordered_asteroids
  #print "asteroid at " + str(a_x) + "," + str(a_y) + " is blocked by asteroid at " + str(x) + "," + str(y)
  pair = []
  pair.append(x)
  pair.append(y)
  unordered_asteroids.append(pair)

  x_jump = x - a_x
  y_jump = y - a_y
  if abs(x_jump) > abs(y_jump):
    max_factor = abs(x_jump)
  else:
    max_factor = abs(y_jump)

  for fac in range(1, max_factor+1):
    if abs(x_jump) % fac == 0 and abs(y_jump) % fac == 0:
      my_fac = fac
  #print "x_jump = " + str(x_jump) + " , y_jump = " + str(y_jump) + " , my_fac = " + str(my_fac)
  x_jump = x_jump / my_fac
  y_jump = y_jump / my_fac


  block_x = x + x_jump
  block_y = y + y_jump

  while block_x >= 0 and block_x < map_x and block_y >= 0 and block_y < map_y:
    map[block_y][block_x] = 'B'
    block_x = block_x + x_jump
    block_y = block_y + y_jump

  return map  

vaporized_asteroids = []

start_x = 31
start_y = 20
start = []
start.append(start_x)
start.append(start_y)
asteroids_l = []
asteroids_l.append(start)

last_len = -1
while True:
  if len(vaporized_asteroids) == last_len:
    break
  last_len = len(vaporized_asteroids) 

  unordered_asteroids = []
  for asteroid in asteroids_l:
    map = deepcopy(orig_map)
    for v in vaporized_asteroids:
      map[v[1]][v[0]] = '.'

    asteroid_x = asteroid[0]
    asteroid_y = asteroid[1]

    for layer in range(1, map_x+1):
      min_x = asteroid_x - layer
      max_x = asteroid_x + layer
      min_y = asteroid_y - layer
      max_y = asteroid_y + layer

      for x in range(min_x, max_x+1):
        if x < 0 or x >= map_x:
          continue
        if min_y >= 0:
          if map[min_y][x] == '#':
            map = block(map, asteroid_x, asteroid_y, x, min_y)
        if max_y < map_x:
          if map[max_y][x] == '#':
            map = block(map, asteroid_x, asteroid_y, x, max_y)
      for y in range(min_y, max_y+1):
        if y < 0 or y >= map_y:
          continue
        if max_x < map_x:
          if map[y][max_x] == '#':
            map = block(map, asteroid_x, asteroid_y, max_x, y)
        if min_x >= 0: 
          if map[y][min_x] == '#':
            map = block(map, asteroid_x, asteroid_y, min_x, y)
    result[asteroid_y][asteroid_x] = count_visible(map)
    print '--------------'
    print_map(map)
    print '--------------'
    unordered_asteroids = sort_unique(unordered_asteroids)
    print unordered_asteroids

  ordered_asteroids = aster_sort(unordered_asteroids)
  print "---------------"
  print unordered_asteroids
  print ordered_asteroids
  count = 1
  for a in ordered_asteroids:
    vaporized_asteroids.append(a)
    delta_x = a[0]-start_x
    delta_y = a[1]-start_y 
    angle = anti_clockwise(delta_x, delta_y)
    map[a[1]][a[0]] = count
    count += 1
    if count > 9:
      count = 1


count = 1
result = deepcopy(orig_map)
for a in vaporized_asteroids:
  result[a[1]][a[0]] = count
  count += 1
  if count > 9:
    count = 1

print "-------------------"
print_map(result)

count = 1
for a in vaporized_asteroids:
  print " Vap #" + str(count) + " is at " + str(a[0]) + "," + str(a[1])
  if count == 200:
    get_result = (a[0]*100)+a[1]
  count += 1

print "====="
print get_result
