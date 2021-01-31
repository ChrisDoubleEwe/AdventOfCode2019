import thread
from copy import copy, deepcopy
import sys
from printf import printf

with open("24_input.txt") as f:
    content = f.readlines()

map_size = 5
def print_map():
  for x in range(1, map_size+1):
    for y in range(1, map_size+1):
      printf(map[x][y])
    print ''
map = []

map.append('.......')
for line in content:
  row = ['.']
  for x in line.strip():
    row.append(x)
  row.append('.')
  map.append(row)
map.append('.......')

def bio():
  mult = 1
  sum = 0
  for x in range(1, map_size+1):
    for y in range(1, map_size+1):
      if map[x][y] == '#':
        sum += mult
      mult += mult 
  return sum


def move():
  global map
  new_map = deepcopy(map)

  for x in range(1, map_size+1):
    for y in range(1, map_size+1):
      #print "x=" + str(x) + " ; y=" + str(y)
      adjacent_bugs = 0
      if map[x-1][y] == '#':
        adjacent_bugs+=1
      if map[x+1][y] == '#':
        adjacent_bugs+=1
      if map[x][y-1] == '#':
        adjacent_bugs+=1
      if map[x][y+1] == '#':
        adjacent_bugs+=1
      #print "ADJACENT BUGS: " + str(adjacent_bugs)
      if map[x][y] == '#' and adjacent_bugs != 1:
        new_map[x][y] = '.'
        #print "BUG DIES"
      elif map[x][y] == '.' and adjacent_bugs >= 1 and adjacent_bugs <= 2:
        new_map[x][y] = '#'
        #print "BUG INFESTS"
  map = deepcopy(new_map)


seen = []
i = 0
while True:
  i += 1
  print '\n-- Iteration ' + str(i)
  count = 0
  for x in range(1, map_size+1):
    for y in range(1, map_size+1):
      if map[x][y] == '#':
        count += 1

  #print_map()
  biox = bio()
  print biox
  if biox in seen:
    print "SEEN BEFORE"
    exit()
  seen.append(biox)
  move()



     
