import sys
from printf import printf
import copy
import re
from copy import copy, deepcopy



with open("22_input.txt") as f:
    content = f.readlines()

deck_size = 10007
deck = []

for i in range(0, deck_size):
  deck.append(i)

print deck

for line in content:
  command = line.strip()
  print command
  if command == 'deal into new stack':
    print "REVERSE"
    deck.reverse()

  match = re.search('deal with increment ([0-9]*)', command)
  if match:
    inc = int(match.group(1))
    print "DEAL-INC: " + str(inc)
    new_deck = []
    for i in range(0, deck_size):
      new_deck.append(0)
    deck_index = 0
    for i in range(0, deck_size):
      new_deck[deck_index] = deck[i]
      deck_index += inc
      if deck_index > deck_size:
        deck_index -= deck_size
    deck = deepcopy(new_deck)

  match = re.search('cut ([0123456789]+)', command)
  if match:
    inc = int(match.group(1))
    print "CUT (positive): " + str(inc)
    for i in range(0, inc):
      a = deck.pop(0)
      deck.append(a)

  match = re.search('cut -([0123456789]+)', command)
  if match:
    inc = int(match.group(1))
    print "CUT (negative): " + str(inc)
    new_list = []
    for i in range(0, inc):
      new_list.append(deck.pop())
    new_list.reverse()
    new_list.extend(deck)
    deck = deepcopy(new_list)
      
    
    


      


  print deck
  
pos = deck.index(2019)
print "Part a: " + str(pos)
