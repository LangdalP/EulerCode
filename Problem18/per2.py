fname = "input.txt"
numberStrings = []
numberInt = []
numbers = []
with open(fname) as f:
    content = f.readlines()

for i in range(0, len(content)):
	content[i] = content[i].strip("\n")
	numberStrings.append(content[i].split(" ")) 
	numberInt = []
	for j in range(0, i+1):
		numberInt.append(int(numberStrings[i][j]))
	numbers.append(numberInt)

numbers = numbers[::-1]
for line in numbers:
	if len(line) != 1:
		for i in range(0, len(line)-1):
			numbers[len(numbers)-len(line)+1][i] += max(line[i], line[i+1])

print(numbers[len(numbers)-1][0])