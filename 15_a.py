from copy import copy, deepcopy
from random import randint
from os import system, name 
import sys
import readchar
import time

with open("15_a_input.txt") as f:
    content = f.readlines()

input_val = 1
old_input_val = input_val

path = []
prog = []
oxy_y = -99
oxy_x = -99
content = [x.strip() for x in content]
for line in content:
  values = line.split(',')
  for v in values:
    prog.append(long(v))

for i in range(0, 1000):
  prog.append(0)

pc = 0
base = 0

orig_prog = list(prog)
prog = list(orig_prog)

def check_empty(y, x):
  global screen
  if screen[y][x] == 1:
    print "CLASH!!!!!!"
    sys.exit() 



def optimize(path):
  modified = 1
  while modified == 1:
    print "Looping..."
    for i in range(0, len(path)-1):
      modified = 0
      if path[i] == 1 and path[i+1] == 2:
        modified = 1
        print "N + S : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break
      if path[i] == 2 and path[i+1] == 1:
        modified = 1
        print "S + N : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break
      if path[i] == 3 and path[i+1] == 4:
        modified = 1
        print "W + E : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break
      if path[i] == 4 and path[i+1] == 3:
        modified = 1
        print "E + W : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break

  return path

def print_screen():
  global screen
  time.sleep(0.0005)
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
      if c == 5:
        row_str = row_str + '*'

    print row_str 

    
def get_arg(arg):
  global pc
  global prog
  global base
  global p1_mode
  global p2_mode
  global p3_mode

  #print "GET ARG " + str(arg) + " mode = " + str(p1_mode) + " base=" + str(base)
  if arg == 1:
    if p1_mode == 0:
      p = prog[prog[pc+1]]
    elif p1_mode == 2:
      p = prog[prog[pc+1]+base] 
    else:
      p = prog[pc+1]
  if arg == 2:
    if p2_mode == 0:
      p = prog[prog[pc+2]]
    elif p2_mode == 2:
      p = prog[prog[pc+2]+base]
    else:
      p = prog[pc+2]
  return p

def get_loc(arg):
  global pc
  global prog
  global base
  global p1_mode
  global p2_mode
  global p3_mode

  if arg == 1:
    if p1_mode == 0:
      p = prog[pc+1]
    else:
      p = prog[pc+1]+base
  if arg == 3:
    if p3_mode == 0:
      p = prog[pc+3]
    else:
      p = prog[pc+3]+base
  return p

pc = 0
output = []
screen_size_x = 50
screen_size_y = 50
me_x = screen_size_x / 2
me_y = screen_size_y / 2

row = []
screen = []
for x in range(0, screen_size_x):
  row.append(0)
for y in range(0, screen_size_y):
  screen.append(deepcopy(row))
  



