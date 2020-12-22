def contains_double(n):
  pair = 0
  last = ''
  for x in str(n):
    if x == last:
      pair = 1
    last = x
  return pair

def ordered_numbers(n):
   n_sorted = ''.join(sorted(str(n)))
   if str(n) == n_sorted:
     return 1
   return 0

total = 0
for n in range(234208, 765869):
  if contains_double(n):
    if ordered_numbers(n):
      print n
      total += 1

print "======"
print total

