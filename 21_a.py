import sys
from printf import printf

with open("21_input.txt") as f:
    content = f.readlines()

my_prog = []
my_prog.append('NOT A T')
my_prog.append('OR T J')
my_prog.append('NOT B T')
my_prog.append('OR T J')
my_prog.append('NOT C T')
my_prog.append('OR T J')
my_prog.append('AND D J')
my_prog.append('WALK')

input_prog = []
for line in my_prog:
  for c in line:
    input_prog.append(ord(c))
  input_prog.append(10)

#print input_prog

prog = []
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
      #print "Returning : " + str(p)
  if arg == 3:
    if p3_mode == 0:
      p = prog[pc+3]
    else:
      p = prog[pc+3]+base
      #print "Returning : " + str(p)
  return p

pc = 0
while True:
  op = prog[pc]
  #print op

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

  #print op_str
  #print "        " + str(prog[pc+1]) + " " + str(prog[pc+2]) + " " + str(prog[pc+3]) 

  if op == 99:
      #print "EXIT"
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
    input_val = input_prog.pop(0)
    prog[p1] = input_val
    #print "   3: Set [" + str(prog[pc+1]) + "] to " + str(input_val)
    pc = pc +2
    continue

  if op_code == 4:
    p1 = get_arg(1)
    #print "   4: OUTPUT " + str(p1)
    
    if p1 > 255:
      print(p1)
    else:
      printf(chr(p1))
    pc = pc +2
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

