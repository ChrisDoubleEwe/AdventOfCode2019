import sys

with open("05_input_a.txt") as f:
    content = f.readlines()

input_val = 1

prog = []
content = [x.strip() for x in content]
for line in content:
  values = line.split(',')
  for v in values:
    prog.append(eval(v))

pc = 0

orig_prog = list(prog)
prog = list(orig_prog)

pc = 0
while True:
  op = prog[pc]

  # Decode 5-digit op-code
  op_str = str(op)
  while len(op_str) < 5:
    op_str = '0' + op_str
  op_code = eval(op_str[3]+op_str[4])
  p1_mode = eval(op_str[2])
  p2_mode = eval(op_str[1])
  p3_mode = eval(op_str[0])

  #print op_str
  #print "        " + str(prog[pc+1]) + " " + str(prog[pc+2]) + " " + str(prog[pc+3]) 

  if op == 99:
      print "EXIT"
      sys.exit()

  if op_code == 1:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    if p2_mode == 0:
      p2 = prog[prog[pc+2]]
    else:
      p2 = prog[pc+2]
    out = prog[pc+3]
    prog[out] = p1 + p2
    print "   1: Add  (" + str(p1) + " + " + str(p2) + ") to " + str(out)
    pc = pc +4

  if op_code == 2:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    if p2_mode == 0:
      p2 = prog[prog[pc+2]]
    else:
      p2 = prog[pc+2]
    out = prog[pc+3]
    prog[out] = p1 * p2
    print "   2: Mult (" + str(p1) + " * " + str(p2) + ") to " + str(out)
    pc = pc +4


  if op_code == 3:
    p1 = prog[pc+1]
    prog[p1] = input_val
    print "   3: Set [" + str(prog[pc+1]) + "] to " + str(input_val)
    pc = pc +2

  if op_code == 4:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    print "   4: OUTPUT " + str(p1)
    pc = pc +2


