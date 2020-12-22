from copy import copy, deepcopy
from random import randint
from os import system, name 
import sys
import readchar
import time

with open("15_map.txt") as f:
    content = f.readlines()

screen = []
screen_x = -1
screen_y = -1

content = [x.strip() for x in content]
for line in content:
  row = []
  for c in line:
    if screen_y < 0:
      screen_x += 1
    if c == '#':
      row.append(3)
    if c == '.':
      row.append(1)
    if c == '0':
      row.append(2)
  screen.append(deepcopy(row))
  screen_y += 1

def print_screen():
  global screen
  time.sleep(0.01)
  system('clear')
  for row in screen:
    row_str = ''
    for c in row:
      if c == 0:
        row_str = row_str + ' '
      if c == 1:
        row_str = row_str + '.'
      if c == 2:
        row_str = row_str + '0'
      if c == 3:
        row_str = row_str + '#'

    print row_str 

def not_full():
  dots = 0
  for row in screen:
    for c in row:
      if c == 1:
        dots = dots + 1
  if dots == 0:
    return False
  return True

def fill_with_oxygen():
  global screen
  global screen_x
  global screen_y
  next_screen = deepcopy(screen)
  for y in range(0, screen_y):
    for x in range(0, screen_x):
      if screen[y][x] == 2:
        if screen[y][x-1] == 1:
          next_screen[y][x-1] = 2
        if screen[y][x+1] == 1:
          next_screen[y][x+1] = 2
        if screen[y-1][x] == 1:
          next_screen[y-1][x] = 2
        if screen[y+1][x] == 1:
          next_screen[y+1][x] = 2
  screen = deepcopy(next_screen)
  print_screen()

 
print_screen()

steps = 0
while not_full():
  fill_with_oxygen()
  steps += 1

print "Finished after " + str(steps) + " steps"
 
