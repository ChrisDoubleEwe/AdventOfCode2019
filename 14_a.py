from copy import copy, deepcopy
from os import system, name 
import sys
import readchar
import time

map_quantity = {}
map_ingrediant = {}

with open("14_input_test1.txt") as f:
    content = f.readlines()

def convert(inp, i):
   print "CONVERT"
   ing = inp[1]
   qua = int(inp[0])
   print inp
   replacement = deepcopy(map_ingrediant[ing])
   replacement_qua = int(map_quantity[ing])
   replacement[0] = replacement[0] * qua

   print "Converting " + str(qua) + " " + str(ing) + " to " + str(replacement)
   qua = qua - replacement_qua
   if qua < 0:
     inp[0] = 0

   print "  Removing " + str(inp) + " from " + str(i) + " ..."
   i.remove(inp)
   print "   old: " + str(i)
   for pair in replacement:
     i.append(pair)
   print "   new: " + str(i)

for line in content:
  inp = line.split("=")[0]
  out = line.split(">")[1].strip()
  inputs = inp.split(",")
  all_inputs = []
  for y in inputs:
    x = y.strip()
    quantity = x.strip().split(" ")[0]
    ingrediant = x.strip().split(" ")[1]
    pair = []
    pair.append(int(quantity))
    pair.append(ingrediant)
    all_inputs.append(deepcopy(pair))
   
  out_thing = out.split(" ")[1]
  out_quantity = out.split(" ")[0]
  
  map_quantity[out_thing] = out_quantity
  map_ingrediant[out_thing] = all_inputs

orig_map_quantity = map_quantity
orig_map_ingrediant = map_ingrediant

for i in map_quantity:
  if map_quantity[i] > 1:
    denom = int(map_quantity[i])
    map_quantity[i] = 1
  else:
    denom = 1

  for x in map_ingrediant[i]:
    x[0] = int(x[0]) / denom

for x in map_quantity:
  print x + " " + str(map_quantity[x])
for x in map_ingrediant:
  print map_ingrediant[x]

i = deepcopy(map_ingrediant["FUEL"])
non_ore = 1
while non_ore != 0:
  spotted = 0
  print "=========================="
  print "Current list: " + str(i)
  for inp in i:
    if inp[1] == "ORE":
      continue 
    else:
      spotted = 1
      convert(inp, i)
  non_ore = spotted
