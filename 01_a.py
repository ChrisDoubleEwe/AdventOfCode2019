with open("03_a_input.txt") as f:
    content = f.readlines()

wire1 = content[0]
wire2 = content[1]

#grid_size = 7200
grid_size = 7200

cur_x = grid_size
cur_y = grid_size

grid = []

row = []
for x in range(0, grid_size*2+1):
  row.append(' ')

grid = []
for x in range(0, grid_size*2+1):
  grid.append(list(row))

grid[cur_x][cur_y] = 'o'
 
def draw_cell(n, x, y):
  global grid
  if grid[y][x] == ' ' or grid[y][x] == n:
    grid[y][x] = str(n)
  else:
    grid[y][x] = 'X'

def draw_wire(num, dir, length):
  global grid
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
  global cur_x
  global cur_y
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

smallest = grid_size*2
for x in range(0, grid_size*2+1):
  for y in range(0, grid_size*2+1):
    if grid[y][x] == 'X':
      distance = abs(y-grid_size) + abs(x-grid_size)
      if distance < smallest:
        smallest = distance
print smallest
