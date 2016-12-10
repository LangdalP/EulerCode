correctNumber = 0
pNum1 = 0
pNum2 = 0
numbers = []
breakCurr = False
highest = 99

for first in range(1000, 99, -1):
	for second in range(1000, highest, -1):
		numbers = list(map(int, str(first*second)))
		numCorrect = 0
		#f numbers == list(map(int, str(first*second)))_
		if len(numbers) % 2 == 0:
			for i in range(0,(int(len(numbers)/2))):
				if numbers[i] == numbers[len(numbers)-(i+1)]:
					numCorrect = numCorrect + 1
				if numCorrect == int(len(numbers)/2):
					if first*second > correctNumber:
						correctNumber = first * second
						pNum1 = first
						pNum2 = second
						highest = second
					break
		else:
			for i in range(0,(len(numbers))):
				if numbers[i] == numbers[len(numbers)-(i+1)]:
					numCorrect = numCorrect + 1
				else:
					break
				if numCorrect == len(numbers):
					if first*second > correctNumber:
						correctNumber = first * second
						pNum1 = first
						pNum2 = second
						hieghest = second
					break

print(correctNumber)
print(pNum1, pNum2)