from math import factorial

for i in range(3, 100000):
	sumi = 0
	for digit in repr(i):
		sumi += factorial(int(digit))
	if sumi == i:
		print i