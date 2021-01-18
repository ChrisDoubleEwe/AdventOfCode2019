from copy import copy, deepcopy
from os import system, name 
import sys
import readchar
import time
import re

map_quantity = {}
map_ingrediant = {}

with open("14_input.txt") as f:
    content = f.readlines()

equations = []

for c in content:
  match = re.search('(.*) => (.*)', c)
  if match:
    eq_from = match.group(1)
    eq_to = match.group(2)
    eq_to_pair = eq_to.split()
    eq_from_pair = eq_from.split()
    eq_from_pairs = []
    dummy_pair = []
    dummy_pair.append('')
    dummy_pair.append('')
    eq_from_pairs.append(dummy_pair)
    for x in eq_from.split(', '):
      eq_from_pairs.append(x.split())

    eq = []

    eq.append(eq_from_pairs)
    eq.append(eq_to_pair)

    equations.append(eq)


#for x in equations:
#  if x[1][1] == 'FUEL':
#    print x
#    print 'CONSUME ' + str(x[1]) + ' to produce ' + str(x[0])
#    #new_list = consume(x[0])

depth_tree = {}
depth_tree['ORE'] = 0

for k in range(0, 100):
 for x in equations:
  #print "-- Doing " + str(x)
  if x in depth_tree.keys():
    continue
  max_depth = -1
  found_all_components = 1
  for z in x[0]:
    if z[0] == z[1] == '':
      continue
    #print "Looking for " + str(z[1])
    if z[1] in depth_tree.keys():
      #print "  found " + z[1]
      if (depth_tree[z[1]] + 1) > max_depth:
        max_depth = depth_tree[z[1]] + 1 
        #print "Setting max_depth to " + str(max_depth)
    else:
      found_all_components = -1
  if ((x[1][1] not in depth_tree.keys()) and (found_all_components == 1)):
    #print "Adding " + x[1][1] + " to depth tree with max_depth " + str(max_depth)
    depth_tree[x[1][1]] = max_depth


maximum_depth = -1
for x in depth_tree.keys():
  if depth_tree[x] > maximum_depth:
    maximum_depth = depth_tree[x]

print "--------------------"
print depth_tree
print "--------------------"

this_depth = maximum_depth + 1

#while this_depth > 0:
#  this_depth += -1
#  print this_depth 
#  for x in depth_tree.keys():
#    if depth_tree[x] == this_depth:
#      print "CONSUME: " + str(x)

my_list = []
my_pair = []
my_pair.append(1)
my_pair.append('FUEL')
my_list.append(my_pair)

def consume(x):
  if x[1] == x[0] == '':
    return x
  return_list = []
  thing = x[1]
  quantity = int(x[0])
  #print "Need to make " + str(quantity) + "  " + thing
  for z in equations:
    if z[1][1] == thing:
      for p in z[0]:
        return_list.append(p)
      #print "Final list: " + str(return_list)
      made_quantity = int(z[1][0])
      #print "  MADE: " + str(made_quantity)
      #print return_list
      while made_quantity < quantity:
        for p in z[0]:
          return_list.append(p)
        made_quantity += int(z[1][0])
        #print "  MADE: " + str(made_quantity)
        #print return_list
        #remaining_quantity = quantity - made_quantity
        #new_pair = []
        #new_pair.append(remaining_quantity)
        #new_pair.append(thing)
        #return_list.append(new_pair)
  return return_list

def combine(l, x):
  running_total = 0
  new_list = []
  for i in l:
    if i[1] == x:
      running_total += int(i[0])
    else:
      new_list.append(i)
  if running_total > 0:
    new_pair = []
    new_pair.append(running_total)
    new_pair.append(x)
    new_list.append(new_pair)
  return new_list

#for i in range(0,2):
#  print "----- " + str(i)
#  print my_list
#  new_list = []
#  for x in my_list:
#    new_list.extend(consume(x))
#  my_list = deepcopy(new_list)


for j in range(0, 10):
 print "')))))))" + str(j)
 this_depth = maximum_depth + 1

 while this_depth > 1:
  this_depth += -1
  #print "+++++ " + str(this_depth)
  for x in depth_tree.keys():
    #print my_list
    if depth_tree[x] == this_depth:
      #print "Doing: " + str(x)

      # Just do it 1000 times to cheat...
      found = -1
      for t in range(0, 100):
        combine_list = combine(my_list, x)
        my_list = deepcopy(combine_list)
        #print "After combining: " + str(my_list)
        new_list = []
        for y in my_list:
          if y[1] == x:
            new_list.extend(consume(y))
            found = 1
          else:
            new_list.append(y)
        my_list = deepcopy(new_list)
        if found == -1:
          break
  
print "++++"
print new_list


count_ore = 0
for x in new_list:
  if x[1] == 'ORE':
    count_ore += int(x[0])

print "TOTAL ORE: " + str(count_ore)


