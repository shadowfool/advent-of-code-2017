input = [line.rstrip() for line in open('./inputs/day7.txt')]

dict = {}
#### CHEESED PART 1 #####
for line in input:
	stripStart = line.index('(')
	stripEnd = line.index('>') if '>' in line else line.index(')')
	line = line[:stripStart] + line[stripEnd + 1:]
	line = line.replace(',', '')
	line = line.split(' ')
	for word in line: 
		if word in dict: dict[word] += 1
		else:
			dict[ word ] = 1


##### PART 2 #######
dict2 = {}
comb = {}

input2 = [ line.rstrip() for line in open('./inputs/day7.txt') ]


