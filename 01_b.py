with open("03_a_input.txt") as f:
    content = f.readlines()

wire1 = content[0]
wire2 = content[1]
steps = 0

grid_size = 7200
#grid_size = 7200

cur_x = grid_size
cur_y = grid_size

grid = []
a_steps = []
b_steps = []

row = []
for x in range(0, grid_size*2+1):
  row.append(' ')

grid = []
for x in range(0, grid_size*2+1):
  grid.append(list(row))
  a_steps.append(list(row))
  b_steps.append(list(row))


grid[cur_x][cur_y] = 'o'
 
def draw_cell(n, x, y):
  global grid
  global steps
  global a_steps
  global b_steps
  steps = steps + 1
  if grid[y][x] == ' ' or grid[y][x] == n:
    grid[y][x] = str(n)
  else:
    grid[y][x] = 'X'
  if n == '1':
    if a_steps[y][x] == ' ':
      a_steps[y][x] = steps 
  else:
    if b_steps[y][x] == ' ':
      b_steps[y][x] = steps




def draw_wire(num, dir, length):
  global grid
  global steps
  global cur_x
  global cur_y
  if dir == 'R':
    while length > 0:
      cur_x = cur_x + 1
      draw_cell(num, cur_x, cur_y)
      length = length -1
  if dir == 'L':
    while length > 0:
      cur_x = cur_x - 1
      draw_cell(num, cur_x, cur_y)
      length = length -1
  if dir == 'U':
    while length > 0:
      cur_y = cur_y - 1
      draw_cell(num, cur_x, cur_y)
      length = length -1
  if dir == 'D':
    while length > 0:
      cur_y = cur_y + 1
      draw_cell(num, cur_x, cur_y)
      length = length -1

def process_wire(path, id):
  global steps
  global cur_x
  global cur_y
  steps = 0
  cur_x = grid_size
  cur_y = grid_size
  for seg in path.split(','):
    dir = seg[0]
    length = seg[1:]
    draw_wire(id, dir, eval(length))

 
process_wire(wire1, '1')
process_wire(wire2, '2')


 
#for row in grid:
#  print row

smallest = 1000000000
for x in range(0, grid_size*2+1):
  for y in range(0, grid_size*2+1):
    if grid[y][x] == 'X':
      distance = a_steps[y][x] + b_steps[y][x]
      print distance
      if distance < smallest:
        smallest = distance
print smallest
