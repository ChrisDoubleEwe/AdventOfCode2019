from copy import copy, deepcopy
from random import randint
from os import system, name 
import sys
import readchar
import time

input_str = '59719811742386712072322509550573967421647565332667367184388997335292349852954113343804787102604664096288440135472284308373326245877593956199225516071210882728614292871131765110416999817460140955856338830118060988497097324334962543389288979535054141495171461720836525090700092901849537843081841755954360811618153200442803197286399570023355821961989595705705045742262477597293974158696594795118783767300148414702347570064139665680516053143032825288231685962359393267461932384683218413483205671636464298057303588424278653449749781937014234119757220011471950196190313903906218080178644004164122665292870495547666700781057929319060171363468213087408071790'
base_pattern = [0, 1, 0, -1]

input = []
for c in input_str:
  input.append(int(c))

def calc_value(a, b):
  res = a * b
  #res_str = str(res)
  #last_char = res_str[-1]
  #return int(last_char)
  return res

def last_digit(a):
  res_str = str(a)
  last_char = res_str[-1]
  return int(last_char)

def calc_pattern(length, idx):
  global base_pattern
  #print "Calculating pattern for " + str(idx)
  z = 0
  this_pattern = []
  while len(this_pattern) <= length:
    for loop in range(0, idx+1):
      #print "   loop = " + str(loop) + " ; appending base pattern digit " + str(z)
      this_pattern.append(base_pattern[z])
      if len(this_pattern) > length:
        break
    z += 1
    if z == len(base_pattern):
      z = 0
  this_pattern.pop(0)
  #print "  pattern for " + str(idx) + " = " + str(this_pattern)
  return this_pattern
  
def do_phase(input):
  output = []
  for i in range(0, len(input)):
    mult = calc_pattern(len(input), i)
    this_val = 0
    for x in range(0, len(input)):
      this_val += calc_value(input[x], mult[x])
    output.append(last_digit(this_val))
  return output

output = deepcopy(input)
phases = 100
for s in range(1, phases+1):
  print "PHASE " + str(s)
  output = do_phase(output)
  o_str = ''
  for c in output:
    o_str += str(c)
  print "      " + o_str
