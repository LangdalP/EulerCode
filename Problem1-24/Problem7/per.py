def isprime(num):
	for i in range(3, num, 2):
		if num % i == 0:
			return False
	return True

numPrime = 1
currNumber = 3
while numPrime < 10001:
	if isprime(currNumber):
		numPrime += 1
	currNumber += 2

print(currNumber-2)
