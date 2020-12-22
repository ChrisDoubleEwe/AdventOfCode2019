from copy import copy, deepcopy
from random import randint
from os import system, name 
import sys
import readchar
import time

input_str = '59719811742386712072322509550573967421647565332667367184388997335292349852954113343804787102604664096288440135472284308373326245877593956199225516071210882728614292871131765110416999817460140955856338830118060988497097324334962543389288979535054141495171461720836525090700092901849537843081841755954360811618153200442803197286399570023355821961989595705705045742262477597293974158696594795118783767300148414702347570064139665680516053143032825288231685962359393267461932384683218413483205671636464298057303588424278653449749781937014234119757220011471950196190313903906218080178644004164122665292870495547666700781057929319060171363468213087408071790'
#input_str = '03036732577212944063491565474664'
#input_str = '02935109699940807407585447034323'
#input_str = '03081770884921959731165446850517'
input_str = input_str * 10000
start_str = input_str[0:7]
start = int(start_str)
end = len(input_str)

print "START: " + start_str
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
  x = len(input)
  outp = []
  step = 0
  input.reverse()
  last = 0
  for i in input:
    step += 1
    #print " " + str(step) + " / " + str(x)
    res = last_digit(i + last)
    outp.append(res)
    last = res
  outp.reverse()
  return outp

print "LENGTH: " + str(len(input))
print "START: " + str(start)
output = deepcopy(input[start:])
phases = 100
for s in range(1, phases+1):
  print "PHASE " + str(s)
  output = do_phase(output)

o_str = ''
for c in output[0:8]:
  o_str += str(c)
print "      " + o_str

