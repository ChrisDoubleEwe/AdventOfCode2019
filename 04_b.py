import sys

def contains_double(n):
  print "======"
  print n
  pair = 0
  last = ''
  for x in str(n):
    if x == last:
      pair += 1
    else:
      if pair == 1:
        return 1
      else:
        pair = 0
    print x + "   " + str(pair)

    last = x
  if pair == 1:
    return 1
  return 0

def ordered_numbers(n):
   n_sorted = ''.join(sorted(str(n)))
   if str(n) == n_sorted:
     return 1
   return 0

#print contains_double(112233)
#print contains_double(123444)
#print contains_double(111122)
#sys.exit()
total = 0
for n in range(234208, 765869):
  if contains_double(n):
    if ordered_numbers(n):
      print n
      total += 1

print "======"
print total

