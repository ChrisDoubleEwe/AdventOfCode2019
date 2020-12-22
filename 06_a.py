with open("06_a_input.txt") as f:
    content = f.readlines()

pairs = {}
for pair in content:
  values = pair.split(')')
  pairs[values[1].strip()] = values[0].strip()

def get_chain_length(key):
  global pairs
  chain_length = 1
  if key not in pairs:
    return 0
  while pairs[key] != 'COM':
    key = pairs[key]
    chain_length += 1
  return chain_length

def get_common_ancestor(s1, s2):
  s_res = ''
  for s in range(0, len(s1)):
    if s1[s] == s2[s]:
      s_res += s1[s]
    else:
      t = s_res[0:s_res.rindex('-')]
      anc = t[t.rindex('-')+1:]
      return anc
      break
 
def get_chain(key):
  global pairs
  chain = ''
  chain_list = []
  if key not in pairs:
    return 'COM-'
  while pairs[key] != 'COM':
    key = pairs[key]
    chain_list.append(key)
  chain_list.reverse()
  for k in chain_list:
    chain = chain + '-' + k
  chain = 'COM' + chain
  return chain

you_chain = get_chain('YOU')
san_chain =  get_chain('SAN')

anc = get_common_ancestor(you_chain, san_chain)

you_len = get_chain_length('YOU')
san_len = get_chain_length('SAN')
anc_len = get_chain_length(anc)

dist = (you_len - (anc_len+1)) + (san_len - (anc_len+1))
print str(dist)

