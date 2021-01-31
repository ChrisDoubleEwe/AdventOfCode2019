import thread
from copy import copy, deepcopy
import sys
from printf import printf

with open("24_input.txt") as f:
    content = f.readlines()

map_size = 5
maps = []
map = []
empty_map = []
first_map = []
last_map = []

first_map.append(['.', '.', '.', '.', '.', '.', '.'])
for x in range(1, map_size+1):
  row = ['.']
  for y in range(1, map_size+1):
    if x == y == 3:
      row.append('?')
    else:
      row.append('.')
  row.append('.')
  first_map.append(row)
first_map.append(['.', '.', '.', '.', '.', '.', '.'])

last_map.append(['^', '^', '^', '^', '^', '^', '^'])
for x in range(1, map_size+1):
  row = ['<']
  for y in range(1, map_size+1):
    if x == y == 3:
      row.append('.')
    else:
      row.append('.')
  row.append('>')
  last_map.append(row)
last_map.append(['v', 'v', 'v', 'v', 'v', 'v', 'v'])





empty_map.append(['^', '^', '^', '^', '^', '^', '^'])
for x in range(1, map_size+1):
  row = ['<']
  for y in range(1, map_size+1):
    if x == y == 3:
      row.append('?')
    else:
      row.append('.')
  row.append('>')
  empty_map.append(row)
empty_map.append(['v', 'v', 'v', 'v', 'v', 'v', 'v'])


    

map_size = 5
def print_map(z):
  map = maps[z]
  for x in range(1, map_size+1):
    for y in range(1, map_size+1):
      printf(map[x][y])
    print ''

def print_my_map(z):
  for row in z:
    for c in row:
      printf(c)
    print ''

maps.append(first_map)
for i in range(0,99):
  maps.append(empty_map)

map.append(['^', '^', '^', '^', '^', '^', '^'])
l = 0
for line in content:
  l +=1 
  row = ['<']
  r = 0
  for x in line.strip():
    r +=1 
    if l == r == 3:
      row.append('?')
    else:
      row.append(x)
  row.append('>')
  map.append(row)
map.append(['v', 'v', 'v', 'v', 'v', 'v', 'v'])
maps.append(map)

for i in range(0,113):
  maps.append(empty_map)

maps.append(last_map)




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
  global maps
  new_maps = []

  # iterate over maps
  for m in range(0, len(maps)):
    new_map = deepcopy(maps[m])
    map = deepcopy(maps[m])
    #if m > 95 and m < 103:
      #print "One up: "
      #print_my_map(maps[m-1])

      #print "Current map: "
      #print_my_map(map)

      #print "One down: "
      #print_my_map(maps[m+1])




    for x in range(1, map_size+1):
      for y in range(1, map_size+1):
        #print "x=" + str(x) + " ; y=" + str(y) + ' = ' + str(map[y][x])
        adjacent_bugs = 0
        
        # <-- 
        if map[y][x-1] == '#':
          adjacent_bugs+=1
        if map[y][x-1] == '<':
          #print "Checking < up a level ; maps[m-1][3][2] = " + str(maps[m-1][3][2])
          if maps[m-1][3][2] == '#':
            adjacent_bugs+=1
        if map[y][x-1] == '?':
          for j in range(1, map_size+1):
            if maps[m+1][j][5] == '#':
              adjacent_bugs+=1

        # -->
        if map[y][x+1] == '#':
          adjacent_bugs+=1
        if map[y][x+1] == '>':
          #print "Checking > up a level ; maps[m-1][3][4] = " + str(maps[m-1][3][4])
          if maps[m-1][3][4] == '#':
            adjacent_bugs+=1
        if map[y][x+1] == '?': 
          for j in range(1, map_size+1): 
            if maps[m+1][j][1] == '#':
              adjacent_bugs+=1

        # ^--
        if map[y-1][x] == '#':
          adjacent_bugs+=1
        if map[y-1][x] == '^':
          #print "Checking ^ up a level ; maps[m-1][2][3] = " + str(maps[m-1][2][3])
          if maps[m-1][2][3] == '#':
            adjacent_bugs+=1
        if map[y-1][x] == '?':
          for j in range(1, map_size+1):
            if maps[m+1][5][j] == '#':
              adjacent_bugs+=1

        # v--
        if map[y+1][x] == '#':
          adjacent_bugs+=1
        if map[y+1][x] == 'v':
          #print "Checking v up a level ; maps[m-1][4][3] = " + str(maps[m-1][4][3])
          if maps[m-1][4][3] == '#':
            adjacent_bugs+=1
        if map[y+1][x] == '?':
          for j in range(1, map_size+1):
            if maps[m+1][1][j] == '#':
              adjacent_bugs+=1

        #print "ADJACENT BUGS: " + str(adjacent_bugs)
        if map[y][x] == '#' and adjacent_bugs != 1:
          new_map[y][x] = '.'
          #print "BUG DIES"
        elif map[y][x] == '.' and adjacent_bugs >= 1 and adjacent_bugs <= 2:
          new_map[y][x] = '#'
          #print "BUG INFESTS"
    #if m > 95 and m < 105:
      #print ">>>>> " + str(m)
      #print_my_map(new_map)
    new_maps.append(deepcopy(new_map))
  maps = deepcopy(new_maps)


for i in range(0, 200):
  move()
   
count = 0 
for m in range(0, len(maps)-1): 
  for x in range(1, map_size+1):
    for y in range(1, map_size+1):
      #print " -- m: " + str(m) + " ; x: " + str(x) + " ; y: " + str(y)
      if maps[m][y][x] == '#':
        count += 1

print "Part B: " + str(count) 
