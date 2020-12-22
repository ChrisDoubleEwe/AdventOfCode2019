with open("01_input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
def calc_fuel(mass):
  return (mass / 3) -2

content = [x.strip() for x in content] 
total_fuel = 0
for mass in content:
  this_fuel = calc_fuel(eval(mass))
  print this_fuel
  total_fuel+=this_fuel
  while calc_fuel(this_fuel) >= 0:
    this_fuel = calc_fuel(this_fuel)
    print this_fuel
    total_fuel += this_fuel

print "-----------"
print total_fuel

