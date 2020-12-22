import sys
import itertools


with open("07_a_input_data.txt") as f:
    content = f.readlines()

orig_prog = []
last_output = 0
my_prog = []
content = [x.strip() for x in content]
for line in content:
  values = line.split(',')
  for v in values:
    orig_prog.append(int(v))
my_prog.append([])
my_prog.append([])
my_prog.append([])
my_prog.append([])
my_prog.append([])

my_prog[0] = list(orig_prog)
my_prog[1] = list(orig_prog)
my_prog[2] = list(orig_prog)
my_prog[3] = list(orig_prog)
my_prog[4] = list(orig_prog)

master_pc = [0, 0, 0, 0, 0]
output_bus = [[],[],[],[],[]]


def run_program(amp, inputs):
  global master_pc
  global my_prog
  global output_bus
  global last_output
  pc = master_pc[amp]
  print "Running amplifier " + str(amp) + " from PC=" + str(pc)
  output = 0
  prog = my_prog[amp]

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
        print "EXIT"
        master_pc[amp ] = pc
        return 0

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
      print "   amp=" + str(amp) + " pc=" + str(pc) + "   1: Add  (" + str(p1) + " + " + str(p2) + ") to " + str(out)
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
      print "   amp=" + str(amp) + " pc=" + str(pc) + "   2: Mult (" + str(p1) + " * " + str(p2) + ") to " + str(out)
      pc = pc +4
      continue

    if op_code == 3:
      print "   amp=" + str(amp) + " pc=" + str(pc) + "GET INPUT"
      for o in output_bus:
        print o
      bus = 4
      if amp > 0:
        bus = amp-1
      if len(output_bus[bus]) == 0:
        master_pc[amp ] = pc
        return 1
      input_val = output_bus[bus].pop()
      p1 = prog[pc+1]
      prog[p1] = input_val
      print "   amp=" + str(amp) + " pc=" + str(pc) + "   3: Set [" + str(prog[pc+1]) + "] to " + str(input_val)
      pc = pc +2
      master_pc[amp ] = pc
      continue

    if op_code == 4:
      if p1_mode == 0:
        p1 = prog[prog[pc+1]]
      else:
        p1 = prog[pc+1]
      print "   amp=" + str(amp) + " pc=" + str(pc) + "   4: OUTPUT " + str(p1)
      output = p1
      pc = pc +2
      master_pc[amp ] = pc
      output_bus[amp].append(p1)
      last_output = p1
      for o in output_bus:
        print o
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
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   5: JUMP TAKEN, jumping to " + str(p2)
        pc = p2
      else:
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   5: Jump skipped"
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
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   6: JUMP TAKEN, jumping to " + str(p2)
        pc = p2
      else:
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   6: Jump skipped"
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
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   7: Less Than True"
        prog[p3] = 1
      else:
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   7: Less Than False"
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
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   8: Equals True, put 1 in " + str(p3)
        prog[p3] = 1
      else:
        print "   amp=" + str(amp) + " pc=" + str(pc) + "   8: Equals False, put 0 in " + str(p3)
        prog[p3] = 0
      pc = pc +4
      continue

all_phases = []
phases = [5, 6, 7, 8, 9]
for set in itertools.permutations(phases, len(phases)):
  all_phases.append(set)

#all_phases = [[9,8,7,6,5]]
max_set = []
max_o = 0

for set in all_phases:
  my_prog[0] = list(orig_prog)
  my_prog[1] = list(orig_prog)
  my_prog[2] = list(orig_prog)
  my_prog[3] = list(orig_prog)
  my_prog[4] = list(orig_prog)

  master_pc = [0, 0, 0, 0, 0]
  output_bus = [[],[],[],[],[]]

  p0 = set[0]
  p1 = set[1]
  p2 = set[2]
  p3 = set[3]
  p4 = set[4]

  inputs = 0
  output_bus[4] = [0, p0]
  state = run_program(0, inputs)
  output_bus[0].append(p1)
  state = run_program(1, inputs)
  output_bus[1].append(p2)
  state = run_program(2, inputs)
  output_bus[2].append(p3)
  state = run_program(3, inputs)
  output_bus[3].append(p4)
  state = run_program(4, inputs)
  while True: 
    state = 0
    state += run_program(0, inputs)
    state += run_program(1, inputs)
    state += run_program(2, inputs)
    state += run_program(3, inputs)
    state += run_program(4, inputs)
    if state == 0:
      print "======"
      print last_output
      if last_output > max_o:
        max_o = last_output
        max_set = set
      break


print "-------------"
print str(max_o)
print max_set




