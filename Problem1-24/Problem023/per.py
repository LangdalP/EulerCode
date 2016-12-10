def isAbundant(n):
	num = 0
	for i in range(1, n//2+1):
		if n % i == 0:
			num += i
	if num > n:
		return True
	return False

def sumTwoAbundant(n):
	global abundant
	for i in range(0, min(n, len(abundant))):
		for j in range(i,  min(n, len(abundant))):
			if abundant[i]+abundant[j] == n:
				return True
	return False

abundant = []
roof = 28124
numbers = []

for i in range(1,roof):
	if (i % 2 == 0 or i % 5 == 0) and isAbundant(i):
		abundant.append(i)

for num in range(1, roof):
	if num < 47 or num % 2 != 0:
		if not sumTwoAbundant(num):
			numbers.append(num)
			print num

print(sum(numbers))