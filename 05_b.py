import sys

with open("05_input_a.txt") as f:
    content = f.readlines()

input_val = 5

prog = []
content = [x.strip() for x in content]
for line in content:
  values = line.split(',')
  for v in values:
    prog.append(int(v))

pc = 0

orig_prog = list(prog)
prog = list(orig_prog)

pc = 0
while True:
  #print prog
  op = prog[pc]

  # Decode 5-digit op-code
  op_str = str(op)
  while len(op_str) < 5:
    op_str = '0' + op_str

  op_both = op_str[3] + op_str[4]
  op_both_int = int(op_both)

  op_code = int(op_str[3]+op_str[4])
  p1_mode = int(op_str[2])
  p2_mode = int(op_str[1])
  p3_mode = int(op_str[0])

  print op_str
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
    continue

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
    continue

  if op_code == 3:
    p1 = prog[pc+1]
    prog[p1] = input_val
    print "   3: Set [" + str(prog[pc+1]) + "] to " + str(input_val)
    pc = pc +2
    continue

  if op_code == 4:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    print "   4: OUTPUT " + str(p1)
    pc = pc +2
    continue

  # JUMP-IF-TRUE
  if op_code == 5:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    if p2_mode == 0:
      p2 = prog[prog[pc+2]]
    else:
      p2 = prog[pc+2]
    if p1 != 0:
      print "   5: JUMP TAKEN"
      pc = p2
    else:
      print "   5: Jump skipped"
      pc = pc + 3
    continue

  # JUMP-IF-FALSE
  if op_code == 6:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    if p2_mode == 0:
      p2 = prog[prog[pc+2]]
    else:
      p2 = prog[pc+2]
    if p1 == 0:
      print "   6: JUMP TAKEN"
      pc = p2
    else:
      print "   6: Jump skipped"
      pc = pc + 3
    continue

  # LESS THAN
  if op_code == 7:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    if p2_mode == 0:
      p2 = prog[prog[pc+2]]
    else:
      p2 = prog[pc+2]
    p3 = prog[pc+3]
    if p1 < p2:
      print "   7: Less Than True"
      prog[p3] = 1
    else:
      print "   7: Less Than False"
      prog[p3] = 0
    pc = pc +4
    continue

  # EQUALS
  if op_code == 8:
    if p1_mode == 0:
      p1 = prog[prog[pc+1]]
    else:
      p1 = prog[pc+1]
    if p2_mode == 0:
      p2 = prog[prog[pc+2]]
    else:
      p2 = prog[pc+2]
    p3 = prog[pc+3]
    if p1 == p2:
      print "   8: Equals True, put 1 in " + str(p3)
      prog[p3] = 1
    else:
      print "   8: Equals False, put 0 in " + str(p3)
      prog[p3] = 0
    pc = pc +4
    continue


