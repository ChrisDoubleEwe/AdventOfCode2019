import sys
import itertools


with open("07_a_input_data.txt") as f:
    content = f.readlines()

prog = []
content = [x.strip() for x in content]
for line in content:
  values = line.split(',')
  for v in values:
    prog.append(int(v))
orig_prog = list(prog)


def run_program(inputs):
  pc = 0
  output = 0
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

    #print op_str
    #print "        " + str(prog[pc+1]) + " " + str(prog[pc+2]) + " " + str(prog[pc+3]) 

    if op == 99:
        #print "EXIT"
        return output

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
      #print "   1: Add  (" + str(p1) + " + " + str(p2) + ") to " + str(out)
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
      #print "   2: Mult (" + str(p1) + " * " + str(p2) + ") to " + str(out)
      pc = pc +4
      continue

    if op_code == 3:
      input_val = inputs.pop()
      p1 = prog[pc+1]
      prog[p1] = input_val
      #print "   3: Set [" + str(prog[pc+1]) + "] to " + str(input_val)
      pc = pc +2
      continue

    if op_code == 4:
      if p1_mode == 0:
        p1 = prog[prog[pc+1]]
      else:
        p1 = prog[pc+1]
      #print "   4: OUTPUT " + str(p1)
      output = p1
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
        #print "   5: JUMP TAKEN"
        pc = p2
      else:
        #print "   5: Jump skipped"
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
        #print "   6: JUMP TAKEN"
        pc = p2
      else:
        #print "   6: Jump skipped"
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
        #print "   7: Less Than True"
        prog[p3] = 1
      else:
        #print "   7: Less Than False"
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
        #print "   8: Equals True, put 1 in " + str(p3)
        prog[p3] = 1
      else:
        #print "   8: Equals False, put 0 in " + str(p3)
        prog[p3] = 0
      pc = pc +4
      continue

all_phases = []
phases = [0, 1, 2, 3, 4]
for set in itertools.permutations(phases, len(phases)):
  all_phases.append(set)

max_set = []
max_o = 0

for set in all_phases:
  p0 = set[0]
  p1 = set[1]
  p2 = set[2]
  p3 = set[3]
  p4 = set[4]

  inputs = [0, p0]
  o1 =run_program(inputs)
  inputs = [o1, p1]
  o2 =run_program(inputs)
  inputs = [o2, p2]
  o3 =run_program(inputs)
  inputs = [o3, p3]
  o4 =run_program(inputs)
  inputs = [o4, p4]
  o5 =run_program(inputs)
  if o5 > max_o:
    max_o = o5
    max_set = set

print max_set
print max_o








