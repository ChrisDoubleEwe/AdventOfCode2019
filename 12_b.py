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


start_x = ''
start_y = ''
start_z = ''

for i in range(0, len(moons)):
  start_x += "pos=<x= " + str(moons[i][0]) + '> , vel=<x= ' + str(vel[i][0]) + '>'
  start_y += "pos=<y= " + str(moons[i][1]) + '> , vel=<y= ' + str(vel[i][1]) + '>'
  start_z += "pos=<z= " + str(moons[i][2]) + '> , vel=<z= ' + str(vel[i][2]) + '>'

print start_x
print start_y
print start_z


steps = 4686774999
step = 0

seen = []

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def gcd3(a, b, c):
  gcd_ab = gcd(a, b)
  gcd_abc = gcd(gcd_ab, c)
  return gcd_abc

def lcm2(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b  / gcd(a, b)

def lcm(a, b, c):
    mul1 = lcm2(b, c) 
    return lcm2(a, mul1)


def lcmz(x, y, z):  
   if x > y:  
       if z > x:
         greater = z
         smaller = y 
       else:
         greater = x
         if z > y:
           smaller = y
         else:
           smaller = z
   else:  
       if z > y:
         greater = z
         smaller = x
       else:
         greater = y  
         if z > x:
           smaller = x
         else:
           smaller = z

   val = greater
   while(True):
       print "looking for   374307970285176"
       print "got as far as " + str(greater)
       if((greater % x == 0) and (greater % y == 0) and (greater % z == 0)):  
           lcm = greater  
           break  
       greater += val
   return lcm  

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

this = ''
for i in range(0, len(moons)):
    this += "pos=<x= " + str(moons[i][0]) + ', y= ' + str(moons[i][1]) + ', z= ' + str(moons[i][2]) + '>, vel=<x= ' + str(vel[i][0]) + ', y= ' + str(vel[i][1]) + ', z= ' + str(vel[i][2]) + '>'
seen.append(this)


rep_x = -1
rep_y = -1
rep_z = -1

while step < steps:
  step+=1
  gravity() 
  velocity()

  this_x = ''
  this_y = ''
  this_z = ''

  for i in range(0, len(moons)):
    this_x += "pos=<x= " + str(moons[i][0]) + '> , vel=<x= ' + str(vel[i][0]) + '>'
    this_y += "pos=<y= " + str(moons[i][1]) + '> , vel=<y= ' + str(vel[i][1]) + '>'
    this_z += "pos=<z= " + str(moons[i][2]) + '> , vel=<z= ' + str(vel[i][2]) + '>'

  if this_x == start_x and rep_x < 0:
    print this_x
    print "X repeats after " + str(step) + " steps"
    rep_x = step

  if this_y == start_y and rep_y < 0:
    print this_y
    print "Y repeats after " + str(step) + " steps"
    rep_y = step

  if this_z == start_z and rep_z < 0:
    print this_z
    print "Z repeats after " + str(step) + " steps"
    rep_z = step

  if rep_x >= 0 and rep_y >=0 and rep_z >= 0:
    print "Finished"
    break

print "Calculating lcm..."
tot = lcm(rep_x, rep_y, rep_z)
print tot