print "Running program..."
while True:
  op = prog[pc]

  # Decode 5-digit op-code
  op_str = str(op)
  while len(op_str) < 5:
    op_str = '0' + op_str

  op_both = op_str[3] + op_str[4]
  op_both_int = long(op_both)

  op_code = long(op_str[3]+op_str[4])
  p1_mode = long(op_str[2])
  p2_mode = long(op_str[1])
  p3_mode = long(op_str[0])

  #print "        " + str(prog[pc+1]) + " " + str(prog[pc+2]) + " " + str(prog[pc+3]) 

  if op == 99:
      print "EXIT"
      sys.exit()

  if op_code == 1:
    p1 = get_arg(1)
    p2 = get_arg(2)
    out = get_loc(3)
    prog[out] = p1 + p2
    #print "   1: Add  (" + str(p1) + " + " + str(p2) + ") to " + str(out)
    pc = pc +4 
    continue

  if op_code == 2:
    p1 = get_arg(1)
    p2 = get_arg(2)
    out = get_loc(3)
    prog[out] = p1 * p2
    #print "   2: Mult (" + str(p1) + " * " + str(p2) + ") to " + str(out)
    pc = pc +4
    continue

  if op_code == 3:
    p1 = get_loc(1)

    # N: try west, then north, then east, then south
    if old_input_val == 1:
      if screen[me_y][me_x-1] != 3:
        input_val = 3
      elif screen[me_y-1][me_x] != 3:
        input_val = 1
      elif screen[me_y][me_x+1] != 3:
        input_val = 4
      elif screen[me_y+1][me_x] != 3:
        input_val = 2
    # S: try east, then south, then west, then north
    if old_input_val == 2:
      if screen[me_y][me_x+1] != 3:
        input_val = 4
      elif screen[me_y+1][me_x] != 3:
        input_val = 2
      elif screen[me_y][me_x-1] != 3:
        input_val = 3
      elif screen[me_y-1][me_x] != 3:
        input_val = 1
    # E: try north, east, south, west
    if old_input_val == 4:
      if screen[me_y-1][me_x] != 3:
        input_val = 1
      elif screen[me_y][me_x+1] != 3:
        input_val = 4
      elif screen[me_y+1][me_x] != 3:
        input_val = 2
      elif screen[me_y][me_x-1] != 3:
        input_val = 3
    # W: try south, west, north, east
    if old_input_val == 3:
      if screen[me_y+1][me_x] != 3:
        input_val = 2
      elif screen[me_y][me_x-1] != 3:
        input_val = 3
      elif screen[me_y-1][me_x] != 3:
        input_val = 1
      elif screen[me_y][me_x+1] != 3:
        input_val = 4

    print "OLD INPUT VAL = " + str(old_input_val)
    print "NEW INPUT VAL = " + str(input_val)



    prog[p1] = input_val
    print "   3: INPUT -  " + str(input_val)
    pc = pc +2
    continue

  if op_code == 4:
    p1 = get_arg(1)
    print "   4: OUTPUT - " + str(p1)
    screen[me_y][me_x] = 1
    if oxy_y > -99:
      screen[oxy_y][oxy_x] = 2
    if p1 == 0:
      if input_val == 1:
        check_empty(me_y-1, me_x)
        screen[me_y-1][me_x] = 3
      if input_val == 2:
        check_empty(me_y+1, me_x)
        screen[me_y+1][me_x] = 3
      if input_val == 3:
        check_empty(me_y, me_x-1)
        screen[me_y][me_x-1] = 3
      if input_val == 4:
        check_empty(me_y, me_x+1)
        screen[me_y][me_x+1] = 3
    if p1 == 1 or p1 == 2:
      path.append(input_val)
      old_input_val = input_val
      if input_val == 1:
        screen[me_y-1][me_x] = p1
        me_y += -1
      if input_val == 2:
        screen[me_y+1][me_x] = p1
        me_y += 1
      if input_val == 3:
        screen[me_y][me_x-1] = p1
        me_x += -1
      if input_val == 4:
        screen[me_y][me_x+1] = p1
        me_x += 1
    if p1 == 2:
      print "FOUND OXYGEN!!!"
      opt=optimize(path)
      print opt
      print "PATH LENGTH"
      print len(opt)
      
      #sys.exit()
      screen[me_y][me_x] = 2
      oxy_y = me_y
      oxy_x = me_x
    screen[me_y][me_x] = 5

    pc = pc +2
    print_screen()
    continue

  # JUMP-IF-TRUE
  if op_code == 5:
    p1 = get_arg(1)
    p2 = get_arg(2)
    if p1 != 0:
      #print "   5: JUMP TAKEN"
      pc = p2
    else:
      #print "   5: Jump skipped"
      pc = pc + 3
    continue

  # JUMP-IF-FALSE
  if op_code == 6:
    p1 = get_arg(1)
    p2 = get_arg(2)
    if p1 == 0:
      #print "   6: JUMP TAKEN"
      pc = p2
    else:
      #print "   6: Jump skipped"
      pc = pc + 3
    continue

  # LESS THAN
  if op_code == 7:
    p1 = get_arg(1)
    p2 = get_arg(2)
    p3 = get_loc(3)
    if p1 < p2:
      #print "   7: Less Than True"
      prog[p3] = 1
    else:
      #print "   7: Less Than False"
      prog[p3] = 0
    pc = pc +4
    continue

  # EQUALS
  if op_code == 8:
    p1 = get_arg(1)
    p2 = get_arg(2)
    p3 = get_loc(3)
    if p1 == p2:
      #print "   8: Equals True, put 1 in " + str(p3)
      prog[p3] = 1
    else:
      #print "   8: Equals False, put 0 in " + str(p3)
      prog[p3] = 0
    pc = pc +4
    continue

  # ADJUST RELATIVE BASE OFFSET
  if op_code == 9:
    p1 = get_arg(1)
    base = base + p1
    pc = pc +2
    continue

