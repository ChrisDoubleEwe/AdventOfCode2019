path = [1, 1, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 3, 3, 2, 2, 3, 3, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 2, 2, 2, 2, 4, 4, 1, 1, 1, 1, 4, 4, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 3, 3, 2, 2, 3, 3, 3, 3, 1, 1, 4, 4, 1, 1, 4, 4, 4, 4, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 4, 4, 4, 4, 1, 1, 4, 4, 2, 2, 4, 4, 2, 2, 4, 4, 4, 4, 2, 2, 2, 2, 3, 3, 2, 2, 4, 4, 2, 2, 2, 2, 4, 4, 4, 4, 1, 1, 3, 3, 1, 1, 1, 1, 4, 4, 4, 4, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 4, 4, 2, 2, 3, 3, 2, 2, 4, 4, 2, 2, 3, 3, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 1, 1, 3, 3, 1, 1, 4, 4, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 4, 4, 1, 1, 4, 4, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 1, 1, 3, 3, 3, 3, 1, 1]

def optimize(path):
  modified = 1
  while modified == 1:
    print "Looping..."
    for i in range(0, len(path)-1):
      modified = 0
      if path[i] == 1 and path[i+1] == 2:
        modified = 1
        print "N + S : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break
      if path[i] == 2 and path[i+1] == 1:
        modified = 1
        print "S + N : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break
      if path[i] == 3 and path[i+1] == 4:
        modified = 1
        print "W + E : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break
      if path[i] == 4 and path[i+1] == 3:
        modified = 1
        print "E + W : removing at position " + str(i)
        path.pop(i+1)
        path.pop(i)
        break

  return path
print optimize(path)
