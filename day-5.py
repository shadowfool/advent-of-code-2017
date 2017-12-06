input = [int(line) for line in open('./inputs/day5.txt')]

escape = False
index = 0
steps = 0

while escape == False:
  if index > len( input ) - 1 or index < 0:
    escape = True
    break

  oldIndex = index
  current = input[ index ]
  index = current + index
  input[ oldIndex ] += 1
  steps += 1

print(steps)


# ---- CHALLENGE 2 ------
input2 = [int(line) for line in open('./inputs/day5.txt')]


escape = False
index = 0
steps = 0

while escape == False:
  if index > len( input2 ) - 1 or index < 0:
    escape = True
    break

  oldIndex = index
  current = input2[ index ]
  index = current + index
  input2[ oldIndex ] =  input2[ oldIndex ] + (-1 if current >= 3 else 1)
  steps = steps + 1

print(steps)