import sys
from copy import copy, deepcopy

with open("12_input_a.txt") as f:
    content = f.readlines()

moons = []
vel = []
for r in content:
  triple = r.split('=')
  triple.pop(0)
  xyz = []
  for t in triple:
    a = t.split(',')[0]
    b = a.split('>')[0]
    xyz.append(int(b))
  moons.append(xyz)
  vel.append([0, 0, 0])


steps = 1000
step = 0

def gravity():
  global moons
  global vel

  for a in range(0, len(moons)):
    for b in range(a, len(moons)):
      if a != b:
        if moons[a][0] < moons[b][0]:
          vel[a][0] += 1
          vel[b][0] -= 1
        if moons[a][0] > moons[b][0]:
          vel[a][0] -= 1
          vel[b][0] += 1
        if moons[a][1] < moons[b][1]:
          vel[a][1] += 1
          vel[b][1] -= 1
        if moons[a][1] > moons[b][1]:
          vel[a][1] -= 1
          vel[b][1] += 1
        if moons[a][2] < moons[b][2]:
          vel[a][2] += 1
          vel[b][2] -= 1
        if moons[a][2] > moons[b][2]:
          vel[a][2] -= 1
          vel[b][2] += 1

def velocity():
  for a in range(0, len(moons)):
    moons[a][0] += vel[a][0]
    moons[a][1] += vel[a][1]
    moons[a][2] += vel[a][2]


def energy():
  retval = 0
  for a in range(0, len(moons)):
    pot = abs(moons[a][0])+abs(moons[a][1])+abs(moons[a][2])
    kin = abs(vel[a][0])+abs(vel[a][1])+abs(vel[a][2])
    tot = pot * kin
    retval += tot
  return retval



def print_moons():
  global moons
  global vel
  for i in range(0, len(moons)):
    print "pos=<x= " + str(moons[i][0]) + ', y= ' + str(moons[i][1]) + ', z= ' + str(moons[i][2]) + '>, vel=<x= ' + str(vel[i][0]) + ', y= ' + str(vel[i][1]) + ', z= ' + str(vel[i][2]) + '>'


while step < steps:
  step+=1
  print step
  gravity() 
  velocity()
  print_moons()

tot = energy()
print tot

