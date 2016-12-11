import math
import random
from time import time

def isPrime(n, k):
	# n > 1, k accuracy of test(int, the higher the better, min 1)
	if n in primes:
		return True
	elif n in nonPrimes:
		return False
	elif n > 3 and n % 2 != 0:
		if millerPrimalityTest(n, k):
			primes.add(n)
			return True
		else:
			nonPrimes.add(n)
			return False
	else:
		nonPrimes.add(n)
		return False

def millerPrimalityTest(n, k):
	# n > 3, k = accuracy of test
	# returns True if n is probably prime, False if composite
	for r in range(1, n):
		if (n - 1) % (2 ** r) != 0:
			r -= 1
			break
	d = n / 2**r

	for WitnessLoop in range(k):
		if k == 1:
			a = 2
		else:
			a = random.randrange(2, n - 2, 1)
		x = (a ** d) % n

		if x == 1 or x == n - 1:
			continue
		continueWitnessLoop = False
		for i in range(r-1):
			x = (x ** 2) % n
			if x == 1:
				return False
			if x == n - 1:
				continueWitnessLoop = True
				break
		if continueWitnessLoop:
			continue
		return False
		
	return True
	

t0 = time()
random.seed()

primes = {3, 2}
nonPrimes = {1}
highestN, highestA, highestB = 0, 0, 0

for a in range(-999, 1000):
	for b in range(-1000, 1001):
		n = 0
		while True:
			if isPrime((n ** 2) + a * n + b, 1):
				n += 1
				continue
			if n > highestN:
				highestN = n
				highestA = a
				highestB = b
			break

print highestN, highestA, highestB, highestB * highestA
print "--- TIME:", time() - t0, "---"