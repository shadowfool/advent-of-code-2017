input = [line.rstrip() for line in open('./inputs/day4.txt')]
badWords = 0

for line in input: 
  dictionary = {}
  words = line.split(' ')
  for word in words:
    print(words)
    if word in dictionary:
      badWords = badWords + 1
      break
    dictionary[ word ] = 1

print(len(input) - badWords)


444

456