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

def bestSum(x, y, n):
	global numbers
	if y > len(numbers)-1:
		return 0
	elif n == 0:
		return numbers[y][x]
	else:
		leftValue = bestSum(x, y+1, n-1)
		rightValue = bestSum(x+1, y+1, n-1)
		return numbers[y][x] + max(leftValue, rightValue)

path = []
lastPos = 0
dep = 25

for line in numbers:
	if len(line) == 1:
		path.append(numbers[0][0])
	elif bestSum(lastPos, len(line)-1, dep) > bestSum(lastPos+1, len(line)-1, dep):
		path.append(line[lastPos])
	else:
		path.append(line[lastPos+1])
		lastPos += 1
	print(len(path))
print(path)
print(sum(i for i in path))