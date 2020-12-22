import sys

with open("02_input_a.txt") as f:
    content = f.readlines()

prog = []
content = [x.strip() for x in content]
for line in content:
  values = line.split(',')
  for v in values:
    prog.append(eval(v))

pc = 0

orig_prog = list(prog)
for noun in range(0, 99):
  for verb in range(0, 99):
    prog = list(orig_prog)

    prog[1] = noun
    prog[2] = verb
    pc = 0
    while True:
      op = prog[pc]
      if op == 99:
        if prog[0] == 19690720:
          result = (noun * 100 ) + verb
          print result
          sys.exit()
        break 
      in1 = prog[pc+1]
      in2 = prog[pc+2]
      out = prog[pc+3]

      if op == 1:
        prog[out] = prog[in1] + prog[in2]

      if op == 2:
        prog[out] = prog[in1] * prog[in2]

      pc = pc +4
