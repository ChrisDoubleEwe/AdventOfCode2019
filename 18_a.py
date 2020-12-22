import sys
from copy import copy, deepcopy

with open("18_test6.txt") as f:
    content = f.readlines()

all_full_paths = []
shortest_path = 999999999
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


def get_path_length(all_p):
  this_steps = 0
  for x in all_p:
    this_steps = this_steps + x[0]
  return this_steps

def print_map(m):
  for row in m:
    c_str = ''
    for c in row:
      c_str += str(c)
    print c_str

def find_keys(x, y, m, p):
  global shortest_path
  global map_y
  global map_x
  global all_full_paths
  keys = []
  map = deepcopy(m)
  map[y][x] = 0
  step = -1
  step_taken = 1
  while step_taken == 1:
    step += 1
    step_taken = 0
    #print_map(map)
    for y in range(0, map_y):
      for x in range(0, map_x):
        if map[y][x]==step:
          if map[y-1][x] == '.':
            map[y-1][x] = step+1
            step_taken = 1
          if map[y+1][x] == '.':
            map[y+1][x] = step+1
            step_taken = 1
          if map[y][x-1] == '.':
            map[y][x-1] = step+1
            step_taken = 1
          if map[y][x+1] == '.':
            map[y][x+1] = step+1
            step_taken = 1
          if str(map[y-1][x]).islower():
            key = [step+1, y-1, x, map[y-1][x]]
            keys.append(key)
            step_taken = 1
          if str(map[y+1][x]).islower():
            key = [step+1, y+1, x, map[y+1][x]]
            keys.append(key)
            step_taken = 1
          if str(map[y][x-1]).islower():
            key = [step+1, y, x-1, map[y][x-1]]
            keys.append(key)
            step_taken = 1
          if str(map[y][x+1]).islower():
            key = [step+1, y, x+1, map[y][x+1]]
            keys.append(key)
            step_taken = 1
  #print "No more steps left"
  keys_left = 0
  for y in range(0, map_y):
    for x in range(0, map_x):
      if str(map[y][x]).islower():
        keys_left = 1
  if keys_left == 0:
    #print "ADDING PATH:"
    print p
    if get_path_length(p) < shortest_path:
      shortest_path = get_path_length(p)
      print "New shortest path! "
      print get_path_length(p)
    all_full_paths.append(deepcopy(p))
  return keys

def update_pos(me_y, me_x, m):
  global map_y
  global map_x
  for y in range(0, map_y):
    for x in range(0, map_x):
      if m[y][x] == '@':
        m[y][x] = '.'
      if y == me_y and x == me_x:
        m[y][x] = '@' 
  return m

def unlock(k, m):
  global map_y
  global map_x
  for y in range(0, map_y):
    for x in range(0, map_x):
      if m[y][x] == k.upper():
        m[y][x] = '.'
  return m

def take_step(p, m):
  global map_y
  global map_x
  global shortest_path
  
  if get_path_length(p) > shortest_path:
    return

  me_x = -1
  me_y = -1
  for y in range(0, map_y):
    for x in range(0, map_x):
      if m[y][x] == '@':
        me_x = x
        me_y = y

  #print "Starting point: " + str(me_x) + " , " + str(me_y)
  #print p
  #print_map(m)
  key_list = find_keys(me_x, me_y, m, p)
  if len(key_list) == 0:
    return
  #print "KEY LIST:"
  #print key_list
  for key in key_list:
    this_m = deepcopy(m)
    this_m = unlock(key[3], this_m)
    this_m = update_pos(key[1], key[2], this_m)
    #print key
    #print p
    this_step = []
    this_step.append(key[0])
    this_step.append(key[3])

    this_path = deepcopy(p)
    this_path.append(deepcopy(this_step))
    #print "Append path:"
    #print this_path
    #print "Calling TAKE_STEP:"
    #print this_path
    #print_map(this_m)
    take_step(this_path, this_m)

path_so_far = []
take_step(path_so_far, map)
print all_full_paths

shortest_steps = 99999999
shoprtest_path = []
max_steps = 0

for p in all_full_paths:
    print
    print p
    this_steps = 0
    for x in p:
      this_steps = this_steps + x[0]
    if this_steps < shortest_steps:
      shortest_steps = this_steps
      shortest_path = p

print "SHORTEST"
print shortest_steps
print shortest_path

