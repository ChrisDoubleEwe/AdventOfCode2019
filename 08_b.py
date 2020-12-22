import sys
import itertools


with open("08_a_input_data.txt") as f:
    content = f.readlines()

c = content[0].strip()
c_list = list(c)

layers = []

width = 25
height = 6

while len(c_list) > 0:
  layer = []
  for y in range(0, height):
    row = []
    for x in range(0, width):
      row += c_list.pop(0)
    layer.append(row)
  layers.append(layer)

min_zero_count = 10000000000
min_zero_layer = 0
layer_count = 0


for layer in layers:
  layer_count += 1
  layer_zero_count = 0
  for row in layer:
    for item in row:
      if item == '0':
        layer_zero_count += 1
  if layer_zero_count < min_zero_count:
    min_zero_count = layer_zero_count
    min_zero_layer = layer_count

#print "Layer with minimum zeroes:"
#print "  num zeroes: " + str(min_zero_count)
#print "  layer: " + str(min_zero_layer)

result_layer = []

for y in range(0, height):
  result_row = ''
  for x in range(0, width):
    this_pixel = -1
    for l in range (0, len(layers)):
      if layers[l][y][x] != '2':
        this_pixel = layers[l][y][x]
        break
    result_row += this_pixel
  result_layer.append(result_row)


for row in result_layer:
  p_row = ''
  for item in row:
    if item == '1':
      p_row = p_row + '*'
    else:
      p_row = p_row + ' '
  print p_row

