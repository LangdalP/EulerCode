import math

def isPrime(candidate):
	if candidate < 9:
		return True
	elif candidate % 3 == 0:
		return False
	else:
		r=math.floor(math.sqrt(candidate))
		f = 5
		while f<=r:
			if candidate % f== 0:
				return False
			if candidate % (f+2) == 0:
				return False
			f = f + 6
		return True

limit = 2*10**6
sum = 2
for i in range(3, limit, 2):
	if isPrime(i):
		sum = sum + i
print(sum)