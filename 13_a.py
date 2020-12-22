from copy import copy, deepcopy
from os import system, name 
import sys
import readchar
import time

sleeping = 0
with open("13_input_a.txt") as f:
    content = f.readlines()

input_val = 2
high_score = 0

prog = []
content = [x.strip() for x in content]
for line in content:
  values = line.split(',')
  for v in values:
    prog.append(long(v))

for i in range(0, 1000):
  prog.append(0)

prog[0]=2

pc = 0
base = 0

orig_prog = list(prog)
prog = list(orig_prog)

def get_x_o():
  for row in screen:
    x_o = 0
    for c in row:
      if c == 4:
        return x_o
      x_o += 1

def get_x_bat():
  for row in screen:
    x_o = 0
    for c in row:
      if c == 3:
        return x_o
      x_o += 1

def count_blocks():
  global screen
  count = 0
  for row in screen:
    for c in row:
      if c == 2:
        count += 1
  print count

def print_screen():
  global screen
  global sleeping
  if sleeping == 1:
    time.sleep(0.05)
  system('clear')
  for row in screen:
    row_str = ''
    for c in row:
      if c == 0:
        row_str = row_str + ' '
      if c == 1:
        row_str = row_str + '|'
      if c == 2:
        row_str = row_str + '#'
      if c == 3:
        row_str = row_str + '='
      if c == 4:
        row_str = row_str + 'o'

    print row_str 
  print " "
  print " "
  print "***********************************************************"
  print "  HIGH SCORE: " + str(high_score)
  print "***********************************************************"

    
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
screen_size_x = 45
screen_size_y = 23

row = []
screen = []
for x in range(0, screen_size_x):
  row.append(0)
for y in range(0, screen_size_y):
  screen.append(deepcopy(row))
  



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
      print_screen()
      count_blocks()
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
    #input_key = readchar.readchar()
    #input_val = 0
    #print input_key
    #if input_key == 'z':
    #  input_val = -1
    #if input_key == 'x':
    #  input_val = 1

    input_val = 0
    if get_x_o() < get_x_bat():
      input_val = -1
    if get_x_o() > get_x_bat():
      input_val = 1
 

    prog[p1] = input_val
    #print "   3: Set [" + str(prog[pc+1]) + "] to " + str(input_val)
    sleeping = 1
    pc = pc +2
    print_screen()
    continue

  if op_code == 4:
    p1 = get_arg(1)
    #print "   4: OUTPUT " + str(p1)
    pc = pc +2
    output.append(p1)
    if len(output) > 2:
      #print "       Output To Screen: x=" + str(output[0]) + " ; y= " + str(output[1]) + " ; tile= " + str(output[2])
      if output[0]==-1 and output[1]==0:
        high_score = output[2]
      else:
        screen[output[1]][output[0]] = output[2]
      output = []
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

