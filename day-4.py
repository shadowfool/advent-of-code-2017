
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



# ---- CHALLENGE 2 ------
badCount = 0

def letterMap(word=''):
  mp = {}
  for i, letter in enumerate(''.join(sorted(word))):
    if letter not in mp: mp[ letter ] = 0
    mp[ letter ] = mp[ letter ] + 1
  return mp
  
for line in input:
  words = line.split(' ')
  words = [ letterMap(word) for word in words ]
  if len(words) != len([dict(t) for t in set([tuple(d.items()) for d in words])]):
    badCount = badCount + 1
print(len(input) - badCount)