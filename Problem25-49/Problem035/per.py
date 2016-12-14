import math
from time import time

def is_circular_prime(prime):
	for i in range(len(prime)-1):
		prime = prime[1:len(prime)] + prime[0]
		if not prime in primes:
			return False
	return True

t0 = time()

primes = set()
f = open("primes.txt", "r")
primestxt = f.read()
primesstr = list(primestxt.split())
for i in range(0, len(primesstr)):
	primes.add(primesstr[i])

numCircularPrimes = 0
for prime in primes:
	if is_circular_prime(prime):
		numCircularPrimes += 1

print numCircularPrimes
print "--- TIME:", time() - t0, "---"