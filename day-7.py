input = [line.rstrip() for line in open('./inputs/day7.txt')]

dict = {}

for line in input:
	stripStart = line.index('(')
	stripEnd = line.index('>') if '>' in line else line.index(')')
	line = line[:stripStart] + line[stripEnd + 1:]
	line = line.replace(',', '')
	line = line.split(' ')
	print(line)
	for word in line: 
		if word in dict: dict[word] += 1
		else:
			dict[ word ] = 1


print(dict)