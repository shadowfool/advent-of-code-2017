def mapIntToString(stringList):
  return [ str(i) for i in stringList ]

def mapStringsToInt(intList):
  return [ int(i) for i in intList ]

input = open('./inputs/day6.txt', 'r').read().split(' ')

input = mapIntToString(input)

cont = True
round = 0
pastMoves = {}

def findHighestNumber( arr ):
  highestIndex = 0
  for index, number in enumerate(arr):
    if number > arr[ highestIndex ]: highestIndex = index

  return highestIndex


while cont is True:
  pastMoves[ ('-').join( mapIntToString( input ) ) ] = True

  count = 0
  input = mapStringsToInt(input)
  round += 1
  highestIndex = findHighestNumber( input )
  count = input[ highestIndex ]
  input[ highestIndex ] = 0
  currentIndex = highestIndex

  while count is not 0:
    currentIndex += 1
    if currentIndex > len(input) - 1: currentIndex = 0
    input[ currentIndex ] += 1
    count -= 1
  if ('-').join( mapIntToString( input ) ) in pastMoves:
    cont = False
    break;

print(round)


###### ROUND 2 ###########

cont2 = True
round2 = 0
pastMoves2 = {}

input2 = open('./inputs/day6.txt', 'r').read().split(' ')

input2 = mapIntToString( input2 )

checkFor = ('-').join( input2 )

input2 = mapStringsToInt(input2)
print(checkFor)

while cont2 is True:

  count2 = 0
  round2 += 1
  highestIndex2 = findHighestNumber( input2 )
  count2 = input2[ highestIndex2 ]
  input2[ highestIndex2 ] = 0
  currentIndex2 = highestIndex2

  while count2 is not 0:
    currentIndex2 += 1
    if currentIndex2 > len(input2) - 1: currentIndex2 = 0
    input2[ currentIndex2 ] = input2[ currentIndex2 ] + 1
    count2 -= 1
    

print(round2, input2)

