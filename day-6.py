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
  if round != 0: pastMoves[ ('-').join( mapIntToString( input ) ) ] = round

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

key = ('-').join( mapIntToString([2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]))
print(round,  pastMoves[ key ])

