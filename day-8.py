
input = [ line.rstrip().split(' ') for line in open('./inputs/day8.txt')]

instructionDict = {
  'inc': 1,
  'dec': -1
}

registers = {
  
}
highestValue = 0


for instruction in input:
  base = instruction[0]
  modifier = instructionDict[instruction[1]]
  action = instruction[2]
  conditionCompare = instruction[4]
  condition = instruction[5]
  conditionAmount = instruction[6]

  if not conditionCompare in registers: registers[conditionCompare] = 0
  if not base in registers: registers[base] = 0

  if eval(''.join([ str(registers[conditionCompare]),' ',condition,' ',conditionAmount])):
    registers[ base ] = int(registers[ base ]) + ( int(modifier) * int(action) )
  
  if(registers[ base ] > highestValue): highestValue = registers[ base ]


print(registers[max(registers, key=registers.get)])
print(highestValue)
